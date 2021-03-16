# importing the modules we need at the top
import numpy as np
import matplotlib.pyplot as plt
import math
plt.figure(figsize=[12,12])  # size of graphs in units of inches

#Function to give h
def h (a, b, n):
    return (b-a)/(n) #taken directly from formula given in question description

#Function to give rectangular rule
def rectangular (f, a, b, n):
    total = 0 # initial value of total
    hr = h(a, b, n) # define the h variable, to make it easier to use more than once
    for i in range (0, n): #for each integer between 0 and n-1 (the number of slices)
        total = total + f(a + (i*hr)) #f(x1) + f(x2) + ... + f(xn-1)
    return total*hr # h[f(x1) + f(x2) + ... + f(xn-1)]

#Function to give trapeziodal rule
def trapezoidal(f, a, b, n):
    total = 0.5*f(a) + 0.5*f(b) #instead of multiplying only the middle values by 2 and dividing the whole thing by 2, multiply the limits by 0.5
    ht = h(a, b, n) # define the h variable, to make it easier to use more than once
    for i in range(1, n): #for each integer between 1 and n-1 (the number of slices)
        total = total + f(a + i*ht) # total + f(x1) + f(x2) + ... + f(xn-1)
    return total*ht # total multiplied by ht => h[0.5f(x1) + f(x2) + ... + 0.5f(xn)]

x = np.arange(2,101) #x axis for all of the graphs is for values of n between 2 and 100

#𝑓(𝑥)=𝑥 
def f(x):
    return x

result_t = [] #empty array for trapezium rule values for 𝑓(𝑥)=𝑥 
result_r = [] #empty array for rectangular rule values for 𝑓(𝑥)=𝑥 

for n in np.arange(2, 101):#array between n=2 to n=100 
    r = rectangular(f, 0, 1, n)
    result_r.append(r)

for n in np.arange(2, 101):#array between n=2 to n=100 
    t = trapezoidal(f, 0, 1, n)
    result_t.append(t)
     
yt = result_t #rename the variable to make it less confusing when I come to graph it - optional
yr = result_r #rename the variable to make it less confusing when I come to graph it - optional

plt.plot(x, yt)# Plots the line for trapezium rule values for 𝑓(𝑥)=𝑥 
plt.plot(x, yr)# Plots the line for rectangular rule values for 𝑓(𝑥)=𝑥 


#𝑓(𝑥)=𝑠𝑖𝑛𝑥 
def f1(x):
    return np.sin(x)

result_t1 = [] #empty array for trapezium rule values for 𝑓(𝑥)=sin𝑥 
result_r1 = [] #empty array for rectangular rule values for 𝑓(𝑥)=sin𝑥 

for n in np.arange(2, 101):#array between n=2 to n=100 
    t1 = trapezoidal(f1, 0, 1, n)
    result_t1.append(t1)

for n in np.arange(2, 101):#array between n=2 to n=100 
    r1 = rectangular(f1, 0, 1, n)
    result_r1.append(r1)

yt1 = result_t1 #rename the variable to make it less confusing when I come to graph it - optional
yr1 = result_r1 #rename the variable to make it less confusing when I come to graph it - optional

#𝑓(𝑥)=(𝑒^(−𝑥))𝑠𝑖𝑛𝑥 
def f2(x):
    return (math.exp(-x))*(np.sin(x))

result_t2 = [] #empty array for trapezium rule values for 𝑓(𝑥)=(𝑒^(−𝑥))𝑠𝑖𝑛𝑥 
result_r2 = [] #empty array for rectangular rule values for 𝑓(𝑥)=(𝑒^(−𝑥))𝑠𝑖𝑛𝑥 

for n in np.arange(2, 101):#array between n=2 to n=100 
    t2 = trapezoidal(f2, 0, 1, n)
    result_t2.append(t2)

for n in np.arange(2, 101):#array between n=2 to n=100 
    r2 = rectangular(f2, 0, 1, n)
    result_r2.append(r2)

yt2 = result_t2 #rename the variable to make it less confusing when I come to graph it - optional
yr2 = result_r2 #rename the variable to make it less confusing when I come to graph it - optional

# plot graph 1, add axis labels and a title
plt.subplot(2, 2, 1)
plt.plot(x, yt, label='Approximate integration using trapeziodal rule')# Create trapezium line
plt.plot(x, yr, label='Approximate integration using rectangular rule')# Create rectangular line
plt.title('Integration of f(x)=x')
plt.xlabel('Value of n')
plt.ylabel('Integrated value of f(x)=x')
plt.legend()

# plot graph 2, add axis labels and a title
plt.subplot(2, 2, 2)
plt.plot(x, yt1, label='Approximate integration using trapeziodal rule')# Create trapezium line
plt.plot(x, yr1, label='Approximate integration using rectangular rule')# Create rectangular line
plt.title('Integration of f(x)=sinx')
plt.xlabel('Value of n')
plt.ylabel('Integrated value of f(x)=sinx')

plt.legend()

# plot graph 3, add axis labels and a title
plt.subplot(2, 2, 3)
plt.plot(x, yt2, label='Approximate integration using trapeziodal rule')# Create trapezium line
plt.plot(x, yr2, label='Approximate integration using rectangular rule')# Create rectangular line
plt.title('Integration of f(x)=(e^(-x))sinx') 
plt.xlabel('Value of n')
plt.ylabel('Integrated value of f(x)=(e^(-x))sinx')
plt.legend()

plt.show # This actually draws the plot (and enables us to move on to drawing another one, if we wish)
