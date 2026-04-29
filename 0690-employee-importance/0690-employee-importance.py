"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {e.id:e for e in employees}
        ans = 0

        def dfs(id):
            nonlocal ans
            node = emp_map[id]
            ans += node.importance

            for sub_id in node.subordinates:
                dfs(sub_id)
        
        dfs(id)
        return ans