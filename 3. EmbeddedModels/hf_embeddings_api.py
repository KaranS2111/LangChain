from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-mpnet-base-v2"
)

docs = [
    "Rajasthan is beautiful",
    "Crocodiles live in freshwater",
    "Eid is a Muslim Festival"
]
query_result = embeddings.embed_documents(docs)
print(str(query_result))