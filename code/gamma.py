
import numpy as np
import matplotlib.pyplot as plt
import math

#Change these values to see how the parameters affect the distribution
alpha,beta=5,0.1              
x= np.linspace(0.001,30,num=1000)
#basically the pdf for gamma distribution
y=(beta**alpha)*(x**(alpha-1))*(np.exp(-beta*x))/math.gamma(alpha)

#alpha is known as the shape parameter, use values <1 and >=1 to see why
plt.plot(x,y)
plt.grid()
plt.show()
#Use the zoom tool if the graph comes out concentrated in a small area
#The weibull distribution has almost the same graph and behaves similarly with the shape parameter
