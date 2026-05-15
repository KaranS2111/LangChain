from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
# for model to download locally in D drive instead of C because it's full.

os.environ["HF_LOCAL_RUN"]= 'D:/hf_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id="Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2",
    task = 'text-generation',
    pipeline_kwargs= dict(
        temperature = 0.9,
        max_new_tokens = 100
    )
    
)

model = ChatHuggingFace(llm = llm)

response = model.invoke("what is capital of Iran")

print(response.content)