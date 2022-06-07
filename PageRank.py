import numpy as np #importing the numpy library
from scipy.linalg import eig # importing the scipy library for eigen functions
nodes=int(input("Number of nodes:")) # enterring the number of nodes
connecs=int(input("Number of connections:")) # enterring the number of connections or edges
arr=np.zeros((nodes, nodes))
arr1=np.zeros((nodes, nodes))
for j in range(connecs): # forming the probability distribution matrix
    a,b=map(int,input().split(','))
    arr[a-1][b-1]=1
for i in range(nodes):
    cc=0
    for j in range(nodes):
        if (arr[i][j]==1):
            cc=cc+1
    for j in range(nodes):
        if (arr[i][j]==1):
            arr[i][j]=1/cc
arr1=arr
print(f"\nProbability transition matrix without random teleportations:\n{arr1}")
w1,vl1=eig(np.array(arr1), left=True,right=False) # finding the left eigenvector of arr1
sum1=0
rnk1=[]
for x in w1:
    if x == 1:
        rnk1=vl1[:,sum1]
    sum1=sum1+1
print("\nRank before normalisation:",rnk1)
sum1=0 
rnk2=[]
for i in range(len(rnk1)): #Loop to normalise the rank
    sum1=sum1+rnk1[i]
for i in range(len(rnk1)):
    rnk2.append(rnk1[i]/sum1)
print(f"\nPrincipal Left eigenvector of probability transition matrix without random teleportations:\n{rnk2}")
df=0.1 # random page with probability is df and probability to go through a link is 1-df. Note that df is given already as 0.1
arr=arr*(1-df)
arr=arr+(df/nodes)
print(f"\nProbability transition matrix with random teleportations:\n{arr}")
w, vl = eig(np.array(arr), left=True,right=False) #finding the left eigen vector
sum = 0
rnk = []
mev=0
mevindex=0
for x in w:
    if x>mev:
        mev=x
        mevindex=sum
    sum =sum+ 1
rnk=vl[:, mevindex]
sum = 0
print("\nRank before normalisation:",rnk)
for i in range(len(rnk)): # Loop to normalize the rank
    sum =sum+ rnk[i]
rnk3=[]
#eigen value method
for i in range(len(rnk)):
    rnk3.append(rnk[i] / sum)
print(f"\nNormalized Principal Left eigenvector of probability transition matrix with random teleportations:\n{rnk3}")


# power method
print(f"\nPower method for probability transition matrix with random teleportations:")
l1 = [1/nodes]*nodes
def rec(l3):
    l2 = np.dot(l3, arr)
    dist = np.sum((l3 - l2) ** 2)
    if dist > 0.001:
        dist = rec(l2)
    return l2, dist 
x=rec(l1)
print(x) 