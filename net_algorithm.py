

import randomNetworkGenerator as rn

n = int(input('\nHow many vertices do you want to have in your network ?\n'))  # number of vertices in the network

min_n = n - 1  # calculation of minimum possible edges
max_n = n * (n - 1) / 2  # calculation of maximum possible edges

m = int(input('How many edges do you want to have in your network ? \n'
              '(minimum number of edges is: {a})\n'
              '(maximum number of edges is: {b})\n'.format(a=min_n, b=max_n)))
while m < min_n or m > max_n:
    raise TypeError('Your input is incorrect, try again.\n')

net = rn.RandomNetwork(n, m)
print(net)
adj_matrix = net.createAdjMatrix()
net.assignDist(adj_matrix)
net.plotNetwork(adj_matrix)
adj_list = net.createAdjDict(adj_matrix)



"""
net_points = rn.NetworkElements(n, m, points, node_dict, adj_list)
net_points.printNetworkList()
#net_points.plotRandomNPoints()
net_points.plotNetwork(adj_matrix)

startPoint = input('Give the start point:\n')
endPoint = input('Give the end point:\n')
"""