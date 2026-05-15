from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M1-80k", 
    task="text-generation",
    provider='novita'
   
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    
    name : str = Field(description='Name of person')
    age: int = Field(gt=18,description='age of the person')
    city: str = Field(description='City where the person belongs')
    
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
    
chain = template | model | parser
results = chain.invoke({'place':'Pakistan'})

print(results)
