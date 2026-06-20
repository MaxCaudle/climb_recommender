from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from temporalio.client import Client
from ..temporal import workflows
import asyncio

app = FastAPI()


class RecommendRequest(BaseModel):
    location: str
    climb: str


class RecommendResponse(BaseModel):
    recommendation: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/recommend", response_model=RecommendResponse)
async def recommend(req: RecommendRequest):
    """Start the Temporal LLM workflow and return its result.

    This connects to the Temporal service at `temporal:7233` (docker-compose
    service) and starts `LLMWorkflow`. It waits for the workflow result and
    returns it to the HTTP client.
    """
    try:
        client = await Client.connect("temporal:7233")
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Temporal connect error: {e}")

    try:
        handle = await client.start_workflow(
            workflows.LLMWorkflow.run,
            req.location,
            req.climb,
            id=None,
            task_queue="llm-task-queue",
        )

        # Await result (this blocks the request until workflow completes).
        result = await handle.result()
        # `result` is expected to be the string returned by the workflow
        return RecommendResponse(recommendation=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Workflow error: {e}")

