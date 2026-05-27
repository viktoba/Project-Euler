import numpy as np
import itertools as iter

#####Currently:   correct for N=20
#####           incorrect for N=100

def sieve(N):
    boolist = [False,False]+[True]*(N-2)
    sqrt_N = int(np.ceil(np.sqrt(N))+1)
    for i in range(2,sqrt_N):
        if boolist[i]:
            for j in range(i**2,N,i):
                boolist[j]=False
    return boolist

def boolist_to_primelist(boolist):
    primelist=[]
    for i in range(len(boolist)):
        if boolist[i]:
            primelist.append(i)
    return(primelist)

def primelist(N):
    s = sieve(N)
    p = boolist_to_primelist(s)
    return(p)


N=20
#N = 1000000
N= 1000

plist = primelist(N)
for p in plist:
    if p%4==3:
        plist.remove(p)

short_odd_plist = plist[1:]
print("short_odd_plist",short_odd_plist)
bracelet_nums = [1]+plist
for p in short_odd_plist:
    for i in range(1,int(np.ceil(np.log2(N+1)))):
        if 1<i and p**i<N:
            bracelet_nums.append(p**i)
        if 2*(p**i)<N:
            bracelet_nums.append(2*p**i)

print("bracelet_nums:", bracelet_nums)
sqplus1_nums= []

for n in range(N+1):
    m=n*n+1
    sqplus1_nums.append(m)

print("sqplus1_nums:", sqplus1_nums)
neighbor_pairs =[]

#matrix= np.zeros((len(bracelet_nums),len(bracelet_nums)))
matrix = [[0 for i in range(N)] for i in range(N)]
# for row in matrix:
#     print(row)



for i in bracelet_nums:
    for j in bracelet_nums:
        if i!=j and i*j in sqplus1_nums:
            #print(i,j, i*j)
            neighbor_pairs.append([i,j])
            matrix[i][j]=1
            # if i<j:
            #     matrix[i][j]=1
            # if i>j:
            #     matrix[i][j]=-1

print(neighbor_pairs)

def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("Vertex ", v, " already exists.")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []

    # Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2):
    global graph
    # Check if vertex v1 is a valid vertex
    # if v1 not in graph:
    #     print("Vertex ", v1, " does not exist.")
    # # Check if vertex v2 is a valid vertex
    # elif v2 not in graph:
    #     print("Vertex ", v2, " does not exist.")
    # else:
        # Since this code is not restricted to a directed or 
        # an undirected graph, an edge between v1 v2 does not
        # imply that an edge exists between v2 and v1
    #temp = v2
    graph[v1].append(v2)

    # Print the graph
def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex, " -> ", edges)

# driver code
graph = {}
# stores the number of vertices in the graph
vertices_no = 0
for n in bracelet_nums:
    add_vertex(n)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
for ed in neighbor_pairs:
    add_edge(ed[0],ed[1])
temp=[]
for v in graph:
    if graph[v]==[]:
        temp.append(v)
for v in temp:
    del(graph[v])
#print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)

def find_all_paths(graph, start, end, path=[], length=0):
    path = path + [start]
    length+=1
    #print(path, start,end)
    if start == end and length>3:
        print("path:",path)
        return [path]
    if start not in graph:
        return []
    paths = []
    for neighbor in graph[start]:
        # new_paths = find_all_paths(graph, neighbor, end, path, length)
        # for new_path in new_paths:
        #     paths.append(new_path)
        if neighbor not in path[1:]:
            new_paths = find_all_paths(graph, neighbor, end, path, length)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

#print("allpaths:", find_all_paths(graph,1,1))


def find_all_cycles(graph):
    cycles=[]
    for vertex in graph:
       cycles += find_all_paths(graph,vertex,vertex)
    return cycles

def unique_cycles(graph):
    cycles = find_all_cycles(graph)
    uni_cycles=cycles
    unis = []
    for cycle1 in cycles:
        uni_bool=True
        s1=cycle1[1:]
        s1list=[]
        for n in range(len(s1)):
            z1=s1[n:]+s1[:n]
            s1list.append(z1)
            if z1 in unis:
                uni_bool=False
        if uni_bool:
            unis.append(s1)
            print("uni:", s1)
    return unis


unis = unique_cycles(graph)
print("all unis:", unis)

sum=0
for cyc in unis:
    if 2 not in cyc and 1 not in cyc:
        print("not 2 not 1:", cyc)
    for n in cyc:
        # if n%4==3: ##never happens!
        #     print(cyc,n, "n is 3 mod 4")
        # if n%4==2:
        #     if n%8==6:
        #         print(cyc,n, "n is 6 mod 8")
            # if n%8==2:
            #     print(cyc,n, "n is 2 mod 8")
        sum+=n
    #print(cyc,sum)
print("totalsum",sum/2)

    



# for pair_i in neighbor_pairs:     #Finds len 3 paths
#     for pair_j in neighbor_pairs:
#         if pair_i[1]==pair_j[0]:
#             #print(pair_i,pair_j)
#             if [pair_i[0],pair_j[1]] in neighbor_pairs:
#                 print(pair_i+[pair_j[1]])



# print("m1")
# for row in matrix:
#     print(row)

# print("m2")
# m2=np.matmul(matrix,matrix)
# for row in m2:
#     print(row)
# for i in range(len(m2)):
#     m2[i][i]=0
# print("m2 without diag")
# for row in m2:
#     print(row)

# print("m3")
# m3=np.matmul(m2,matrix)
# for row in m3:
#     print(row)
# for i in range(len(m3)):
#     m3[i][i]=0

# print("m4")
# m4=np.matmul(m3,matrix)
# for row in m4:
#     print(row)
# for i in range(len(m3)):
#     m4[i][i]=0

# print("m5")
# m5=np.matmul(m4,matrix)
# for row in m5:
#     print(row)
# for i in range(len(m3)):
#     m5[i][i]=0
# print("m5 with 0 on diag")
# for row in m5:
#     print(row)
