class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(path, u):
            if u == len(graph)-1:
                result.append(path+[u])
            else:
                for v in graph[u]:
                    dfs(path+[u],v)
                    
        result=[]
        dfs([],0)
        return result