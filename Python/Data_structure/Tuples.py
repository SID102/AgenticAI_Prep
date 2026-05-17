# %% [markdown]
# Tuples

# %% [markdown]
# Tuples are ordered collections of items that are immutables. They are similar to lists , but their immutable makes them different

# %%
##creating tuple 
empty_tuple=()
print(type(empty_tuple))

# %%
lst=list()
print(type(lst))
tuplee=tuple()
print(type(tuplee))

# %%
numbers=tuple([1,2,3,4,5])

# %%

numbers

# %%
mixed_tuple=(1,"sid",62)
print(mixed_tuple)

# %%
## Acessing tuple element 

print(numbers[2])
print(numbers[-1])

# %%
print(numbers[0:4])

# %%
print(numbers[::])

# %%
print(numbers[::-1])

# %%
print(numbers + mixed_tuple)

# %%
print(mixed_tuple*3)

# %%
##Imutable nautre of tuples
lst=[1,2,3,4,5]
print(lst)
lst[1]="sid"
print(lst)

# %%
numbers[1]

# %%
numbers[1]="sid"

# %%
## tuples methods 
print(numbers)
print(numbers.count(1))
print(numbers.index(3))## first occurence of 3

# %%
##packing and unpakcing tuples 
packed=1,2,"sid"
print(packed)

# %%
##unpacked 
a,b,c=packed 
print(a)
print(b)
print(c)

# %%
##unpacking with *
numbers=(1,2,3,4,5)
first,*second,third=numbers
print(first)
print(second)
print(third)

# %%
##Nested tuples
nested_tuples=((1,2,3),(4,5,6),("s","j","u"))
print(nested_tuples[0][2])

# %%
## Iterating over tuples
for i in nested_tuples:
    for j in i:
        print(f"{i}:{j}")

# %%



