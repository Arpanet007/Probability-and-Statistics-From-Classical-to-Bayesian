import numpy as np
import matplotlib.pyplot as plt
import math

#Change these values to see how the parameters affect the distribution
mu,sigma=0,1              
x= np.linspace(-50,50,num=1000)
#basically the pdf for normal distribution
y=((1/(2*math.pi))**(0.5))*(1/sigma)*np.exp((-1)*((x-mu)**2)/(2*sigma**2))   
k=max(y)

#mu is commonly knows as shift parameter, try guessing the reason by changing mu and plotting 
plt.plot(x,y)
plt.plot(mu*np.ones(50),np.linspace(0,k,50)) 
plt.grid()
plt.show()
#Use the zoom tool if the graph comes out concentrated in a small area