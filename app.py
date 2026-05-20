from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

history = []

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

query = input("write your query.")
history.append(query)
result = model.invoke(query)
history.append(result.text)
print(result.text)
print(history)