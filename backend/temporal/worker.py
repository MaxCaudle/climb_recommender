"""Temporal worker for running the LLM workflow.

Run with:
  python backend/temporal/worker.py

The worker connects to the Temporal service at temporal:7233 (compose).
"""
import asyncio
import os

from temporalio.client import Client
from temporalio.worker import Worker
from backend.temporal import workflows


async def main():
    # Retry loop: Temporal service may not be ready when the container starts.
    backoff = 1
    client = None
    while True:
        try:
            client = await Client.connect("temporal:7233")
            break
        except Exception as e:
            print(f"Temporal connect failed: {e}. Retrying in {backoff}s...")
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, 30)

    worker = Worker(
        client,
        task_queue="llm-task-queue",
        workflows=[workflows.LLMWorkflow],
        activities=[workflows.llm_activity],
    )
    print("Worker started, waiting for tasks on 'llm-task-queue'...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
