import pandas as pd
import matplotlib.pyplot as plt

#With Using Plot
df = pd.read_csv("cars.csv")

df1=pd.DataFrame(df)
#selecting That coloum in CSV
x=df['Car']
#Seleceting Weight column in the CSV File
y=df['Weight']
plt.xlabel('x - axis Cars')
# naming the y axis
plt.ylabel('y - axis Weight')
# giving a title to my graph
plt.title('Cars graph!')
plt.plot(x,y)
plt.show()

#Using Bar

df = pd.read_csv("cars.csv")
plt.style.use('ggplot')
df1=pd.DataFrame(df)
#selecting That coloum in CSV
x=df['Car']
#Seleceting Weight column in the CSV File
y=df['MPG']
plt.xlabel('x - axis Cars')
# naming the y axis
plt.ylabel('y - axis MPG')
# giving a title to my graph
plt.legend()
plt.title('Cars graph!')
plt.bar(x,y,color='green')
plt.show()


#Using  scatter


df = pd.read_csv("cars.csv")
plt.style.use('ggplot')
df1=pd.DataFrame(df)
#selecting That coloum in CSV
x=df['Car']
#Seleceting Horsepower column in the CSV File
y=df['Horsepower']
plt.xlabel('x - axis Cars')
# naming the y axis
plt.ylabel('y - axis Horsepower')
# giving a title to my graph
plt.legend()
plt.title('Cars graph!')
plt.scatter(x,y,color = '#88c999')
plt.show()

#using Histogram


df = pd.read_csv("cars.csv")

plt.style.use('ggplot')

df1=pd.DataFrame(df)
y=df['Acceleration']

plt.hist(y)

plt.show()