#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import copy
import time
#Sudoku grids will be taken to be 9*9 numpy arrays with 0's for any unknown value.

def Fill(S,I):
    #A funciton that takes a 9*9 numpy array S and a vector I and in coordinate order fills the 0's in S
    #with the elements of I until I is exhausted.
    #It returns a grid with I filled in and the row and collumn value that was last filled in.
    n=0
    B=copy.deepcopy(S)
    for i in range(9):
        for j in range(9):
            if n<len(I):
                
                if S[i,j]==0:
                    
                    B[i,j]=I[n]
                    n=n+1
                    a=i
                    b=j
                    
            
    return [B,a,b]


# In[2]:


def Check(A,I):
    #This function takes a grid and an attempt vector I and checks if the latest value of I contradicts the rules of sudoku.
    S=Fill(A,I)[0]
    a=Fill(A,I)[1]
    b=Fill(A,I)[2]
    B=True
    
    Nums=[1,2,3,4,5,6,7,8,9]
    
    row=list(S[a,:])
    collumn=list(S[:,b])
    
    alpha=int(np.floor(a/3))
    beta=int(np.floor(b/3))
    square=[S[3*alpha,3*beta],S[3*alpha,3*beta+1],S[3*alpha,3*beta+2],S[3*alpha+1,3*beta],S[3*alpha+1,3*beta+1],S[3*alpha+1,3*beta+2],S[3*alpha+2,3*beta],S[3*alpha+2,3*beta+1],S[3*alpha+2,3*beta+2]]

    for x in Nums:
        if row.count(x)>1:
            B=False
 
        if collumn.count(x)>1:
            B=False
           
        if square.count(x)>1:
            B=False
         
            
    
      
    
    return B


# In[3]:


def Solver(S):
    B=copy.deepcopy(S)
    n=(B==0).sum()
    #Solves a sudoku by creating a vector with 1, if it works it guesses the next value. if it doesn't,
    #it tries all values for that slot until one works, if that doesn't work it moves down one spot and repeats.
    I=[1]
    while len(I)<n:
        if Check(S,I)==True:
            I.append(1)
        else:
            if I[-1]!=9:
                I[-1]=I[-1]+1
            else:
                j=-1

                while I[j]==9:
                    j=j-1
                J=I[0:j+1]

                J[len(J)-1]+=1
                I=J

    if len(I)==n:
        while  Check(S,I) is False:
            I[n-1]=I[n-1]+1
            
    B=Fill(B,I)[0]
        
    return B


# In[4]:


#4 sudokus.
A1=np.array([[3,2,0,6,0,9,0,8,0],[0,0,0,0,8,0,1,0,0],[0,8,5,0,0,4,0,9,2],[0,0,8,4,0,7,0,1,0],[2,0,1,0,0,5,0,0,0],[5,0,0,1,0,6,9,7,0],[4,0,0,0,0,8,0,6,3],[6,0,9,0,0,0,0,2,0],[0,0,7,0,6,1,0,5,9]])
A2=np.array([[0,7,0,5,0,0,2,3,0],[0,8,0,0,9,0,5,0,0],[5,0,0,0,0,7,0,6,4],[2,0,0,0,3,0,0,0,5],[0,0,0,9,4,8,0,0,0],[4,0,0,0,7,0,0,0,3],[7,2,0,4,0,0,0,0,1],[0,0,1,0,5,0,0,8,0],[0,5,6,0,0,3,0,7,0]])
A3=A=np.array([[0,1,3,0,0,7,0,0,2],[0,0,0,0,3,0,0,0,8],[0,4,0,0,0,2,0,0,0],[0,0,9,2,0,1,0,7,5],[0,0,0,0,0,0,0,0,0],[7,8,0,4,0,9,6,0,0],[0,0,0,9,0,0,0,6,0],[8,0,0,0,6,0,0,0,0],[1,0,0,7,0,0,3,9,0]])
A4=A=np.array([[0,0,3,0,0,0,4,5,0],[9,0,0,0,0,0,0,0,0],[7,2,0,6,0,0,0,0,9],[5,0,0,0,8,4,0,0,2],[0,0,0,1,0,2,0,0,0],[4,0,0,3,6,0,0,0,8],[8,0,0,0,0,6,0,3,7],[0,0,0,0,0,0,0,0,4],[0,7,4,0,0,0,2,0,0]])


# In[5]:


t1=time.perf_counter()
Solver(A1)
t2=time.perf_counter()
Dt1=t2-t1

t1=time.perf_counter()
Solver(A2)
t2=time.perf_counter()
Dt2=t2-t1

t1=time.perf_counter()
Solver(A3)
t2=time.perf_counter()
Dt3=t2-t1

t1=time.perf_counter()
Solver(A4)
t2=time.perf_counter()
Dt4=t2-t1
#the time for solution of those 4 sudokus.
print(Dt1,Dt2,Dt3,Dt4)


# In[ ]:




