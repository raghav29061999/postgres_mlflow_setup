import os


def setup_mlflow(version: str = "0.1.0", env: str = "dev") -> None:
    """
    Configure MLflow tracking and Agno autologging.

    This function is safe to call at application startup.
    """
    try:
        import mlflow
    except ImportError:
        print("MLflow not installed; skipping MLflow observability setup")
        return

    tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
    experiment_name = os.getenv("MLFLOW_EXPERIMENT_NAME", "Agno-Math-Agent")

    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)

    # Enable Agno tracing into MLflow
    mlflow.agno.autolog(log_traces=True)

    mlflow.set_tags(
        {
            "project_version": version,
            "environment": env,
            "framework": "agno",
            "application": "math-agent",
        }
    )

    print(f"MLflow tracking URI set to: {tracking_uri}")
    print(f"MLflow experiment set to: {experiment_name}")