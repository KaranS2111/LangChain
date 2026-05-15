from typing import TypedDict, Annotated,Literal
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    max_retries=2,
    # other params...
)

#schema
class Output(TypedDict):
    
    hype : Annotated[str,"A brief hype surrounding the film in its release year in one word"] #custom detail to llm
    summary : Annotated[str,"Summarize the review"] #the llm itself understands use summary and sentiment nikalna hai from the input we give to it
    sentiment: Annotated[Literal["+","-"],"Sentiment in one word"]

struct_model = model.with_structured_output(Output)

response = struct_model.invoke("Fitoor was an awesome film. The actors were pathetic however the songs were dope af!!!!.")

print(response)
# print(response['summary'])
# print(response['sentiment'])


