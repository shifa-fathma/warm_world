#!/usr/bin/env python
# coding: utf-8

# In[1]:


#3
numbers = [int(x) for x in input("Enter a list of numbers : ").split(",")]
largest_number = max(numbers)


print(f"{largest_number} is the largest number.")


# In[2]:


#2

name = input("Enter the name: ")
roll_number = input("Enter the roll number: ")
mark = float(input("Enter the mark: "))

print(f"Name: {name}")
print(f"Roll No: {roll_number}")
print(f"Mark: {mark}")


# In[3]:


#4

for current_number in range(1, 11):
   
    if current_number == 1:
        previous_number = 0
    else:
        previous_number = current_number - 1
    

    current_sum = current_number + previous_number
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {current_sum}")


# In[6]:


#5
numbers = [10, 20, 33, 46, 55]
for number in numbers:
    if number % 5 == 0:
        print(f"{number} is divisible by 5.")
    else:
        print(f"{number} is not divisible by 5.")


# In[7]:


#6
num = int(input("Enter the number: "))


prime = True

if num < 2:
    prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break


if prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# In[8]:


# 9
num1 = float(input(" first number: "))
num2 = float(input(" second number: "))
num3 = float(input(" third number: "))


max_number = max(num1, num2, num3)


print(f"The maximum of {num1}, {num2}, and {num3} is {max_number}.")


# In[9]:


#exercise 2 


# In[10]:


#6
numbers = [int(x) for x in input("Enter a list of numbers : ").split(",")]


most_frequent_item = max(set(numbers), key=numbers.count)


print(f"The most frequent item in the list is: {most_frequent_item}")


# In[11]:


#7

numbers = [int(x) for x in input("Enter a list of numbers : ").split(",")]


sum_of_squares = sum(x**2 for x in numbers)


print(f"The sum of squares of the numbers in the list is: {sum_of_squares}")


# In[13]:


def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)


num1 = float(input(" first number: "))
num2 = float(input(" second number: "))
num3 = float(input(" third number: "))

result = find_maximum(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {result}")


# In[ ]:




