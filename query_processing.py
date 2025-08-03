# User interaction 
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

from dotenv import load_dotenv
load_dotenv()

vectorstore = FAISS.load_local(
    "vectorstores/hr_policy",
    OpenAIEmbeddings(model="text-embedding-3-small"),
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    
template = """ 
Question: {question}
Answer using information from the following context only: {context}
Limit your answer to 2 or 3 lines.
"""
prompt = ChatPromptTemplate.from_template(template)

llm = ChatOpenAI(model="gpt-4o-mini")

def get_context_and_question(question):
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    return {"context": context, "question": question}

chain = RunnableLambda(get_context_and_question) | prompt | llm | StrOutputParser()

while True:
    question = input("Ask a question (or type 'exit' to quit): ")
    if question.lower() in ['exit', 'quit']:
        break
    response = chain.invoke(question)
    print("Answer:", response)
    print("-" * 40)
    