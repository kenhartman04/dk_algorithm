import numpy as np
import random as rnd
import networkx as nx
import matplotlib.pyplot as plt

class RandomNetwork():

    plt.close()

    def __init__(self, vertices, edges):
        self.ver = vertices
        self.edg = edges

    def __str__(self):
        return ('Random network with {} vertices and {} edges'.format(self.ver, self.edg))

    def createAdjMatrix(self):
        lines = np.ones(self.edg, int)
        adj_mat = np.zeros((self.ver, self.ver), int)
        for i in range(self.ver):
            while all(x == adj_mat[i][i] for x in adj_mat[i]):
                ran_j = rnd.randint(0, self.ver - 1)
                if i == ran_j:
                    pass
                else:
                    adj_mat[i][ran_j] = lines[0]
                    adj_mat[ran_j][i] = lines[0]
                    lines = np.delete(lines, 0)
        while len(lines) >= 1:
            ran_i = rnd.randint(0, self.ver - 1)
            ran_j = rnd.randint(0, self.ver - 1)
            if ran_i == ran_j or adj_mat[ran_i][ran_j] > 0:
                pass
            else:
                adj_mat[ran_i][ran_j] = lines[0]
                adj_mat[ran_j][ran_i] = lines[0]
                lines = np.delete(lines, 0)
        return adj_mat

    def genDist(self):
            dist = np.empty(self.edg, int)
            for i in range(self.edg):
                x = rnd.randint(2, 30)
                dist[i] = x
            return dist

    def assignDist(self, adj_mat):
        dist = RandomNetwork.genDist(self)
        for i in range(self.ver):
            j = 0
            while 1 in adj_mat[i]:
                if adj_mat[i][j] == 1:
                    adj_mat[i][j] = dist[0]
                    adj_mat[j][i] = dist[0]
                    dist = np.delete(dist, 0)
                    j += 1
                else:
                    j += 1
    def createLabels(self):
        labels = []
        for i in range(0, self.ver):
            label = ('V{a}'.format(a=i+1))
            labels.append(label)
        return labels

    def createAdjDict(self, adj_mat):
        adj_list = {}
        keys = RandomNetwork.createLabels(self)
        for i in range(self.ver):
            record = []
            for j in range(self.ver):
                if adj_mat[i][j] > 0:
                    x = (keys[j], adj_mat[i][j])
                    record.append(x)
            y = {keys[i]: record}
            adj_list.update(y)
        return adj_list

    def plotNetwork(self, adj_mat):
        labels = {}
        for i in range(0, self.ver):
            label = ('V{a}'.format(a=i+1))
            labels[i] = label
        g2 = nx.DiGraph(adj_mat)
        nx.draw(g2, labels=labels)
        plt.show()