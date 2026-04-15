from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool


@tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b


@tool
def subtract_numbers(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b


@tool
def divide_numbers(a: float, b: float) -> float:
    """Divide the first number by the second."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def get_math_agent() -> Agent:
    """
    Create and return a simple math agent.
    """
    return Agent(
        name="Math Agent",
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[
            add_numbers,
            subtract_numbers,
            multiply_numbers,
            divide_numbers,
        ],
        instructions=[
            "You are a precise math assistant.",
            "Always use the available math tools for calculations.",
            "Return concise and correct answers.",
        ],
        markdown=True,
    )