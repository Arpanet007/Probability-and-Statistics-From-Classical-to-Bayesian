import numpy as np
import matplotlib.pyplot as plt
import math


#lets take I= (integral 0 ->1/4) sqrt(x -x^2), I will explain later the reasoning behind this.
step=100
error=np.zeros(100);
pi_estimate= np.zeros(100);
#generating estimates for different sample sizes
for j in range(0,100):
    n=(j+1)*(step)
    x=np.random.uniform(0,0.25,n)
    for i in range(0,len(x)):
        x[i]= (x[i]-x[i]*x[i])**(0.5)
    expected_x = x.sum()/n
    #note that the intgral of expectation will be equal to 4I, since limits are form 0 to 1/4 (check by yourself)
    estimate= expected_x/4

    #Newton was one of the leading figures in changing how we claculate pi, allowig us to reach higher accuracy
    # this is the integral he used in 1666 to calculate pi (soon after he "discovered" calculus)
    # pi= 3/4 * sqrt(3) + 24I (proved geometrically)

    pi_estimate[j]= 0.75*(3**(0.5)) + 24*estimate
    error[j]= 100*abs(pi_estimate[j]-math.pi)/(math.pi)

#plotting the values
plt.subplot(212)
plt.plot(range(step,101*step,step),error)
plt.ylabel("Error(in %)")
plt.xlabel("Size")
plt.ylim(0,2)
plt.grid()
#note that the error will not always decrease, but the probability of getting a high error decreases
plt.subplot(211)
plt.plot(range(step,101*step,step),pi_estimate)
plt.plot(range(step,101*step,step),np.ones(100)*math.pi)
plt.ylabel( "Estimated value")
plt.ylim(3,3.3)
plt.grid()
plt.show()
#notice how small the margin of error is, we can easily inc step to get more accuracy as well
print(error[99])