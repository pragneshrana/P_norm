import numpy as np 
import matplotlib.pyplot as plt
import math

#We are assuming norm value is 1 and try to visualize it 
norm_value = 1

#Intial values
start = -1
stop = 1
steps = 10000
p = 2
x1 = np.linspace(start,stop,steps)

def p_norm(x1,p):
    x2 = []
    negative_x2  = [] #as norm is 
    for i in range(len(x1)):
        temp_x2 =np.power(1-np.power(abs(x1[i]),p),1/p)
        x2.append(temp_x2)
        negative_x2.append(-temp_x2)

    x2 = x2 + negative_x2 #ADDING NEGATIVE VALUES IN THE END  
    x1 = np.append(x1,x1) #Settlement for plotting :)

    plt.scatter(x1,x2)

p_norm(x1,1)
p_norm(x1,2)
p_norm(x1,5)
p_norm(x1,50)
p_norm(x1,500)


plt.show()



     
