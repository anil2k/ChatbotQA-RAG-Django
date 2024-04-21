from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file, if it exists
load_dotenv()

CHROMA_PATH = r"chatbot\data\data\chroma"

PROMPT_TEMPLATE = """
Given data is leave rules of employees .
Find the answer on the following context:

{context}

---

Answer the question on the above context.: {question}
"""

def generate_response(query_text):
    # Prepare the DB.
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    
    # if len(results) == 0 or results[0][1] < 0.7:
    #     return "Unable to find matching results."

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatOpenAI()
    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    # response={"Response":response_text,
    #           "Sources":sources}
    response={"Response":response_text}
    return response

if __name__ == "__main__":
    query_text = "what are types of leaves"
    response = generate_response(query_text)
    print(response)
