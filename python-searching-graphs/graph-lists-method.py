
# coding: utf-8

# In[13]:

file = open("graphSmall1.in")
name = set()
edge = []
for i in file:
    i =i.strip('\n')
    i = i.split(" ")
    for line in i:
        edge.append(line)
        line = line.split('-')
        name.add(line[0])
        name.add(line[1])
        
Node = []
for i in name:
    Node.append(i)

Edge_adj = [[] for _ in range(len(Node))]
for i in range (0, len(Node)):
    num = 0
    for x in range (0, len(Node)):
        if str(Node[i])+"-"+str(Node[x]) in edge:
            num = num +1
            Edge_adj[i].append(Node[x])
 

#test--------------------------------------------------
print("Read",len(Node),"and",len(edge),"edges")
for i in range(0, len(Node)):
    print("Node:",i,"","Name:",Node[i])
    for x in Edge_adj[i]:
        x=Node.index(x)
        print("Edge:",x)


# In[ ]:



