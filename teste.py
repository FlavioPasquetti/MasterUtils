
import pandas as pd
import matplotlib.pyplot as plt

df= pd.DataFrame(data = [[1,2,[1,2,3,4]], [2,4,[3,4,5,6]], [5,6,[5,6,7,8]], [7,8,[6,7,8,9]]], columns= ["X", "Y", "Z"]) 
print(df)


xValue = "X"
yValue = "Y"
zValue = "Z"


graph = plt.contour(df[xValue].values, df[yValue].values, list(df[zValue].values), colors= "k", linewidth= 1.5)
plt.clabel (graph, inline= True, fontsize= 15.0, inline_spacing = 10)\

plt.show()