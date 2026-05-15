from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")
chat_history = []
while True:
    user_input = input('You : ')
    chat_history.append(user_input)
    length = len(chat_history)
    if length>10:
        summary = model.invoke(f"summarize {chat_history} in 50 words")
        chat_history.clear()
        chat_history.append(summary.content)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    
    print("AI : ",result.content)
    print(chat_history)