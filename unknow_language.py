"""
ordered list of words of an unknown language
{“baa”, “abcd”, “abca”, “cab”, “cad”}
Find the order of this alphabet (my answer was b d a c)
"""


def first_unequal_char(first, second):
    """
    :param first: str, no empty
    :param second: str, no empty
    :return: (char, char) or None
    assume first < second
    """
    for a, b in zip(first, second):
        if a < b:
            return a, b
    return None


def unknown_language(ordered_words):
    """
    :param ordered_words: [str]
    :return: str with the order of this alphabet
    assume no empty str
    """
    all_nodes = set("".join(ordered_words))
    ordered_pairs_graph = dict().fromkeys(all_nodes, [])
    for first, second in zip(ordered_words[:-1], ordered_words[1:]):
        t = first_unequal_char(first, second)
        if t:
            a, b = t[0], t[1]
            ordered_pairs_graph[a].append(b)
    # find the start node
    end_node = None
    for node in all_nodes:
        if len(ordered_pairs_graph[node]) == 0:
            end_node = node

    ans = []


if __name__ == '__main__':
    case1 = ["baa", "abcd", "abca", "cab", "cad"]
    assert unknown_language(case1) == "bdac"
