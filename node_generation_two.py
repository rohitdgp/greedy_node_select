import os
import random
import math


def main():
    n = input("Enter the max weight of the nodes = ")
    f = open('RandomMatrix.txt', 'r')
    matrix = []
    a = map(int, f.readline().strip().split())
    while a:
        matrix.append(a)
        a = map(int, f.readline().strip().split())
    f.close()
    f = open('NodeDetail.txt', 'w')
    
    mat2=[]
    
    for i in xrange(len(matrix)):
        temp=[]
        for j in xrange(len(matrix)):
            if matrix[i][j] == 1:
                temp.append(j+1)
        mat2.append(temp)
        
    mat_final=[]
    #make a matrix with two hops
    for i in xrange(len(matrix)):
        temp=mat2[i]
        for j in xrange(len(mat2[i])):
            val=mat2[i][j]
            temp=list(set(temp) | set(mat2[val-1]))
            
    #remove values with the same value as the node
        if (i+1) in temp:
            temp.remove(i+1)
        mat_final.append(temp)
        
    
  
    f.write('{\n')
    
    
    for i in xrange(len(matrix)):
        f.write(str(i + 1) + ": {'edges': [")
        node = ""
        for j in xrange(len(mat_final[i])):
            node = node + str(mat_final[i][j]) + ","
        node = node[:len(node) - 1]
        
        f.write(node)
        f.write("],")
        
        weight = random.randint(1, n - 1)
        
        f.write(" 'weight': " + str(weight) + "},")
        f.write("\n")
    f.write("}")
    f.close()
  
if __name__ == "__main__":
    main()
