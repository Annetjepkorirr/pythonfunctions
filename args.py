def my_country(country="Rwanda"):
    print(f"Hello from {country}")

def greet(*names):
    for name in names:
        print(f"Hello {names}")    

def sum(*numbers):
    answer= 0
    for number in numbers:
        answer+=number  
    return answer   

#create a function that can output any number of  intergers and return the result of multiplu all of them      

def multiply(a,b):
    return a*b 

def multiply(*nums):
    answer = 1
    for num in nums:
        answer*=num
    return answer

def student_attribute(**kwargs):
    for key,value in kwargs.items():

        print(f"{key} : {value}")

# A function named concatenate_args that takes any number of string arguments 
# in positional arguments format and concatenates them into a single string
# def concatenate_args(*names):
def concatenate_args(*names):
    word=""
    for name in names:
        word+=name
    return word


# A function named concatenate_kwargs that takes any number of string arguments
#  in keyword arguments  format and concatenates them into a singles string
def concatenate_kwargs(**kwargs):
    content=""
    for key,value in kwargs.items():
        content+=value
    return content

        