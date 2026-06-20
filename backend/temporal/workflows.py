from datetime import timedelta
from temporalio import workflow, activity


@activity.defn
async def llm_activity(location: str, climb: str) -> str:
    """Simulated LLM activity — replace with real LLM call or integration.

    This activity would normally call an LLM or orchestrate prompts. For
    the sample we return a deterministic string so the workflow can be run
    without external keys.
    """
    # Simulate an LLM response (placeholder)
    return f"Recommendation: For {climb} in {location}, start with easy approach routes and check local conditions."


@workflow.defn
class LLMWorkflow:
    @workflow.run
    async def run(self, location: str, climb: str) -> str:
        # Execute the LLM activity with a 30s timeout
        return await workflow.execute_activity(
            llm_activity,
            location,
            climb,
            start_to_close_timeout=timedelta(seconds=30),
        )
