# from math import *

f = open('NodeDetail.txt', 'r')
nodes = eval(f.read())
f.close()
print "Node = ",
print nodes
sum_tot=0
for i in xrange(1,len(nodes)+1):
    sum_tot+=nodes[i]['weight']

f = open('temp1.txt', 'w')
f.write(str(nodes))
f.close()

deleted_nodes = []
neigh_deleted_nodes = []
done = False
operation_count = 1
#sum_tot=0
sum_del_node=0
while not done:
    print 'operation count', operation_count
    operation_count += 1
    nodes = eval(open('temp1.txt', 'r').read())
    node_ids = nodes.keys()
    for node_id in node_ids:
        #sum_tot+=node_id['weight']
        nodes = eval(open('temp1.txt', 'r').read())
        print 'before operation for node', node_id
        node = nodes[node_id]  # present node
        connected_nodes = node['edges']  # present node neighbour
        weight = node['weight']  # present node wt
        #sum_tot+=weight
        maxw = 0
        for nid in connected_nodes:  # get max wt of neighbours
            n = nodes[nid]
            w = n['weight']
            if w > maxw:
                maxw = w
                maxn = nid
        temp_nodes = nodes  # alias for nodes
        if weight > maxw or weight == maxw:
            # if present node wt greater than max wt of neighbour ,,include it and delete all its neighbour
            node = nodes[node_id]  # present node
            weight1 = node['weight']  # present node wt
            sum_del_node+=weight1
            deleted_nodes.append(node_id)
            for nnid in nodes[node_id]['edges']:
                if nnid not in neigh_deleted_nodes:
                    neigh_deleted_nodes.append(nnid)
            del temp_nodes[node_id]
        print ''
        print '--------------------------'
        print 'deleted nodes', deleted_nodes
        print 'deleted neighbour nodes', neigh_deleted_nodes
        print '--------------------------------------------------------------'
        print ''
    for deleted_node_ids in deleted_nodes:  # delete present included node from all entry of our network
        if deleted_node_ids in nodes.keys():
            del nodes[deleted_node_ids]
            for node_id in nodes.keys():
                if deleted_node_ids in nodes[node_id]['edges']:
                    ind = nodes[node_id]['edges'].index(deleted_node_ids)
                    del nodes[node_id]['edges'][ind]
    for deleted_node_ids in neigh_deleted_nodes:
        # delete neighbour node of present included node from all entry of our network
        if deleted_node_ids in nodes.keys():
            del nodes[deleted_node_ids]
            for node_id in nodes.keys():
                if deleted_node_ids in nodes[node_id]['edges']:
                    ind = nodes[node_id]['edges'].index(deleted_node_ids)
                    del nodes[node_id]['edges'][ind]

    f = open('temp1.txt', 'w')
    f.write(str(nodes))
    f.close()

    nodes_distinct = True  # do till all node traversed
    for node_id in nodes.keys():
        if not len(nodes[node_id]['edges']) == 0:
            nodes_distinct = False
            break

    if len(nodes.keys()) == 0 or nodes_distinct:
        done = True
#sum_del_node = 0
for node_id in nodes.keys():
    # left out node due to values inclusion ,,to get maximum weighted independent set of all nodes
    node = nodes[node_id]  # present node
    weight = node['weight']  # present node wt
    sum_del_node+=weight
    deleted_nodes.append(node_id)
print 'nodes that transmit at a time:', deleted_nodes
f=open('hop_nodes.txt','w')
for i in xrange(len(deleted_nodes)):
    f.write(str(deleted_nodes[i])+" ")
f.close()
f=open('output.txt','w+')
f.write("Greedy Algorithm Results ->\n\nNo of active nodes = "+ str(len(deleted_nodes)))
f.write("\nTotal Resources in the network = "+ str(sum_tot))
f.write("\nTotal resources on active nodes = "+ str(sum_del_node))
f.write("\nTotal unused resources  = "+str(sum_tot-sum_del_node))
f.close()
print 'Greedy Hopping :-> operation ended...\n'
