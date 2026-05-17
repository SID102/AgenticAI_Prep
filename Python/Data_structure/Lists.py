# %% [markdown]
# List data structure 
# List are ordered mutable collection of items 
# They can contain items of different data types.

# %%
arr=[]
print(type(arr))

# %%
arr=[1,2,3,"sidd","o"]
print(arr)
print(type(arr))

# %%
##Acessing list items 
arr=["apple","banana","cherry","kiwi"]
print(arr[0])
print(arr[-1])
print(arr[-2])

# %%
print(arr[1:])
print(arr[2:3])
print(arr[-1])

# %%
##Modifying the list element
arr[1]="sidd"
print(arr)

# %%
arr[1:]="sid"
print(arr)

# %%
## LIst method
fruits=["apple","banana","cherry","oranges"]
fruits.append("sid")## add an item to the end 
print(fruits)
fruits.insert(1,"singh")
print(fruits)


# %%
##remove
fruits=["apple","banana","cherry","oranges"]
fruits.remove("cherry")
print(fruits)
##remove and return last element
fruits_pop=fruits.pop()
print(fruits_pop)
print(fruits)
##index
indx=fruits.index("banana")
print(indx)
##count
count=fruits.count("apple")
print(count)

# %%
fruits.sort()
print(fruits)

# %%
fruits.reverse()
print(fruits)

# %%
fruits.clear()
print(fruits)

# %%
##slicing list
number=[1,2,3,4,5,6,7,8,9,10]
print(number[2:5])
print(number[:5])
print(number[5:])
print(number[::2])
print(number[::-1])

# %%
print(number[::2])

# %%
##iterating over list
number=[1,2,3,4]
for num in number:
    print(num)

# %%
##to iterate with index also 
number=[1,2,3,4]
for i,num in enumerate(number):
    print(i,num)

# %%
list=[]
for i in range(10):
    list.append(i*i)
print(list)

# %%
[i*i for i in range(10)]

# %% [markdown]
# #### List Comprehension 
# Basic syntax: [expression for item in iterable ]
# 
# with conditional logic [expression of item in iterable if condition]
# 
# Nested list comprehension [expression for item1 in iterable1 for item2 in iterable2 ]
# 

# %%
### condition list comprehension
even_number=[i for i in range(10) if i%2==0]
print(even_number)

# %%
##Nested List COmprehension 
list1=[1,2,3,4]
list2=['a','b','c','d']
pair=[[i,j] for i in list1 for j in list2]
print(pair)

# %%
##list comprehension with function 
arr=["sid","si","sjj"]
lst=[len(s) for s in arr]
print(lst)

# %%
### f string : used to format the string 
## print(f"{task}")

# %%



