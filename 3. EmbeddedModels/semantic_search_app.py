from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-mpnet-base-v2"
)

docs = [
    "Narendra Modi is the Prime Minister of India known for economic reforms and digital initiatives",
    "Joe Biden is the President of the United States focusing on climate policy and international alliances",
    "Xi Jinping is the President of China emphasizing centralized power and economic growth",
    "Vladimir Putin is the President of Russia known for strong leadership and geopolitical strategies",
    "Emmanuel Macron is the President of France promoting European unity and liberal economic policies",
    "Olaf Scholz is the Chancellor of Germany focusing on economic stability and energy transition",
    "Rishi Sunak is the Prime Minister of the United Kingdom working on economic recovery and fiscal policy",
    "Justin Trudeau is the Prime Minister of Canada known for progressive policies and multiculturalism",
    "Fumio Kishida is the Prime Minister of Japan focusing on defense reforms and economic security",
    "Volodymyr Zelenskyy is the President of Ukraine known for leadership during the Russia-Ukraine conflict"
]

print("Enter your Query regarding WORLD LEADERS : ")
query = input()

docu_embeddings = embeddings.embed_documents(docs)
query_embeddings = embeddings.embed_query(query)

#2d list must be passed in cos similarity
# print("Cosine Similarity : ",cosine_similarity([query_embeddings],docu_embeddings))

scores = cosine_similarity([query_embeddings],docu_embeddings)[0] #2d to 1d thats why [0]

print(sorted(list(enumerate(scores)),key=lambda x:x[1])) #enumerate to add (0,[similarity score])