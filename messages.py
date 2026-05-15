from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-20b")
msgs = [
    SystemMessage(content="You are a Bollywood critic"),
    HumanMessage(content="Tell me about Swades")
]

result = model.invoke(msgs)
msgs.append(AIMessage(content=result.content))

print(msgs)

#we can integrate this system, human and ai format msgs
# in our own chatbot in chatbot.py 