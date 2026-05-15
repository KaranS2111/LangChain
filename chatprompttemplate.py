from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate(
    [
        SystemMessage(content="You are a helpful {domain} expert"),
        HumanMessage(content="Explain in simple terms, what is {topic}")
    ]
)

#better way
chat = ChatPromptTemplate(
    [
        ('system',"You are a helpful {domain} expert"),
        ('human',"Explain in simple terms, what is {topic}")
    ]
)


prompt = chat.invoke({
    'domain' : 'cricket',
    'topic':'australian cricket'
})

print(prompt)