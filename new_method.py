import os
import random
import math


def main():
    f = open('RandomMatrix.txt', 'r')
    matrix = []
    wt=[]
    cnt=0
    a = map(int, f.readline().strip().split())
    while a:
        cnt=0
        matrix.append(a)
        for x in xrange(0,len(a)):
            if a[x]==1:
                cnt+=1
        wt.append(cnt)
        a = map(int, f.readline().strip().split())

    f.close()
    mi=0
    done=[0]*len(wt)
    prio=[0]*len(wt)
    for x in xrange(0,len(wt)):
        if wt[mi]>wt[x]: mi=x
    for x in xrange(0,len(wt)):
        mx=mi
        for y in xrange(0,len(wt)):
            if wt[mx]<wt[y] and done[y]==0:
                mx=wt[y]
                done[y]=1
        prio[x]=mx

    #print len(matrix)
    weights = []
    for x in xrange(0,len(matrix)):
        r = random.randint(0, 100)
        s = random.randint(0, 100)
        val={r,s}
        weights.append(val)
    print "min ",mi," max ",mx
    print prio
    print wt
    print done



if __name__=="__main__":
    main()