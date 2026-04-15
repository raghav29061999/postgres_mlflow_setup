import os

from src.agents import get_math_agent
from src.config import setup_mlflow
from dotenv import load_dotenv
load_dotenv()


def main() -> None:
    # Call MLflow setup once at application startup
    setup_mlflow(
        version=os.getenv("APP_VERSION", "0.1.0"),
        env=os.getenv("APP_ENV", "dev"),
    )

    agent = get_math_agent()

    user_query = input("Enter your math question: ").strip()
    if not user_query:
        print("No input provided.")
        return

    try:
        agent.print_response(user_query, stream=True)
    except Exception as exc:
        print(f"Application error: {exc}")


if __name__ == "__main__":
    main()