from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M1-80k", 
    task="text-generation",
    provider='novita'
   
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()
temp = PromptTemplate(
    template='Give me the name, age, city of a Fictional Indian male person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    
)

prompt = temp.format()
#print(prompt)
result = model.invoke(prompt)
#print(result)

# final_res = parser.parse(result.content)
# print(final_res)
# print(final_res['name'])

#chain method
chain = temp | model |parser
resultda = chain.invoke({}) #chain.invoke takes input as an argument which is must have. if we 
#dont have any then send an empty dictionary. will work

print(resultda)