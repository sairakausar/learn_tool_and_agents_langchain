#..............1.......................
# from langchain_google_genai import GoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain_core.tools import tool
# from langchain_core.runnables import RunnableSequence

# llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAidgZgpXu9mvAPEMSGGeiRaAdWF05rd5s")

# prompt_template = PromptTemplate(
#     input_variables=["input"],
#     template="you are a tool caller. : {input}\n"
# )
# @tool
# def add_numbers_tools(input_data: str) -> str:
#     """addition of two numbers"""
#     print("add number Tool ", input_data)
#     return "you result is 10"

# chain = RunnableSequence(
#     prompt_template,
#     llm,
#     add_numbers_tools,
# )

# output = chain.invoke("5,10")
# print("output", output)
        #         /.......................2...................................../.....

# from langchain_google_genai import GoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain_core.tools import tool
# from langchain_core.runnables import RunnableSequence

# llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAidgZgpXu9mvAPEMSGGeiRaAdWF05rd5s")

# prompt_template = PromptTemplate(
#     input_variables=["input"],
#     template="You are a tool caller, you have to call the tool named add_number_tool if case if there is any addition required, please don't send any explanation while calling the function, just send the two numbers what users provided e.g 5,2, even though user give the sentance you have to find two numbers and pass to the functions, user input is : {input}\n"
# )
# @tool
# def add_numbers_tools(input_data: str) -> str:
#     """addition of two numbers"""
#     print("add number Tool ", input_data)
    
#     try: 
#         numbers =input_data.split(",")
        

#     except Exception as e:
#         return "No number found"

#     num1 = int(numbers[0])
#     num2 = int(numbers[1])
        
#     result= num1+num2

#     return f"The sum of {num1} and  {num2} is {result}"

#     #   #    or
#     #  #  result "The sum of", {num1}, "and", {num2}, "is", {result}


# chain = RunnableSequence(
#     prompt_template,
#     llm,
#     add_numbers_tools,
# )

# output = chain.invoke("5,10")
# print("output", output)
# .................................3..................................................
# from langchain_google_genai import GoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain_core.tools import tool
# from langchain_core.runnables import RunnableSequence

# llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAidgZgpXu9mvAPEMSGGeiRaAdWF05rd5s")

# prompt_template = PromptTemplate(
#     input_variables=["input"],
#     template="You are a tool caller, you have to call the tool named add_number_tool if case if there is any addition required, please don't send any explanation while calling the function, just send the two numbers what users provided e.g 5,2, even though user give the sentance you have to find two numbers and pass to the functions, user input is : {input}\n"
# )
# @tool
# def add_numbers_tools(input_data: str) -> str:
#     """addition of two numbers"""
#     print("add number Tool ", input_data)
    
#     try: 
#         print("function parameter",input_data)

#         numbers =input_data.split(",")

#         print("after split",numbers)

        

#     except Exception as e:
#         return "No number found"

#     num1 = int(numbers[0])

#     print("first number",num1)
    
#     num2 = int(numbers[1])
        
#     print("second number",num2)

#     result= num1+num2

#     print("result",result)

#     return f"The sum of {num1} and  {num2} is {result}"

#     #   #    or
#     #  #  result "The sum of", {num1}, "and", {num2}, "is", {result}

# chain = RunnableSequence(
#     prompt_template,
#     llm,
#     add_numbers_tools,
# )

# output = chain.invoke("visited Five places and five more places want to visite")
# print("output", output)
# ........................4...................................

# from langchain_google_genai import GoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain_core.tools import tool
# from langchain_core.runnables import RunnableSequence

# llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAidgZgpXu9mvAPEMSGGeiRaAdWF05rd5s")

# prompt_template = PromptTemplate(
#     input_variables=["input"],
#     template="You are a tool caller, you have to call the tool named add_number_tool if case if there is any addition required, please don't send any explanation while calling the function, just send the two numbers what users provided e.g 5,2, even though user give the sentance you have to find two numbers and pass to the functions, user input is : {input}\n"
# )
# @tool
# def add_numbers_tools(input_data: str) -> str:
#     """addition of two numbers"""
#     print("add number Tool ", input_data)
    
#     try: 
#         print("function parameter",input_data)

#         numbers =input_data.split(",")

#         print("after split",numbers)

        

#     except Exception as e:
#         return "No number found"

#     num1 = int(numbers[0])

#     print("first number",num1)
    
#     num2 = int(numbers[1])
        
#     print("second number",num2)

#     result= num1+num2

#     print("result",result)

#     return f"The sum of {num1} and  {num2} is {result}"

#     #   #    or
#     #  #  result "The sum of", {num1}, "and", {num2}, "is", {result}

# @tool
# def multiply_number_tool(input_data: str) -> str:
#     """ multiptication of two numbers """
#     print("multiply_Number_TOOL", input_data)
#     return "this is multiply of"

# chain = RunnableSequence(
#     prompt_template,
#     llm,
#     add_numbers_tools,
#     multiply_number_tool,
# )

# output = chain.invoke("vmy first number is 10 second number should be minust of first number by 2")
# print("output", output)

#  Hardcoded

#  # In chains, a sequence of actions is hardcoded (in code)

#  #  its no good Agent because I say do add but it do both add and multiply,  ,,,but i only say do add
#  # i give one template to it.

#  #   .....................5...................

#   #  In agents, a language model is used as a reasoning engine to determine which actions to take 
#    #   and in which order.
# from langchain_google_genai import GoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain_core.tools import tool
# from langchain_core.runnables import RunnableSequence

# llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAidgZgpXu9mvAPEMSGGeiRaAdWF05rd5s")

# prompt_template = PromptTemplate(
#     input_variables=["input"],
#     template="You are a tool caller, you have to call the tool named add_number_tool if case if there is any addition required, please don't send any explanation while calling the function, just send the two numbers what users provided e.g 5,2, even though user give the sentance you have to find two numbers and pass to the functions, user input is : {input}\n"
# )
# @tool
# def add_numbers_tools(input_data: str) -> str:
#     """addition of two numbers"""
#     print("add number Tool ", input_data)
    
#     try: 
#         print("function parameter",input_data)

#         numbers =input_data.split(",")

#         print("after split",numbers)

        

#     except Exception as e:
#         return "No number found"

#     num1 = int(numbers[0])

#     print("first number",num1)
    
#     num2 = int(numbers[1])
        
#     print("second number",num2)

#     result= num1+num2

#     print("result",result)

#     return f"The sum of {num1} and  {num2} is {result}"

#     #   #    or
#     #  #  result "The sum of", {num1}, "and", {num2}, "is", {result}

# @tool
# def multiply_number_tool(input_data: str) -> str:
#     """ multiptication of two numbers """
#     print("multiply_Number_TOOL", input_data)
#     return "this is multiply of"

# chain = RunnableSequence(
#     prompt_template,
#     llm,
#     add_numbers_tools,
#     multiply_number_tool,
# )

# output = chain.invoke("vmy first number is 10 second number should be minust of first number by 2")
# print("output", output)

#   ,,,,,,,,,,,,,,,,,,,,,,,6,,,,,........................

# from langchain.agents import initialize_agent, AgentType

# from langchain_google_genai import GoogleGenerativeAI

# from langchain_core.tools import tool


# llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAidgZgpXu9mvAPEMSGGeiRaAdWF05rd5s")


# @tool
# def add_numbers_tools(input_data: str) -> str:
#     """addition of two numbers"""
#     print("add number Tool ", input_data)
    
#     try: 
#         print("function parameter",input_data)

#         numbers =input_data.split(",")

#         print("after split",numbers)

        

#     except Exception as e:
#         return "No number found"

#     num1 = int(numbers[0])

#     print("first number",num1)
    
#     num2 = int(numbers[1])
        
#     print("second number",num2)

#     result= num1+num2

#     print("result",result)

#     return f"The sum of {num1} and  {num2} is {result}"

#     #   #    or
#     #  #  result "The sum of", {num1}, "and", {num2}, "is", {result}

# @tool
# def get_weather_tool(city: str) -> str:
#     """ check weather info from llm """
#     return f"the waether of {city} in 25C"


# agent = initialize_agent(
#     tools = [add_numbers_tools ,  get_weather_tool],
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     llm=llm,
#     verbose=True,
#     max_iterations=2,
# )

# agent.run("what is the weather of faisalabad")
# # # ...................7.....................

from langchain.agents import AgentExecutor
from langchain.agents import create_tool_calling_agent
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS   # FAISS = DATA base
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.tools.retriever import create_retriever_tool
from langchain_community.chat_message_histories import ChatMessageHistory #manage Chat Memory we make list and it few message save
from langchain_core.runnables.history import RunnableWithMessageHistory  
from langchain import hub
import os
from dotenv import load_dotenv

load_dotenv()

#Intialize the LLM with GoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

search = TavilySearchResults(tavily_api_key=os.getenv("TAVILY_API_KEY"))


 # this also a tool

loader =WebBaseLoader("https://www.techloset.com/")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
).split_documents(docs)

vector = FAISS.from_documents(documents, GoogleGenerativeAIEmbeddings(model="models/embedding-001"))

content = vector.as_retriever()

retriever_tool = create_retriever_tool(      # three things
    content, # retriver .....data collect
    "techloset_search",  #  name 
    "Search for any questions about Techloset Solutiojs, you must use this tool" #prompt  kab ya tool call ho sakta ha
)

tools = [search, retriever_tool]     # ya 2 tool hain is main

# we make agent crator and execut agant

prompt = hub.pull("hwchase17/openai-functions-agent")

agent = create_tool_calling_agent(
    llm,
    tools,
    prompt
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


message_history = ChatMessageHistory()

agent_with_chat_history = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: message_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

while True:
    agent_with_chat_history.invoke(
        {"input": input("How can I help you today? : ")},
        config={"configurable": {"session_id":"test123"}},
    )
