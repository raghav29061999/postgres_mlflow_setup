# MLflow + PostgreSQL Setup Guide

This guide explains how to set up MLflow with a PostgreSQL backend, including database setup, MLflow configuration, migration, and server startup.

---

# 📌 Overview

This setup uses:

- PostgreSQL → Backend store (metadata)
- Local filesystem → Artifacts (traces, outputs)
- MLflow server → Tracking + UI

---

# 🛠️ 1. PostgreSQL Setup (pgAdmin)

## Step 1: Create User

Go to:

```
Login/Group Roles → Create → Login/Group Role
```

Fill:

- Name: `<DB_USER>`
- Password: `<DB_PASSWORD>`
- Enable: Can Login

---

## Step 2: Create Database

Go to:

```
Databases → Create → Database
```

Fill:

- Database Name: `<DB_NAME>`
- Owner: `<DB_USER>`

---

## Step 3: Grant Permissions

Open Query Tool and run:

```sql
GRANT ALL PRIVILEGES ON DATABASE <DB_NAME> TO <DB_USER>;
GRANT ALL ON SCHEMA public TO <DB_USER>;
```

Optional (recommended):

```sql
ALTER DATABASE <DB_NAME> OWNER TO <DB_USER>;
```

---

# 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙️ 3. Environment Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=<YOUR_API_KEY>

MLFLOW_TRACKING_URI=http://127.0.0.1:5000
MLFLOW_EXPERIMENT_NAME=Agno-Math-Agent

APP_VERSION=0.1.0
APP_ENV=dev

POSTGRES_USER=<DB_USER>
POSTGRES_PASSWORD=<DB_PASSWORD>
POSTGRES_DB=<DB_NAME>
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```

---

# 🚀 4. Start MLflow Server (Initial Run)

```bash
mlflow server \
  --backend-store-uri postgresql://<DB_USER>:<DB_PASSWORD>@127.0.0.1:5432/<DB_NAME> \
  --artifacts-destination ./mlruns \
  --host 127.0.0.1 \
  --port 5000
```

---

# 🔄 5. Database Migration (After MLflow Upgrade)

If you upgrade MLflow and see schema mismatch error, run:

```bash
mlflow db upgrade postgresql://<DB_USER>:<DB_PASSWORD>@127.0.0.1:5432/<DB_NAME>
```

This upgrades the database schema to match the MLflow version.

---

# 🔁 6. Restart MLflow Server

After migration, restart MLflow:

```bash
mlflow server --backend-store-uri postgresql://<DB_USER>:<DB_PASSWORD>@127.0.0.1:5432/<DB_NAME> --artifacts-destination ./mlruns --host 127.0.0.1 --port 5000
```

---

# 🌐 7. Access MLflow UI

Open in browser:

```
http://127.0.0.1:5000
```

---

# 🧠 Notes

- PostgreSQL stores:
  - runs
  - metrics
  - params
  - traces (MLflow 3.x)

- Artifacts (traces JSON, outputs) are stored in:

```
./mlruns/
```

- Always use `MLFLOW_TRACKING_URI` in your application (not DB URI)

---

# 📁 Local Data Exports

- The `all_data/` folder is intentionally ignored by Git and should stay local only. It may contain downloaded database exports, traces, and metadata that should not be shared from the repo.

- The list of tables created in the MLflow PostgreSQL database was captured in `all_data/all_tables_made.csv`.

- Tables created:
  - `logged_model_metrics`
  - `tags`
  - `params`
  - `metrics`
  - `runs`
  - `logged_model_params`
  - `alembic_version`
  - `experiment_tags`
  - `latest_metrics`
  - `datasets`
  - `input_tags`
  - `trace_tags`
  - `trace_request_metadata`
  - `logged_models`
  - `logged_model_tags`
  - `inputs`
  - `trace_info`
  - `assessments`
  - `entity_associations`
  - `webhook_events`
  - `scorers`
  - `scorer_versions`
  - `evaluation_dataset_tags`
  - `evaluation_dataset_records`
  - `endpoint_tags`
  - `trace_metrics`
  - `jobs`
  - `endpoint_model_mappings`
  - `online_scoring_configs`
  - `endpoint_bindings`
  - `span_metrics`
  - `spans`
  - `experiments`
  - `registered_models`
  - `model_versions`
  - `registered_model_tags`
  - `model_version_tags`
  - `registered_model_aliases`
  - `evaluation_datasets`
  - `webhooks`
  - `secrets`
  - `endpoints`
  - `model_definitions`
  - `workspaces`
  - `budget_policies`
  - `issues`

- Useful tables for this project were downloaded and saved locally as CSV files inside `all_data/`:
  - `experiments.csv`
  - `runs.csv`
  - `spans.csv`
  - `span_metrics.csv`
  - `tags.csv`
  - `trace_info.csv`
  - `trace_metrics.csv`
  - `trace_request_metadata.csv`
  - `trace_tags.csv`
  - `all_tables_made.csv`

---

# ✅ Summary

Steps:

1. Setup PostgreSQL (user + DB + permissions)
2. Install dependencies
3. Configure `.env`
4. Start MLflow server
5. Run your application
6. (Optional) Run DB migration after upgrades

---

# 🔥 Ready for

- Agent observability
- ML experiment tracking
- Tracing (LLM + tools)

---

Happy building 🚀
