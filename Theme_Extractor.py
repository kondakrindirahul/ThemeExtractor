
# coding: utf-8

# In[1]:

import spacy
nlp = spacy.load('en')


# In[2]:

doc = nlp(input("enter a sentence "))

from spacy.symbols import nsubj, pobj, conj, nsubjpass

dependency_dict = {}

# for np in doc.noun_chunks:
#     print(np)
    
for each in doc:
    if each.dep == nsubj or each.dep == pobj or each.dep == conj or each.dep == nsubjpass:
        dependency_dict[each] = each.dep_
 
# print(dependency_dict)
# print(len(dependency_dict))

value_list = dependency_dict.values()
new_value_list = list(value_list)
# print(new_value_list)

first_dep = new_value_list[0]
# print(first_key)

key_list = dependency_dict.keys()
new_key_list = list(key_list)
# print(new_key_list)

subjects = []
objects = []
count = 0
d_l = len(dependency_dict)

if first_dep == 'nsubj' or first_dep == 'nsubjpass':

    for each in dependency_dict.keys():
        if dependency_dict[each] != 'pobj':
            subjects.append(each)
            count += 1
        else:
            break
    
    for i in range(count, d_l):
        objects.append(new_key_list[i])
        
if first_dep == 'pobj':
    
    for each in dependency_dict.keys():
        if dependency_dict[each] != 'nsubj' or dependency_dict[each] != 'nsubjpass':
            objects.append(each)
            count += 1
        else:
            break
    
    for i in range(count, d_l):
        subjects.append(new_key_list[i])
            
            
print("the subjects are ")        
print(subjects)
print("the objects are")
print(objects)   

