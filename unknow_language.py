"""
ordered list of words of an unknown language
{“baa”, “abcd”, “abca”, “cab”, “cad”}
baa < abcd  => b<a
abcd < abca => d<a
...   ->  a<c
... -> b<d


Find the order of this alphabet (my answer was b d a c)
"""
from collections import defaultdict


def first_unequal_char(first, second):
    """
    :param first: str, no empty
    :param second: str, no empty
    :return: (char, char) or None
    assume first < second
    """
    for a, b in zip(first, second):
        if a != b:
            return a, b
    return None


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A recursive function used by topologicalSort

    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

                # Push current vertex to stack which stores result
        stack.insert(0, v)

        # The function to do Topological Sort. It uses recursive

    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        return stack


def unknown_language(ordered_words):
    """
    :param ordered_words: [str]
    :return: str with the order of this alphabet
    assume no empty str
    """
    vocabulary = list(set("".join(ordered_words)))
    ordered_pairs_graph = Graph(len(vocabulary))
    for first, second in zip(ordered_words[:-1], ordered_words[1:]):
        t = first_unequal_char(first, second)
        if t:
            a, b = t[0], t[1]
            ordered_pairs_graph.addEdge(vocabulary.index(a),
                                        vocabulary.index(b))
    return [vocabulary[t] for t in ordered_pairs_graph.topologicalSort()]


if __name__ == '__main__':
    case1 = ["baa", "abcd", "abca", "cab", "cad"]
    print(unknown_language(case1))
