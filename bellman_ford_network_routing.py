# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:23:27 2021

@author: schoud21
"""
import pandas as pd

path=''

def partial_iteration(V, dist, vertices):
    print("Source\t Destination\t Cost")
    for i in range(V):
        print('{0}\t\t {1}\t\t\t\t {2}'.format('u', vertices[i], dist[i]))

def printPath(parent, vertex, vertices):
    '''Iteratively determine the shortest path traversed from the source node to any
    destination node'''
    global path
    if vertex < 0:
        return
    printPath(parent, parent[vertex], vertices)
    path +=vertices[vertex]
    
def bellman_ford(input_data):
    '''An implementation of the Bellman-Ford algorithm in network routing
    The function here calculates:
        1. The routing table generated in each step of the algorithm.
        2. The Final routing table.
        3. The matrix denoting the number of hops to reach a node and the corresponding
           shortest path traversed.
    '''
    global path
    start_node=input_data.loc[input_data['source node = starting node'] == 'Y', 'source'].iloc[0]
    print("\n\nThe starting node for out graph is: {0}".format(start_node))
    vertices=list(set(list(input_data['source'].unique())+list(input_data['destination'].unique())))
    vertices=sorted(vertices)

    V=len(vertices)

    E=len(input_data.index)

    print("\n\nThe number of vertices: {0}".format(V))
    print("The number of edges: {0}".format(E))
    
    #Step 1: Initialize the graph
    dist=[float('inf')]*V
    dist[0]=0

    # Initial routing table
    print("\nThe initial routing table")
    partial_iteration(V, dist, vertices)
    
    #Convert the Input data in into a list of lists with values
    graph=input_data[['source','destination','weight']].values.tolist()
    graph_indexed=[]
    for i in graph:
        graph_indexed.append([vertices.index(i[0]),vertices.index(i[1]),i[2]])
    print(graph_indexed)
    parent=[-1]*V
    
    #Step 2: Relax the Edges repeatedly
    for i in range(V - 1):
        for j in range(E):
            if dist[graph_indexed[j][0]] + graph_indexed[j][2] < dist[graph_indexed[j][1]]:
                dist[graph_indexed[j][1]] = dist[graph_indexed[j][0]] + graph_indexed[j][2]
                parent[graph_indexed[j][1]]=graph_indexed[j][0]
                #print(parent)
        print("\n\nRouting table after {0}th iteration".format(i+1))
        partial_iteration(V, dist, vertices)
        
    print("\n\nFinal Routing table:")
    partial_iteration(V, dist, vertices)
    #print(parent)
    
    #Step 3: Check for Negative-Weight Cycles
    for (u,v,w) in graph_indexed:
        if dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return
        
    #Print the number of hops and the path taken to reach a destination node while 
    #traversing along the shortest path between them
    print("\n\nThe shortest path from source to destination is:")
    print("Source\t Destination\t number of hops\t Path")
    directed_path=''
    number_of_hops=0
    for i in range(V):
        #print("Source\t Destination\t number of hops\t Path")
        printPath(parent, i, vertices)
        for j in path:
            if j==path[0]:
                directed_path=j
            else:
                directed_path+=' -> '+j
        number_of_hops=len(path)-1
        print("{0}\t\t {1}\t\t\t\t {2}\t\t\t\t [ {3} ]".format(vertices[0], vertices[i], number_of_hops, directed_path))
        path=''
        directed_path=''

    
if __name__ == '__main__':
    #Take the input from csv file denoting the source, destination, weight and if the 
    #source node is the starting node in out process
    input_data=pd.read_csv("input_edges_vertices.csv")
    print('The input for the interconnections between the nodes is:')
    print(input_data)
    #Run the Bellman-Ford algorithm on the user input
    bellman_ford(input_data)
