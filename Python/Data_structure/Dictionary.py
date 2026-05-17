# %% [markdown]
# Dictionaries

# %% [markdown]
# dictionaries are used to store data in key value pair , key is unique and immutable 

# %%
## creating an empty dictonary
empty_dictonary={}
print(type(empty_dictonary))

# %%
empty_dict=dict()
print(type(empty_dict))

# %%
student={"name":"sid","age":"25","state":"up"}
print(student)
print(type(student))

# %%
student={"name":"sid","age":"25","name":"up"}
print(student)

# %%
print(student["name"])
print(student.get("name"))
print(student.get("last_name","singh"))##deafult value 

# %%
##Dictionary are mutable 
print(student)
student["age"]=33
student["address"]="Nodia"
print(student)


# %%
del student["age"]## delete key and value pair 
print(student)

# %%
## DIctonary methods
keys=student.keys()## get all keys 
print(keys) 
values=student.values()## get all values 
print(values)

items=student.items()
print(items)


# %%
## shallow copy 
student_copy=student
print(student)
print(student_copy)

# %%
##update student 
student["address"]="kanpur"
print(student)
print(student_copy)

# %%
## shallow copy :- we dont want the changes that we have made in student will also reflect in stduent_copy 
student_copy=student.copy()
print(student)
print(student_copy)

# %%
student["address"]="delhi"

# %%
print(student)
print(student_copy)

# %%
##Iterating over dictionaries 
##use can use loop to iterate over dictonaries 
for keys in student.keys():
    print(keys)


# %%
for values in student.values():
        print(values)

# %%
for key,values in student.items():
    print(key)
    print(values)

# %%
##Nested dictonary 
students={
    "stduent1":{"name":"sid","age":"25"},
    "stduent2":{"name":"sid2","age":"24"}
}
print(students)

# %%
##Acess nested dictionary 
print(students["stduent1"]["name"])
print(students["stduent2"]["name"])

# %%
##iteratin gover dictionaries 
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key , value in student_info.items():
        print(f"{key}:{value}")

# %%
##Dictionary compehension 
squares={x:x**2 for x in range(5)}
print(squares)

# %%
evens={x:x**2 for x in range(10) if x%2==0}
print(evens)

# %%
### use a dictionary to count the freq of numbers in a list 
arr=[1,2,2,1,5,6,6,7,9,4]
freq={}
for number in arr:
    if number in freq:
        freq[number]+=1
    else:
        freq[number]=1    
print(freq)

# %%
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
merged_dict={**dict1,**dict2}
print(merged_dict)

# %%



