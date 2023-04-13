
class Dijkstra():

    def __init__(self, adj_list, start, end):
        self.adj_list = adj_list
        self.start = start
        self.end = end

    def __str__(self):
        return ('Finding the cloesest path from {} to {}'.format(self.start, self.end))

    def initialization(self):
        state_mat = []
        for i in range(self.adj_list):
            if self.start == list(self.adj_list.keys())[i]:
                state_mat.append(list(self.adj_list.items())[i])

