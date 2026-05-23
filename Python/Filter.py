# %% [markdown]
# Filter functions 

# %% [markdown]
# The filter() function is used to filter out element from a list based on a condition.

# %%
def event(num):
    if num % 2==0:
        return True

event(4)        


# %%
lst=[1,2,3,4,5,6,7,8]
list(filter(event,lst))

# %%
numbers=[1,2,3,8,9,5,6,7]
nums=list(filter(lambda x:x>5,numbers))
print(nums)

# %%
## with lambda and multiple conditions 

numbers=[9,8,7,6,2,3,1]
nums=list(filter(lambda x:x>5 and x%2==0,numbers))
print(nums)

# %%
## dictionary 
person=[
    {"name":"siddharth","age":25},
    {"name":"singh","age":15}
]
def age(person):
    return person["age"]>=25

list(filter(age,person))

# %%



