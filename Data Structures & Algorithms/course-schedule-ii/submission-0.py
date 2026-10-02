class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList=[[] for _ in range(numCourses)]
        indegrees=[0 for _ in range(numCourses)]
        for u, v in prerequisites:
            adjList[v].append(u)
            indegrees[u]+=1
        queue=deque()
        res=[]
        for i in range(numCourses):
            if indegrees[i]==0:
                queue.append(i)
        while len(queue)!=0:
            cur=queue.popleft()
            res.append(cur)
            for node in adjList[cur]:
                indegrees[node]-=1
                if indegrees[node]==0:
                    queue.append(node) 
        if len(res)==numCourses:
            return res
        return []                       
