import os
import random
import math


def main():
    f=open('input_file2.txt','r')
    n=int(f.readline())
    f.close()
    #n = input("Enter the max weight of the nodes = ")
    f = open('RandomMatrix.txt', 'r')
    matrix = []
    a = map(int, f.readline().strip().split())
    while a:
        matrix.append(a)
        a = map(int, f.readline().strip().split())
    f.close()
    f = open('NodeDetail.txt', 'w')
    f.write('{\n')
    pos = int(math.sqrt(len(matrix)))
    # print pos
    pos1 = 0
    pos2 = 0
    for i in xrange(len(matrix)):
        f.write(str(i + 1) + ": {'edges': [")
        node = ""
        for j in xrange(len(matrix)):
            if matrix[i][j] == 1:
                node = node + str(j + 1) + ","
        node = node[:len(node) - 1]
        # print node
        f.write(node)
        f.write("],")
        #f.write("'node_point': (")
        weight = random.randint(1, n - 1)
        #f.write(str(pos1) + ", " + str(pos2) + "),")
        f.write(" 'weight': " + str(weight) + "},")
        pos2 += 1
        if pos2 >= pos:
            pos2 = 0
            pos1 += 1
        f.write("\n")
    f.write("}")
    f.close()
    #os.system("NodeDetail.txt")


if __name__ == "__main__":
    main()
