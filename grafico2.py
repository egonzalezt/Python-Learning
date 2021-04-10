import matplotlib.pyplot as plt
import numpy as np

#X1 = [300,285,270,255,240,225,210,195]
#Y1 = [150,200,250,300,350,400,450,500]
X1 = [25000,0]
Y1 = [0,100]
plt.plot(X1, Y1, label = "Demanda") 

#X2 = [90,120,150,180,210,240,270,300]
#Y2 = [150,200,250,300,350,400,450,500]
'''
X2 = [27500,0]
Y2 = [0,110]

plt.plot(X2, Y2, label = "Demanda P=↑10% ") 


X3 = [17500,0]
Y3 = [0,70]

plt.plot(X3, Y3, label = "Demanda P=↓30% ") 
'''
plt.xlabel('Q') 
# Labeling the Y-axis 
plt.ylabel('P') 
# Give a title to the graph
plt.title('Precio frente a demanda') 


plt.scatter(3000, 88, label="P=↑10%",color="black")
plt.scatter(11000, 56, label="P=↓30%'",color="red")

# Show a legend on the plot 
plt.legend() 
 
plt.show()