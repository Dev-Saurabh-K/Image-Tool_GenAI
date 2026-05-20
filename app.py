from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
# from langchain.agents import create_agent
from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field
load_dotenv()

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to multiply")
    b: int = Field(required=True, description="The second number to multiply")

@tool
def get_weather(city: str) -> str:
    """Get weather for a given City"""
    return f"It's always sunny in {city}"

def multiply_func(a: int, b: int)-> int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput

)

print(multiply_tool.invoke({"a":3,"b":5}))

print(get_weather.invoke('kolkata'))
# print(get_weather.description)
# print(get_weather.name)
# print(get_weather.args)

# agent = create_agent(
#     model="gemini-2.5-flash-lite",
#     tools=[get_weather],
#     system_prompt="You are a helpful assistant."
# )


# result = agent.invoke(
#     {
#         "messages":[
#             HumanMessage(content="tell me about weather of kolkata")
#         ]
#     }
# )
# print(result)


# url = "https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={topic}&gsrnamespace=6&prop=imageinfo&iiprop=url&format=json"


# history = [
#     SystemMessage(
#         content=f"You are a image searching tool which find image public url based on user input. use url = {url}"
#     )
# ]

# history = []

# print(history)

# model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

# while True:
#     query = input("You:")
#     history.append(HumanMessage(content=query))
#     result = model.invoke(history)
#     history.append(AIMessage(content=result.text))
#     print(result.text)
#     # print(history)

#     if query=='exit':
#         break