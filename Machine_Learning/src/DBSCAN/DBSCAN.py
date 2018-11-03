

# the label is only used for the clustering algorithm
class LabeledPoint:

    def __init__(self, data):
        self._data = data
        self._label = "undefined"

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        return "label: " + str(self._label) + ", data: " + str(self._data)

    def __hash__(self):
        return hash(tuple(self._data))

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, val):
        self._label = val


"""
Density Based Spatial Clustering of Applications with Noise (DBSCAN).
the parameters for this clustering method are different from your usual clustering methods as it doesnt require
the number of clusters as input but rather: epsilon, the maximal distance between a core and the points in its cluster
and min_pts, the minimal number of points required for the group to be considered a cluster.
read up online to further understand these parameters.
The algorithm requires a way to measure distance between any two points and the metric used for distance
is left for the user to decide. note that dist_func(point1, point2) <= eps must return either true or false for any
2 points.
"""


class DBSCAN:

    def __init__(self, eps, min_pts, dist_func):
        self._eps = eps
        self._min_pts = min_pts
        self._dist_func = dist_func

    # this will change the label of each point to be the cluster it is a part of
    def fit(self, data):
        if any([not isinstance(point, LabeledPoint) for point in data]):
            raise ValueError("data must be a list of LabeledPoint")
        cluster_label = 1
        for point in data:
            if point.label != "undefined":
                continue
            neighbors = set([point2 for point2 in data if self._dist_func(point, point2) <= self._eps])
            if len(neighbors) < self._min_pts:
                point.label = "outlier"
                continue
            point.label = str(cluster_label)
            neighbors.remove(point)
            prev_size = 0
            new_size = len(neighbors)
            while prev_size < new_size:
                prev_size = len(neighbors)
                for neighbor in neighbors:
                    if neighbor.label == "outlier" or neighbor.label == "undefined":
                        neighbor.label = str(cluster_label)
                    else:
                        continue
                    connected_components = set([c_c for c_c in data if self._dist_func(neighbor, c_c) <= self._eps])
                    if len(connected_components) >= self._min_pts:
                        neighbors = neighbors.union(connected_components)
                new_size = len(neighbors)
            cluster_label += 1
