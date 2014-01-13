#!/usr/bin/python2
# #####################################################################
# id_0107.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################
import networkx as nx

class Network:
    def __init__(self, ss):
        # read the network from the string ss
        self.mtx = []
        self.max = 0
        for s in ss.split("\n"):
            if s:
                self.mtx.append([])
                for ii in s.split(","):
                    if ii != "-":
                        self.mtx[-1].append(int(ii))
                        self.max = max(self.max, int(ii))
                    else:
                        self.mtx[-1].append(0)
        self.n = len(self.mtx)
        self.pprint()

    def bfs(self, start = 0):
        # perform a breadth-first search algorightm to find all
        # neighboring nodes of start
        # with start = 0 this is used to check connectivity by assuring
        # that ret of bfs = range(length(self.mtx))
        
        # check all nodes from start + 1 to the end
        # and call bfs recursively
        ret = set([start])
        for i in range(start + 1, self.n):
            if self.mtx[start][i] > 0:
                ret = ret.union(self.bfs(i))
        return ret

    def find_max(self, bound):
        # find the maximal element in self.mtx, but smaller than bound
        # and return its position
        m = 0
        mi = 0
        mj = 0
        for i in range(self.n):
            for j in range(self.n):
                r = self.mtx[i][j]
                if r > m and r < bound:
                    m = r
                    mi = i
                    mj = j
        return (mi, mj)
        
    def remove_highest(self, bound = 1200):
        # remove the highest element such that connectivity is not lost
        print "remove_highest - finding a good maximum"
        while True:
            print "bound = " + str(bound)
            G = nx.Graph()
            (mi, mj) = self.find_max(bound)
            m = self.mtx[mi][mj]
            if m == 0:
                return 0
            self.mtx[mi][mj] = 0
            self.mtx[mj][mi] = 0
            G.add_nodes_from(list(range(self.n)))
            for i in range(self.n):
                for j in range(i, self.n):
                    if self.mtx[i][j] > 0:
                        G.add_edge(i, j)
            if nx.is_connected(G):
                return m
            self.mtx[mi][mj] = m
            self.mtx[mj][mi] = m
            bound = m
            
    def weight(self):
        # return the weight of the graph
        s = 0
        for i in range(self.n):
            for j in range(i, self.n):
                s += self.mtx[i][j]
        return s

    def pprint(self):
        print "-"*50
        for row in self.mtx:
            s = ""
            for el in row:
                s += str(el) + " "
            print s
        print "-"*50
        print "Weight: " + str(self.weight())

if __name__ == '__main__':
    f = open("id_0107.txt")
    ss = f.read()
    f.close()
    n = Network(ss)
    saved = 0
    s = 1200
    while True:
        s = n.remove_highest()
        n.pprint()
        if s == 0:
            break
        saved += s
    print "Total saved: " + str(saved)
