# %% [markdown]
# Sets

# %%
##create a set 
my_set={1,2,3,4}
print(my_set)
print(type(my_set))

# %%
my_empty_set = set()
print(my_empty_set)

# %% [markdown]
# Basic set operations 

# %%
my_set=set([0,1,2,3,4])
print(my_set)

# %%
my_set.add(5)
print(my_set)

# %%
my_set.remove(0)
print(my_set)

# %%
## if element is not present then not throw error
my_set.discard(3)
print(my_set) 

# %%
##POP METHOD
removed_element=my_set.pop()
print(removed_element)
print(my_set)

# %%
##clear all element 
my_set.clear()
print(my_set)

# %%
## set membership test
my_set={1,2,3,4,5}
print( 3 in my_set)
print(6 in my_set)


# %%
##Mathematical operations 
set1={1,2,3,4}
set2={3,4,5,6,7}
union_set=set1.union(set2)
print(union_set)

##intersection -- > create new set 
intersection_set=set1.intersection(set2)
print(intersection_set)

##intersection update -> update the set1 with the intersection
set1.intersection_update(set2)
print(set1)

# %%
## difference 
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.difference(set2))

# %%
## SYmetric difference 
print(set1.symmetric_difference(set2))


# %%
## sets method 
set1={1,2,3}
set2={3,4,5}
print(set1.issubset(set2))
print(set1.issuperset(set2))

# %%
##unique words in a text 
test="my name is siddharth singh"
words=test.split()
set3=set(words)
print(set3)

# %%



