t = ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super")

# def method_3(string_):
#     string_to_return = ''
#     sting_len = len(string_)-1
#     dec = 0
#     for i in string_:
#         string_to_return += string_[sting_len-dec]
#         print(string_to_return)
#         dec += 1
#     return string_to_return

def check_connection(graph, fr_a, fr_b):
    nodes = get_unique_names(graph)
    print(nodes)


def get_unique_names(graph):
    node_names = set()
    for i in graph:
        node_names.add(i[:i.find('-')])
        node_names.add(i[i.find('-') + 1:])
    return node_names


class Graph:
    def __init__(self):
        self.verticies = {}

    def dfs(self, vertex):
        vertex.color = 'red'

        for node in vertex.neighbors:
            if node.color == 'black':
                self.dfs(node)

        vertex.color = 'blue'

    def find_neighbors(self, vertex):
        friend_a = self.verticies.get(vertex[:vertex.find('-')])
        friend_b = self.verticies.get(vertex[vertex.find('-') + 1:])
        friend_a.add_neighbors(friend_a, friend_b)


class Vertex():
    def __init__(self, name):
        self.name = name
        self.color = 'black'

        self.neighbors = list()

    def add_neighbors(self, u, v):
        if u not in v.neighbors and v not in u.neighbors:
            u.neighbors.add(v)
            v.neighbors.add(u)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3") == True, "Scout Brotherhood"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "super", "scout2") == True, "Super Scout"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "dr101", "sscout") == False, "I don't know any scouts."

    check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
                     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
                     "scout2", "scout3")
