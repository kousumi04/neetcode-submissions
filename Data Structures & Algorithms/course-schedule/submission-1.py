class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList=[[] for _ in range(numCourses)]
        indegrees=[0 for _ in range(numCourses)]
        for u, v in prerequisites:
            adjList[u].append(v)
            indegrees[v]+=1
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
            return True                
        return False    