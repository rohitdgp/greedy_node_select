import random


def sum_all(a, n):
    for i in xrange(n):
        if a[i] == 0:
            return True
    return False


def make_mat(n):
    matrix = []
    for i in xrange(0, n):
        temp = []
        for j in xrange(0, n):
            temp.append(0)
        matrix.append(temp)
        del temp
    return matrix


def main():
    #print "Enter the number of nodes = "
    #n = input()
    #print "Enter the degree = "
    #deg = input()
    f=open('input_file.txt','r')
    n=int(f.readline())
    deg=int(f.readline())
    f.close()
    lst = []
    sum_row = [0] * n
    # print sum_row[n-1]
    for i in xrange(n):
        lst.append(i)
    # Matrix to store the node info.
    matrix = make_mat(n)
    while sum_all(sum_row, n):
        r = random.randint(0, len(lst) - 1)
        s = random.randint(0, len(lst) - 1)
        while s == r:
            s = random.randint(0, len(lst) - 1)
        matrix[lst[r]][lst[s]] = 1
        matrix[lst[s]][lst[r]] = 1
        # increase the row/column sum by 1.
        sum_row[lst[r]] += 1
        sum_row[lst[s]] += 1
        # print lst[r],lst[s]
        # check if row/column is full.
        popped = 0
        if sum_row[lst[r]] == deg:
            # Row is popped if full
            # print "popped",lst[r]
            lst.pop(r)
            popped = 1

        # print sum_row
        if popped == 1:
            if r < s:
                if sum_row[lst[s - 1]] == deg:
                    # Column is popped if full.
                    lst.pop(s - 1)
            elif sum_row[lst[s]] == deg:
                lst.pop(s)
                # print "2nd"
        elif sum_row[lst[s]] == deg:
            lst.pop(s)
            # print "2nd"
            # print sum_row
    print "Matrix written to file.\n"
    # print "OPENING......"
    f = open('RandomMatrix.txt', 'w')
    # for i in xrange(n+1):
    #    f.write(str(i)+" ")
    # f.write("\n")
    for i in xrange(n):
        # f.write(str(i+1)+" ")
        for j in xrange(n):
            f.write(str(matrix[i][j]) + " ")
        f.write('\n')
    f.close()
    # print "File Opened.!!"
    # os.system('RandomMatrix.txt')
    # print "File Closed.!!"


if __name__ == "__main__":
    main()
