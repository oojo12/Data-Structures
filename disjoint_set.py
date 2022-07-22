class DisjointSet:
    def __init__(self, size):
        self.rank = [1]*size
        self.root = [i for i in range(size)]
        
    # path compression
    def find(self, x):
        # found final parent
        if x == self.root[x]:
            return x
        # recursive call to find parent of index x
        self.root[x] = self.find(self.root[x])
        
        # return values
        return self.root[x]
    
    # union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # cycle detected
        if rootX==rootY:
            return True
        else:
            if self.rank[rootX] <= self.rank[rootY]:
                self.rank[rootY] += self.rank[rootX]
                self.root[rootX] = self.root[rootY]
            else:
                self.rank[rootX] += self.rank[rootY]
                self.root[rootY] = self.root[rootX]
            return False
