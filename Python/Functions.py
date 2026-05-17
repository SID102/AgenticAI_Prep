# %% [markdown]
# A function is a block of code that perform a specific task .

# %%
def function_name(parameter):
    ##body
    return

# %%
def iseven(num):
    """This function find even or odd"""
    if(num%2==0):
        print("even")
    else:
        print("odd")

# %%
## call the function 
iseven(24)

# %%
##deafult parameter 
def greet(name="sidd"):
    print(f"Hello :{name}")
greet()

# %%
##variable length arguement 
def function(*arr):
    for a in arr:
        print(a)
        

# %%
function(1,2,4,7,"aisbs")

# %%
## keywords arguments
def print_details(**arr):
    for key,value in arr.items():
        print(f"{key}:{value}")

# %%
print_details(name="siddharth",age=15)

# %%
## in python a function can return multiple values 
def multi(a,b):
    return a*b,a
print(multi(2,3))    

# %%



