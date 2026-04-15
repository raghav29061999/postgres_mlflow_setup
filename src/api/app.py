from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from src.agents.math_agent import get_math_agent
from src.config.ml_observability import setup_mlflow

# Load env
load_dotenv()

# Setup MLflow ONCE
setup_mlflow(
    version=os.getenv("APP_VERSION", "0.1.0"),
    env=os.getenv("APP_ENV", "dev"),
)

# Initialize agent ONCE
agent = get_math_agent()

app = FastAPI(title="Agno Math Agent API")


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    response: str


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        result = agent.run(req.query)

        # Depending on Agno version
        if hasattr(result, "content"):
            output = result.content
        else:
            output = str(result)

        return ChatResponse(response=output)

    except Exception as e:
        return ChatResponse(response=f"Error: {str(e)}")