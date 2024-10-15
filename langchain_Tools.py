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

#   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,........................

from langchain.agents import initialize_agent, AgentType

from langchain_google_genai import GoogleGenerativeAI

from langchain_core.tools import tool


llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAidgZgpXu9mvAPEMSGGeiRaAdWF05rd5s")


@tool
def add_numbers_tools(input_data: str) -> str:
    """addition of two numbers"""
    print("add number Tool ", input_data)
    
    try: 
        print("function parameter",input_data)

        numbers =input_data.split(",")

        print("after split",numbers)

        

    except Exception as e:
        return "No number found"

    num1 = int(numbers[0])

    print("first number",num1)
    
    num2 = int(numbers[1])
        
    print("second number",num2)

    result= num1+num2

    print("result",result)

    return f"The sum of {num1} and  {num2} is {result}"

    #   #    or
    #  #  result "The sum of", {num1}, "and", {num2}, "is", {result}

@tool
def get_weather_tool(city: str) -> str:
    """ check weather info from llm """
    return f"the waether of {city} in 25C"


agent = initialize_agent(
    tools = [add_numbers_tools ,  get_weather_tool],
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    llm=llm,
    verbose=True,
    max_iterations=2,
)

agent.run("what is the weather of faisalabad")
