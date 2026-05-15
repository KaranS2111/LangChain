from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history=[]
#loading chat history
with open('msg_placeholders/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

#prompt creation
prompt = chat_template.invoke({
    'chat_history' : chat_history,
    'query': 'where is my order?'
})

print(prompt)

#here we can add a model and invoke it further