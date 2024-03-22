# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 04:04:24 2024

@author: USER
"""
h=open('Downloads\hw2_data.txt','r')
data2={}

for i in h.read().splitlines():  #readlines()會有\n，還會把coke\n和coke認成不同詞
    
    if (i not in data2):
        data2[i]=1
       
    else:
        data2[i]+=1

print('詞彙數:',len(data2))   
print(data2)
h.close()
