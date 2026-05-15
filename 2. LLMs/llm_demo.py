import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = 
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2",
    temperature=0.7,
    provider="featherless-ai"
    
)
model = ChatHuggingFace(llm=llm)
response = model.invoke("What is Big Bang Theory?")
print(response.content)
print(response)