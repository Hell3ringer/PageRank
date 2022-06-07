import networkx as nx
import numpy as np

web_graph=nx.read_gpickle("web_graph.gpickle") #Read graph object in Python pickle format.
print(web_graph)

query = input('Enter your query:') #Reading all the queries
query = query.split() #To separate all the words in the queries

ar = np.zeros(100)

for i in range(0,100) :
    docu = web_graph.nodes[i]['page_content'] #getting the content of the individual nodes
    terms=docu.split() #getting the individual words in the document
    for q in query:
        if (q in terms):
            ar[i]=1
            break
ar=np.array(ar)

adjar=nx.to_numpy_array(web_graph) #creating an adjacency matrix for ar
hub=np.dot(ar,adjar) #Getting Hub score
authority=np.dot(ar,adjar.T) #Getting authority score

#Finding which all pages will be a part of the sub-graph for the query given
ar=ar+hub+authority
baseset=[] #creating the baseset

for i in range (0,100):
    if(ar[i]!=0):
        baseset.append(i) #adding i to a vector arr5

sgrph=nx.subgraph(web_graph, baseset) #creating a subgraph using baseset
result=nx.to_numpy_array(sgrph)

l = len(baseset) # Starting with each node having a hub score and authority score of 1
avec=np.ones(l)
avec=np.ones(l)

iteration=1000 # Setting no. of iterations as 1000 randomly
count=0 # Step counter
while(count<=1000):
    count=count+1
    avec=np.dot(result.T,avec) #Running the authority update rule
    avec=np.dot(result,avec) # Running the hub update rule
    avec=avec/sum(avec) #Normalising
    avec=avec/sum(avec)

result=list(sgrph.nodes)
print("\nNode\tHub Values:")
t=0
for value in avec:
    print(result[t],end="\t")
    print(value,end="\n")
    t=t+1

print("\nNode\tAuthority Values:")
t=0
for value in avec:
    print(result[t],end="\t")
    print(value,end="\n")
    t=t+1