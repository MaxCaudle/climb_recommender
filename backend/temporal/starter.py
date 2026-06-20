"""Small starter to launch a sample LLM workflow run.

Run with:
  python backend/temporal/starter.py

This will start a workflow instance and print the result when complete.
"""
import asyncio
from temporalio.client import Client
from backend.temporal import workflows


async def main():
    client = await Client.connect("temporal:7233")

    handle = await client.start_workflow(
        workflows.LLMWorkflow.run,
        "Yosemite",
        "El Capitan",
        id="llm-sample-1",
        task_queue="llm-task-queue",
    )

    print("Workflow started, waiting for result...")
    result = await handle.result()
    print("Workflow result:\n", result)


if __name__ == "__main__":
    asyncio.run(main())
