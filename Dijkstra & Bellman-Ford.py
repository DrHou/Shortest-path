#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:36:01 2018

@author: houzenghao
"""

import math
import pandas as pd 
import time


#ca = pd.read_excel('/Users/yantingshi/Desktop/ECI 257/test.xlsx')# read text file
ca = pd.read_excel('/Users/yantingshi/Desktop/ECI257/anaheim.xlsx')# read test network file
ca = ca.as_matrix() # convert to matrix

link = {}#create a dict and ready to save link information in this
performance =1
for i in ca: #create the hash with link informaiton
    if i[0] not in link:
        link[int(i[0])] ={} 
    link[int(i[0])][int(i[1])]=[i[2],i[3],i[4],i[5],i[6]]
#0. capacity 1. length 2. speed 3. freeflow Travel Time 4. free flow speed


    
t = time.time()# save the starting absolute time to t
 
def dijstra(network,start,end,performance):# define the funtion in case of duplicate operation
    output = []
    seen ={}# all nodes that have been visited
    ongoingnodes = {}# save all nodes haven't been visited
    ongoing={}# save all nodes haven't been visited with weight information
    for i in link.keys():# set infinite to all link in dict
        ongoing[i] = {i:float("inf")} #all processing path
        ongoingnodes[i] = float("inf")
    ongoing[start]={start:0}#set the starting point as 0
    ongoing[start],ongoingnodes[start] ={start:0},0#set the starting point as 0
    while True:
        root = min(ongoingnodes, key=ongoingnodes.get)#select the node with minimum weight
        ###print root
        seen[root] = ongoing[root] #save the processed node into seen dict with previous visited node information
        for i in network[root].keys():
            if i in ongoing.keys(): # search all the connected nodes 
                if network[root][i]: # if the following nodes are exits
                    #print network[root][i]
                    if network[root][i][performance]+ongoing[root][ongoing[root].keys()[0]]  < ongoing[i][ongoing[i].keys()[0]]: # and the distanct is shorter than other connection
                        ongoing[i]={root:network[root][i][performance]+ongoing[root][ongoing[root].keys()[0]]}# assign the following node to the current node in the dict
                        ongoingnodes[i]=network[root][i][performance]+ongoing[root][ongoing[root].keys()[0]]# assign the following node to the current node in the dict
                else:
                    break #ir there is no following nodes, means have visited all possibilities and shoudl break
        del ongoing[root] #remove visited node in ongoing dict
        del ongoingnodes[root] #remove visited node in ongoing dict
    
        if root == end:# if the curretn node is the ending node then break
            break
    output.append(seen[end][seen[end].keys()[0]]) 
    result = [end] # now, put the end node in result list first
    performance = 0 #set the weight as 0
    while seen[end][seen[end].keys()[0]]: #right now, the nodes are saved reversed in the dict
        result.append(seen[end].keys()[0]) # goes from the end to the start and append them into the result list
        #performance += seen[end][seen[end].keys()[0]] # accumulate the perfromances
        #print "cool",performance
        end = seen[end].keys()[0] #reasignt the previous node as current node
    result = list(reversed(result)) #reversed the make it in a from start to end sequence
    #print result
    #print performance
    #print time.time()-t
    output.append(result)
    return output

#results = dijstra(link,1,300,1)#apply function


#Label correcting algorithm


def labelcorrecting(link,start,end,perform):
    output =[]
    excute = {}
    for i in link.keys():# set infinite to all link in dict
        excute[i] = {i:float("inf")} #all processing path
    excute[start] = {start:0}    
    
    for i in xrange(len(link.keys())-1):
    #for i in xrange(1):
        ##print "out",i
        check = []
        for j in link.keys():
            for k in link[j].keys():
                #print "in",i
                if excute[k][excute[k].keys()[0]] > link[j][k][perform]+excute[j][excute[j].keys()[0]]:
                    excute[k] = {j:link[j][k][perform]+excute[j][excute[j].keys()[0]]}
                    check.append(j)
                    #print "in",i
                    #excute[k][k] = link[j][k][perform]
        ##print len(check)            
        if len(check) == 0:
            break
        
    ##print excute[end] 
    output.append(excute[end][excute[end].keys()[0]])
    resultc = [end] # now, put the end node in result list first
    while excute[end][excute[end].keys()[0]]: #right now, the nodes are saved reversed in the dict
        resultc.append(excute[end].keys()[0]) # goes from the end to the start and append them into the result list
        #performance += excute[end][excute[end].keys()[0]] # accumulate the perfromances
        #print "cool",performance
        end = excute[end].keys()[0] #reasignt the previous node as current node
        #print end
    resultc = list(reversed(resultc))
    output.append(resultc)
    
    #print output
    return output

test = [[1, 123], [1, 300], [2, 123],[2, 300]]
results = []
weight = 1
for i in test:
    start, end = i
    results.append(dijstra(link,start,end,weight))
    print dijstra(link,start,end,weight)
    results.append(labelcorrecting(link,start,end,weight))
    print labelcorrecting(link,start,end,weight)
#labelcorrecting(link,1,300,1)

weight = 3
for i in test:
    start, end = i
    results.append(dijstra(link,start,end,weight))
    print dijstra(link,start,end,weight)
    results.append(labelcorrecting(link,start,end,weight))
    print labelcorrecting(link,start,end,weight)
