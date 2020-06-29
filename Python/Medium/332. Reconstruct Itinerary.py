class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        if not tickets: return
        
        tickets_d = collections.defaultdict(list)
        for s,d in tickets:
            tickets_d[s].append(d)
            
        for s,d in tickets_d.items():
            d.sort(reverse=True)
        
        routes=[]
        def dfs(airport):
            deslist = tickets_d[airport]
            while deslist:
                src = deslist.pop()
                dfs(src)
            routes.append(airport)
        dfs("JFK")
        return routes[::-1]
		
		
		
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        if not tickets:
            return 
        tickets_d = collections.defaultdict(list)
        
        for src,dest in tickets:
            tickets_d[src].append(dest)
        routes = ["JFK"]
        
        def dfs(src):
            if len(routes)==len(tickets)+1:
                return True
            destinations = sorted(tickets_d[src])
            for des in destinations:
                routes.append(des)
                tickets_d[src].remove(des)
                if dfs(des):
                    return True
                tickets_d[src].append(des)
                routes.pop()
                
        dfs("JFK")
        return routes