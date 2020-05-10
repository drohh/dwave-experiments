import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt


G=nx.DiGraph()

G.add_edges_from([
                (0,1),(0,2),(0,3),(0,4),

                (1,5),(2,6),(3,7),(4,8),

                (5,9),(5,10),(5,11),(6,12),(6,13),(6,14),(7,15),(7,16),(7,17),(8,18),(8,19),(8,20),

                (9,21),(10,22),(11,23),(12,24),(13,25),(14,26),(15,27),(16,28),(17,29),(18,30),(19,31),(20,32),

                (21,33),(21,34),(21,35),(22,36),(22,37),(22,38),(23,39),(23,40),(23,41),(24,42),(24,43),(24,44),(25,45),(25,46),(25,47),(26,48),(26,49),(26,50),(27,51),(27,52),(27,53),
                (28,54),(28,55),(28,56),(29,57),(29,58),(29,59),(30,60),(30,61),(30,62),(31,63),(31,64),(31,65),(32,66),(32,67),(32,68)
                ])

#nx.draw_kamada_kawai(G,with_labels=True)
#nx.draw_kamada_kawai(G)
#plt.show()
n = G.number_of_nodes()
plabels = [x for x in range(1,n)]
print(plabels)
f = {node:False for node in plabels}
f[0] = 0
print(f)
#for v,l in f.items():
#    if (l is False):
#        print(v,"->",list(G.predecessors(v)))
#exit()

def Search(k):
    #iterations += 1
    if k == 0:
        return True
    #if iterations > threshold:
    #    return False
    for v,l in f.items():
        if (l is False): # if current vertex is not labeled
            parent = list(G.predecessors(v))[0]
            parent_label = f[parent]
            if parent_label is not False: # if its parent is labeled
                if parent_label+k in plabels: # if f(v`)+k is available
                    f[v] = parent_label+k
                    plabels.remove(parent_label+k)
                    if Search(k-1):
                        return True
                    plabels.append(parent_label+k)
                    f[v] = False
                if parent_label-k in plabels:
                    f[v] = parent_label-k
                    plabels.remove(parent_label-k)
                    if Search(k-1):
                        return True
                    plabels.append(parent_label-k)
                    f[v] = False
    return False

print(Search(n-1))
print(f)
