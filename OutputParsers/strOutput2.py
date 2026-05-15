from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="allenai/Olmo-3.1-32B-Instruct", 
    task="text-generation",
    provider="publicai"
)

model = ChatHuggingFace(llm=llm)

temp1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

temp2 = PromptTemplate(
    template='Write a 3 line summary on following text report on : /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()
chain = temp1 | model | parser | temp2 | model | parser
result = chain.invoke({'topic':'IPL'})
print(result)