def main():
    f=open('file.txt','r')
    d=dict()
    while True:
        line=f.readline()
        if not line: break
        if 'var' in line[0:5]:
            l=int(line[6:len(line)-6])
            d[l]=line[len(line)-2]
            print l,d[l],line
    f.close()
    f=open('hop_nodes.txt','r')
    hops=map(int,f.read().strip().split())
    f.close()

    cnt=0
    for i in xrange(1,len(d)+1):
        if d[i]=='2':
            cnt+=1
    print "No of Active nodes = ",cnt
    #print d
    f=open('graph_color.dot','w')
    f.write('graph {\n')
    for i in xrange(1,len(d)+1):
        f.write('\tsubgraph cluster_agentA%d {\n\t\tlabel = A%d;\n\t\tA%d [style = "filled" fontcolor = black '%(i,i,i))
        if d[i]=='2':
            if i in hops:
                f.write('fillcolor = orangered shape = doubleoctagon];\n\t}\n')
            else: f.write('fillcolor = green1 shape = doublecircle];\n\t}\n')
        else:
            if i in hops:
                f.write('fillcolor = dodgerblue shape = doublebox];\n\t}\n')
            else: f.write('fillcolor = grey83 shape = circle];\n\t}\n')
    f2 = open('NodeDetail.txt', 'r')
    nodes = eval(f2.read())
    f2.close()
    f.write('\n\n')
    for i in xrange(1,len(nodes)+1):
        for j in xrange(len(nodes[i]['edges'])):
            if nodes[i]['edges'][j]>i:
                f.write('\tA%d -- A%d;\n'%(i,nodes[i]['edges'][j]))
    f.write('}')
    f.close()
    f=open('NodeDetail.txt','r')
    nodes = eval(f.read())
    f.close()
    active_wt=0
    tot_wt=0
    print len(nodes)
    for i in xrange(1,len(nodes)+1):
        node=nodes[i]
        if d[i]=='2':
            active_wt+=node['weight']
        tot_wt+=node['weight']
    f=open('output.txt','a+')
    f.write("\n\n\nMax-Sum Algorithm Output ->\n\nTotal no of Active nodes - "+str(cnt)+"\nTotal resources at all the nodes = "+str(tot_wt))
    f.write("\nTotal resources on active nodes = "+str(active_wt))
    f.write("\nTotal unused resources = "+str(tot_wt-active_wt))
    f.close()

if __name__=="__main__":
    main()