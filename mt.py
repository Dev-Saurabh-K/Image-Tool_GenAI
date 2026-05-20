from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field
load_dotenv()


@tool
def add(a:int , b:int) -> int:
    """Add two numbers"""
    return a+b


@tool
def multiply(a:int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

class MathToolkit:
    def get_tools(self):
        return [add, multiply]
    

toolkit = MathToolkit()
tools = toolkit.get_tools()
print(tools)