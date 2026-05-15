from langchain_huggingface.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "This place is filthy"

query_result = embeddings.embed_query(text)

print(str(query_result))