# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        dic = {e.id: e for e in employees}
        q = [dic[id]]
        total = 0
        while q:
            emp = q.pop(0)
            total += emp.importance
            for i in emp.subordinates:
                q.append(dic[i])
        return total


ss = Solution()
asd = [[1,2,[2]],[2,3,[]]]
emplo = Employee(1,2,[2])
print(ss.getImportance(employees=emplo,id=2))
