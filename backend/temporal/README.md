# Temporal sample: LLM workflow

This folder contains a minimal Temporal workflow example that simulates an LLM-based
recommendation. It is intended to be run against the Temporal service defined in
the repository `docker-compose.yml` (service name: `temporal`, port 7233).

Files:
- `workflows.py` — workflow and a simulated `llm_activity`
- `worker.py` — worker process that polls `llm-task-queue` and runs workflows/activities
- `starter.py` — simple client that starts a workflow and waits for the result

Quick run (from repo root):

```bash
# 1) Make sure Temporal is up (docker compose should include temporal)
docker compose up -d temporal

# 2) Install backend requirements into a Python environment
pip install -r backend/requirements.txt

# 3) Start the worker in a terminal
python backend/temporal/worker.py

# 4) In another terminal, start the sample workflow
python backend/temporal/starter.py
```

Notes:
- The activity currently simulates an LLM. Replace `llm_activity` with a real LLM
  call or a call into another service or Temporal child workflow.
- You can run the worker inside the `backend` container if you prefer — the
  container already installs `requirements.txt`, so run the worker there.
