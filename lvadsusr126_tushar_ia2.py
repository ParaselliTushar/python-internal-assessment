# -*- coding: utf-8 -*-
"""LVADSUSR126-Tushar-IA2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tYa2FRJrwW_4aU8kj-jnXO6CxzZX0rzQ
"""

import numpy as np
import pandas as pd

#1
rgb_image=np.array([[[255,0,0],[0,255,0],[0,0,255]],
                    [[255,255,0],[0,255,0],[0,0,255]],
                    [[127,127,127],[200,200,200],[50,50,50]]])
con=np.array([0.2989,0.5870,0.1140])
grey_scale_image=rgb_image*con
print(grey_scale_image)

#2
c=np.array([[[[25.4,34.6,31.9],[29.4,13.7,34.7],[38.3,47.6,53.7]]]])
m=np.mean(c)
sd=np.std(c)
print(m)
print(sd)

#3
#p=np.ones((3,1))
c=np.array([[[[25.4,34.6,31.9],[29.4,13.7,34.7],[38.3,47.6,53.7]]]])
print(" Data collected from sensor: \n\n", c)
x=c.flatten()
print("\n flatten data:\n\n",x)
r=x.reshape(3,3)
print("\n Restructred data:\n\n",r)

#4
p=np.ones((2,2))
c=np.array([['Athelete-1',34.6,31.9],['Athelete-2',30.7,34.7],['Athelete-3',47.6,53.7]])
r=c[:,1]
m=c[:,2]
n=np.subtract(m,r)
#n=np.array([[-2.7],[4],[6.1]])
f=np.concatenate((c,n),axis=1)
print(f)

#5
data=np.array([['Student-1',34.6,31.9,-1],['Student-2',30.7,-1,84.7],['Student-3',47.6,53.7,78]])
data
a=data[0,:]
b=data[1:]
c=data[2,:]
avg1=np.average(a)
avg2=np.average(a)
avg3=np.average(a)
avg=np.array([[avg1],[avg2],[avg3]])
print(avg)

#7
a=[['Name','Age','Department'],
['Alice',30,'HR'],
['Bob',35,'Finance'],
['David',40,'HR'],
['Frank',50,'Finance'],
['Grace',55,'HR']]
df=pd.DataFrame(a[1:],columns=a[0])
df3=df[df['Age']> 45]
print(df3['Name'])

#8
l=[['Product','Category','Price','Promotion'],
   ['Apples','Fruit',1.20,True],['Bananas','Fruit',0.50,False],['Cherries','Fruit',3.0,True],['Dates','Fruit',2.50,True],
   ['ElderBerries','Fruit',4.00,False],['Flour','Bakery',1.50,True],['Grapes','Fruit',2.00,False]]

df=pd.DataFrame(l[1:],columns=l[0])
df1=df.groupby('Category')['Price'].mean()
a=df1['Fruit']
df1=df['Promotion']==False
df2=df[df1]
df3=df2['Price']>a
df2[df3]

#9
a=[['Name','Age','Department'],
['Alice',30,'HR'],
['Bob',35,'Finance'],
['Alice',40,'HR'],
['Charlie',50,'Finance'],
['David',55,'HR']]
df=pd.DataFrame(a[1:],columns=a[0])
df3=df
print(df3)

#10
data={'Department':['Electronics','Electronics','Clothing','Clothing','Home','Goods'],
      'Salesperson':['Alice','Bob','Charlie','David','Eve',np.NaN],
      'Sales':[70000,50000,30000,40000,60000,np.NaN]
      }
df=pd.DataFrame(data)
df2=df.groupby('Department').agg({'Sales':'mean'})
df2
df2.sort_values(by='Sales',ascending=False)