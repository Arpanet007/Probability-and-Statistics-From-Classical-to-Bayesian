import numpy as np
import matplotlib.pyplot as plt
import math
import random

#Refer to the birthday paradox that was told in week1_examples, the paradox is that even in small groups, having common birthdays 
#has high probability even though there are 365 days.
#logic: size represents the size of the group, the occurence of having a common birthday in this group can be 
#treated as a bernoulli random variable(lets call it X_i) with p= Probability of having common birthdays.
#We generate n groups of the prescribed size and check if the event happens, if it happens we say X_i=1 and 0 o.w.
#By WLLN the average values of X_i's will converge on the expected value of X_i
# For bernoulli variables, E[X]= p, the quantity we are interested in.   
#Increasing n will give higher accuracy as usual, by chesbley's inequality
size=23
sum=0
n=5000
for itr in range(0,n):
    x=np.zeros(size)
    flag=0
    for i in range(0,len(x)):
        x[i]=random.randrange(1,366)
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if(x[i]==x[j]):
                flag=1
    sum+=flag
estimate= sum/n
#for size=23, p is actually equals 0.5073
#you can change size to check for different groups
print(estimate)