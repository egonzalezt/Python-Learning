import matplotlib.pyplot as plt
import numpy as np

#X1 = [300,285,270,255,240,225,210,195]
#Y1 = [150,200,250,300,350,400,450,500]
#X1 = [115,110,105,100,95,90,85,80,75,70,65]
#Y1 = [0,100,185,200,215,229,241,249,263,278,293]

X1 = [115,110,105,100,95,90,85,80,75,70,65]
Y1 = [0,11000,19425,20000,20425,20610,20485,19920,19725,19460,19045]
nombres = ['A','B','C','D','E','F','G','H','I','J','K']
plt.plot(X1, Y1, label = "") 

fig,ax = plt.subplots(figsize=(10,10))
ax.scatter(X1, Y1)

plt.xlabel('Q') 
# Labeling the Y-axis 
plt.ylabel('P') 
# Give a title to the graph
plt.title('Oferta vs Demanda') 
for i in range(10):
    ax.annotate(nombres[i], (X1[i], Y1[i]), xytext=(10,10), textcoords='offset points')
   

# Show a legend on the plot 
plt.legend() 
 
plt.show()
