import pandas as pd
import numpy as np
df = pd.read_csv('test.csv')
def trysqrt(num):
    try:
        return np.sqrt(num)
    except:
        return num
def ssplit(str):
    try:
        s = str.split()
        try:
            return s[0]+" "+s[1]
        except:
            return s[0]
    except:
        return str
def tapply(df,func):
    def try_func(a):
        try:
            return func(a)
        except:
            return a
    return df.apply(try_func)
def reflect(df,exp):
    return(df[(df.eval(exp))])
def eq(a,b):
    return a == b
def neq(a,b):
    return a != b
def gt(a,b):
    return a > b
def gte(a,b):
    return a >= b
def lt(a,b):
    return a < b
def lte(a,b):
    return a <= b
#df=df[df.columns[::-1]]
df['Alert']=df['Alert'].str.strip()
print(df)
df['Alert']=df['Alert'].apply(ssplit)
print(reflect(df,'Total > 20'))
print(df[(df['Total'] > 20)])
df2 = df.groupby('Alert').mean()
print(df2)
print(tapply(df,np.sqrt))
