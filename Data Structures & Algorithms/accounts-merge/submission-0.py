class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[py] < self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        emailToAcc = {}
        
        for i, account in enumerate(accounts):
            for e in account[1:]:
                if e in emailToAcc:
                    dsu.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        print(emailToAcc)
        emailGroup = defaultdict(list)

        for e, i in emailToAcc.items():
            parent = dsu.find(i)
            emailGroup[parent].append(e)
        print(emailGroup)
        res = []

        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        
        return res

        

