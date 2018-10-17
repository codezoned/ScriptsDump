
from itertools import islice
import math
from collections import defaultdict


class LabeledPoint:

    def __init__(self, data, label="undefined"):
        self._data = data
        self._label = label

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return self._data.__iter__()

    def __str__(self):
        return "label: " + str(self._label) + ", data: " + str(self._data)

    @property
    def label(self):
        return self._label


"""
KNN is a very simple classifier, it classifies in a very intuitive way; show me your friends
and ill know who you are. it takes the K Nearest Neighbors to a point p and defines its label
as the most common label of said neighbors.
"""


class KNN:

    def __init__(self, K):
        self._K = K
        self._data = []

    # for KNN fitting is simply having the data
    def fit(self, data):
        if any([type(point) != LabeledPoint for point in data]):
            raise ValueError("All elements of data must be of type Point")
        self._data = data

    # euclidean distance of 2 points
    def euclidean_dist(self, p1, p2):
        if type(p1) != LabeledPoint or type(p2) != LabeledPoint:
            raise ValueError("p1 and p2 must be Point objects")
        return math.sqrt(sum([(x[0] - x[1]) ** 2 for x in zip(p1, p2)]))

    # given a point p, return its label based on the data at hand.
    def classify(self, p):
        if type(p) != LabeledPoint:
            raise ValueError("p must be a Point object")

        classes = defaultdict(int)
        for point in islice(sorted(self._data, key=lambda p2: self.euclidean_dist(p, p2), reverse=True), 0, self._K):
            classes[point.label] += 1
        return max(classes, key=classes.get)


