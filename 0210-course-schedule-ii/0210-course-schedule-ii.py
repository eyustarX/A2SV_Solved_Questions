class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        ans = []
        for a,b in prerequisites:
            course[b].append(a) 
            incoming[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
                
        while queue:
            c = queue.popleft()
            ans.append(c)

            for n in course[c]:
                incoming[n] -= 1
                if incoming[n] == 0:
                    queue.append(n)
        
        return ans if len(ans) == numCourses else []


