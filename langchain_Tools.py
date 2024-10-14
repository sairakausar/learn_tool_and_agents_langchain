from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_core.runnables import RunnableSequence

llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAidgZgpXu9mvAPEMSGGeiRaAdWF05rd5s")

prompt_template = PromptTemplate(
    input_variables=["input"],
    template="you are a tool caller. : {input}\n"
)
@tool
def add_numbers_tools(input_data: str) -> str:
    """addition of two numbers"""
    print("add number Tool ", input_data)
    return "you result is 10"

chain = RunnableSequence(
    prompt_template,
    llm,
    add_numbers_tools,
)

output = chain.invoke("5,10")
print("output", output)