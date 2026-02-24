class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        dsu=DSU(26)
        for x in equations:
            if x[1]=='=':
                a=ord(x[0])-ord('a')
                b=ord(x[3])-ord('a')
                dsu.unite(a,b)
        for x in equations:
            if x[1]=='!':
                a=ord(x[0])-ord('a')
                b=ord(x[3])-ord('a')
                if dsu.find(a)==dsu.find(b):
                    return False
        return True
class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
        self.component=n

    def find(self,x):
        if x==self.parent[x]:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def unite(self,a,b):
        a=self.find(a)
        b=self.find(b)

        if a==b:
            return False
        if self.size[a]<self.size[b]:
            a,b=b,a
        self.parent[b]=a
        self.size[a]+=self.size[b]
        self.component-=1
        return True
    
    