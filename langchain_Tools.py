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
        #         /............................................................/.....

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
# ...................................................................................
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_core.runnables import RunnableSequence

llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key="AIzaSyAidgZgpXu9mvAPEMSGGeiRaAdWF05rd5s")

prompt_template = PromptTemplate(
    input_variables=["input"],
    template="You are a tool caller, you have to call the tool named add_number_tool if case if there is any addition required, please don't send any explanation while calling the function, just send the two numbers what users provided e.g 5,2, even though user give the sentance you have to find two numbers and pass to the functions, user input is : {input}\n"
)
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

chain = RunnableSequence(
    prompt_template,
    llm,
    add_numbers_tools,
)

output = chain.invoke("visited Five places and five more places want to visite")
print("output", output)