from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", #this model ain't good so I switched to a diff one in strOutput2.py
    task="text-generation",
    provider="featherless-ai"
)
#tinyLlama cant give struct output
model = ChatHuggingFace(llm=llm)

temp1 = PromptTemplate(
    template='Write a detailed report on {topic1}',
    input_variables=['topic1']
)

temp2 = PromptTemplate(
    template='Write a 3 line summary on following text report on : /n {topic}',
    input_variables=['topic']
)

prompt1 = temp1.invoke({'topic1':'KKR'})
result = model.invoke(prompt1)

prompt2 = temp2.invoke({'topic':result.content})
result_2 = model.invoke(prompt2)

print(result_2.content)