# %% [markdown]
# Loops

# %%
##for lop
for i in range(1,10):
    print(i)

# %%
##range 
for i in range(1,10,2):
    print(i)

# %%
##string
str="siddharth"
print(str)

# %%
##pass
##The pass statement is a null operation ; it does nothing 
for i in range(5):
    if i==3:
        pass
    print(i)

# %%
## F string , for printing 
for i in range(5):
    for j in range(3):
        print(f"i:{i} and j:{j}")

# %%
##String
str="siddharth"
for i in str:
    print(i)


