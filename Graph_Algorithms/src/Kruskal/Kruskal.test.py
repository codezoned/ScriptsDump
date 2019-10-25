from Kruskal import Kruskal

try:
    # Test1
    print("\t\t\t\t\t====Test1====")
    kruskal = Kruskal(4, [(1, 2, 3), (1, 3, 3), (1, 4, 4), (3, 4, 1)])
    mst, cost = kruskal.getMST()
    print("Minimum Spanning Tree: ", mst)
    print("Cost: ", cost)
    print("\n\n\n")

    # Test2
    print("\t\t\t\t\t====Test2====")
    kruskal = Kruskal(5, [(1, 2, 3), (1, 3, 3), (1, 4, 4), (3, 4, 1), (5, 3, 3)])
    mst, cost = kruskal.getMST()
    print("Minimum Spanning Tree: ", mst)
    print("Cost: ", cost)
    print("\n\n\n")

    # Test3
    print("\t\t\t\t\t====Test3====")
    kruskal = Kruskal(6, [(1, 2, 3), (1, 3, 3), (1, 4, 4), (3, 4, 1), (5, 3, 3), (6, 2, 4)])
    mst, cost = kruskal.getMST()
    print("Minimum Spanning Tree: ", mst)
    print("Cost: ", cost)
    print("\n\n\n")

    # Test4
    print("\t\t\t\t\t====Test4====")
    kruskal = Kruskal(7, [(1, 2, 3), (1, 3, 3), (1, 4, 4), (3, 4, 1), (5, 3, 3), (6, 2, 4)])
    mst, cost = kruskal.getMST()
    print("Minimum Spanning Tree: ", mst)
    print("Cost: ", cost)
    print("\n\n\n")

except Exception as e:
    print(str(e))