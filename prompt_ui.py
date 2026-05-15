from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2",
    temperature=0.7,
    provider="featherless-ai"
    
)

model = ChatHuggingFace(llm = llm)
st.header('Bookstagram')

# Dropdowns (selectbox)
response_type = st.selectbox(
    "Select Response Type",
    ["Detailed", "Summary", "Recommendations"]
)

depth = st.selectbox(
    "Select Depth",
    ["Short", "Medium", "Deep"]
)

tone = st.selectbox(
    "Select Tone",
    ["Casual", "Professional", "Exciting"]
)

user_query = st.text_input("Enter your book curiousity")
#prompt template
template = PromptTemplate(template=
    """
You are an intelligent book assistant.

User Query:
{user_query}

User Preferences:
- Response Type: {response_type}
- Depth: {depth}
- Tone: {tone}

Instructions:

1. If query is a BOOK NAME:
   Provide:
   - Genre
   - Summary (no spoilers)
   - Themes
   - Writing style
   - Who should read it
   - Similar books

2. If query is a MOOD / GENRE:
   - Recommend 5 books
   - Include title, author, short description, and reason

3. Adapt based on user preferences:
   - If Response Type = "Summary" → keep concise
   - If Response Type = "Detailed" → expand explanation
   - If Response Type = "Recommendations" → focus more on suggestions

   - If Depth = "Short" → bullet points only
   - If Depth = "Medium" → brief explanations
   - If Depth = "Deep" → detailed insights

   - Tone:
     • Casual → friendly
     • Professional → formal
     • Exciting → engaging and dramatic

4. Keep output structured and readable.

Now generate the best possible response.
""",
input_variables=['response_type','depth','tone','user_query']
)

#fillin the placeholders
prompt = template.invoke({
    'response_type' : response_type,
    'depth': depth,
    'tone': tone,
    'user_query':user_query
})

if st.button('Enter'):
    result = model.invoke(prompt)
    st.text(result.content)
    

