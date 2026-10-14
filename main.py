from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.tools import tool

#1. Initialize the chat model
model = init_chat_model("groq:openai/gpt-oss-120b")

#2.Define your tools
@tool
def multiply(a: float, b:float) -> float:
    """Multiplies two numbers. Use for multiplication operations."""
    return a * b
@tool
def divide(a: float, b:float) -> float:
    """Divide the first number by the second number. Return error if dividing by zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

#3 Create the LangChain Agent -
agent = create_agent(model,[multiply, divide])

#4. Run it
result = agent.invoke({"messages":[
    ("user", "What is 10 multiplied by 5, then divided by 2?")
]})

print(result)