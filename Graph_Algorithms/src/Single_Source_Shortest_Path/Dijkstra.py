
def dijkstra(graph, s, v):
    ##priority is set first so that pop is easy 
    ##min/max by default is based on the first element of tuple when we have a list of tuples
    pq_dist = [(float("Inf"), i) for i in range(v)]
    ##set source pq= 0
    pq_dist[s] =  (0, s)
    v = len(graph)
    
    ##create ix and dist list
    done_dist = []
    done_ix = []
    for vertex in range(v):
        ###deque frpm pq
        dq_ele = pq_dist.pop(pq_dist.index(min(pq_dist)))
        dq_ix = dq_ele[1]
        
        ##add to done
        done_dist.append(dq_ele[0])
        done_ix.append(dq_ele[1])

        
        #get the neighbours pf rem ele not in done
        neighbours = [i for i in range(len(graph[dq_ix])) if graph[dq_ix][i] != 0 and 
                    i not in done_ix]
        
        ##update dist of neigh in pq
        #add neigh to pq
        if len(neighbours) > 0:
            ##iternate through all un-finalized neighbours
            for n in neighbours:
                if len(pq_dist) > 1:
                    ##we can use zip
                    ix_of_n_in_pq = list(list(zip(*tuple(pq_dist)))[1]).index(n)
                else:
                    ##we cannot use zip so default 0
                    ix_of_n_in_pq = 0
                ##if old priority > new_priority, update
                if len(pq_dist) > 0 and pq_dist[ix_of_n_in_pq][0] > dq_ele[0] + graph[dq_ix][n]:
                    pq_dist[ix_of_n_in_pq] = (dq_ele[0] + graph[dq_ix][n], n)
        else:
            ##no new neighbours found
            break
    ##get the index that will sort the vertices
    ##rectified the input as range(len(done_ix))
    sorted_ix = sorted(range(len(done_ix)), key=lambda k: done_ix[k])
    
    ##ouput dist in the order of vertices
    output = [done_dist[d] for d in sorted_ix]#list(list(zip(*tuple(done_list)))[1])
    print (" ".join([str(e) for e in output]), end = "")

if __name__ == '__main__':
    
    adjacency_matrix  = [[0,1,43],[1,0,6],[43,6,0]]

    # this function will print shortest path of source to all the vertices.
    src = 2
    number_of_vertices = 3
    dijkstra(adjacency_matrix,src, number_of_vertices)
