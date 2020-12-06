

def main():
    f=open('NodeDetail.txt','r')
    nodes = eval(f.read())
    f.close()
    size=len(nodes)
    for i in xrange(1,size+1):
        print nodes[i]['edges'],nodes[i]['weight']
    f=open('GreedInd.xml','w')
    f.write("<instance>\n<presentation name=\"sampleProblem\" maxConstraintArity=\"6\"\nmaximize=\"true\" format=\"XCSP 2.1_FRODO\" />")
    f.write("\n\n")
    f.write('<agents nbAgents="%d">\n'%size)
    for i in xrange(1,size+1):
        f.write('<agent name="agentA%d" />\n'%i)
    f.write('</agents>\n<domains nbDomains="1">\n<domain name="two_colors" nbValues="2">1..2</domain>\n</domains>\n\n')
    f.write('<variables nbVariables="%d">\n' % size)
    for i in xrange(1,size+1):
        f.write('<variable name="A%d" domain="two_colors" agent="agentA%d" />\n'%(i,i))
    f.write('</variables>\n\n')
    f.write('<relations nbRelations="%d">\n<relation name="NEQ" arity="2" nbTuples="1" semantics="soft" defaultCost="0">\n-999: 2 2\n</relation>\n'%(size+1))
    for i in xrange(1,size+1):
        f.write('<relation name="R%d" arity="1" nbTuples="2" semantics="soft" defaultCost="0">\n%d:1|\n%d:2\n</relation>\n'%(i,nodes[i]['weight']/2,nodes[i]['weight']))
    f.write('</relations>\n\n')
    n=0
    for i in xrange(1,size+1):
        for j in xrange(len(nodes[i]['edges'])):
            n+=1
    f.write('<constraints nbConstraints="%d">\n'%(n+size))
    for i in xrange(1,size+1):
        l=len(nodes[i]['edges'])
        for j in xrange(l):
            f.write('<constraint name="A%d_and_A%d_have_different_colors" arity="2" scope="A%d A%d" reference="NEQ" />\n'%(i,nodes[i]['edges'][j],i,nodes[i]['edges'][j]))
    for i in xrange(1,size+1):
        f.write('<constraint name="A%d_prob" arity="1" scope="A%d" reference="R%d" />\n'%(i,i,i))
    f.write('</constraints>\n</instance>\n')
    f.close()

if __name__=="__main__":
    main()