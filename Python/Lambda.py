# %% [markdown]
# Lambda Functions:
# 
# Lambda function are the anonymous function i.e a function without name .

# %%
## syntax 
lambda arguments : expression

# %%
def addition(a,b):
    return a+b

# %%
addition(2,3)

# %%
addition = lambda a,b:a+b
print(addition(5,6))

# %%
def even(num):
    if num%2==0:
        return True
even(12)        

# %%
even1=lambda num:num%2==0
even1(24)

# %%
def addition(x,y,z):
    return x+y+z
addition(2,4,7)

# %%
addition1=lambda x,y,z:x+y+z
addition1(2,4,5)

# %%
## map()
numbers=[1,2,3,4,5,6]
def square(num):
    return num*2
square(2)    

# %%
##map() - applies a function to all items in a list

list(map(lambda x:x**2,numbers))

# %%



