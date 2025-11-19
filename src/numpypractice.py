import numpy as np
import pandas as pd
def createArray():
    arr=np.array([45,85,94,65,48,99,458])
    print(arr)
    print(type(arr))
#createArray()

def inbuiltMethods():
    arr=np.array([45,98,45,85,62,789,456,25,15])
    print(arr)
    print('mean of array ',arr.mean())
    print('sum of an array ',arr.sum())
    print('standared deviatin of arr ',arr.std())
#inbuiltMethods()

def multidimArray():
    arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(arr)
    print('Martrix transpose \n',arr.T)
    print('shape of matrix ',arr.shape)
    print('dimension of matrix ',arr.ndim)
#multidimArray()

def dataframe():
    data={'Name':['sachin','rahul','rohit','virat'],
          'Age':[22,24,23,25],
          'Course':['python','java','c++','javascript']}
    df=pd.DataFrame(data)
    print(df)
    print('shape of dataframe ',df.shape)
    print('info of dataframe \n',df.info())
    print('describe of dataframe \n',df.describe())

dataframe()