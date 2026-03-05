#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = input("What's your name? ")
for i in range(1, 6):
    print(f"Day {i} of grinding, {name}. No excuses.")


# In[12]:


name = input("Enter name")
age = int(input("Enter age"))
print(f"{name} you will be {age + 1} years old in 2027")


# In[11]:


num = int(input("Enter a number"))
if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is zero")
else:
    print("Number is negitive")


# In[31]:


num = int(input("Enter a number for multiplication table"))
for i in range (1, 11):
    print(f"{num}*{i} is {num*i}")


# In[54]:


List = list()
for i in range(1,6):
    List.append(int(input(f"Enter marks of subject {i}: ")))
largest = max(List)
smallest = min(List)
average = sum(List)/len(List)

print(f"largest = {largest}")
print(f"smallest = {smallest}")
print(f"average = {average}")


# In[ ]:


Write a function called is_even(n) that returns True if n is even, False if odd.
Use it to print all even numbers from 1 to 50.


# In[86]:


def is_even(n):
   if n%2 == 0:
      return True
   else: return False   
for n in range(1, 51):
    if is_even(n):
        print(n)


# In[ ]:




