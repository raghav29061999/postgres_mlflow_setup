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

