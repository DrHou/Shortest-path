#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:11:47 2018

@author: houzenghao
"""

#ca = pd.read_excel('/Users/yantingshi/Desktop/ECI 257/test.xlsx')# read text file
ca = pd.read_excel('/Users/yantingshi/Desktop/ECI 257/anaheim.xlsx')# read test network file
ca = ca.as_matrix() # convert to matrix

link = {}#create a heap and ready to save link information in this
performance =1
for i in ca: #create the heap with link informaiton
    if i[0] not in link:
        link[int(i[0])] ={} 
    link[int(i[0])][int(i[1])]=[i[2],i[3],i[4],i[5],i[6]]
    
vertices={}    
for i in link.keys():
    vertices[i] = {}
    for j  in link.keys():
        vertices[i][j]= float("inf")

        
nextt={}    
for i in link.keys():
    nextt[i] = {}
    for j  in link.keys():
        nextt[i][j]= j                   
perform = 1

for i in link.keys():
    for j in link[i].keys():
        vertices[i][j] = link[i][j][perform]
        
for k in link.keys():
    for i in link.keys():
        for j in link.keys():
            if vertices[i][j] > vertices[i][k] + vertices[k][j]:
                vertices[i][j] = vertices[i][k] + vertices[k][j]
                nextt[i][j] = nextt[i][k]

vertices[2][300]

start =2
end=300

#if nextt[start][end] == None:
#    break

path = [start]
while start != end:
    start = nextt[start][end]
    path.append(start)
#path reconstruction

     