import heapq

class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.task_map = {}   # taskId -> (priority, userId)
        self.task_heap = []  # max-heap by (-priority, -taskId, userId)
        
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (priority, userId)
            heapq.heappush(self.task_heap, (-priority, -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (priority, userId)
        heapq.heappush(self.task_heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task_map[taskId][1]
        self.task_map[taskId] = (newPriority, userId)
        heapq.heappush(self.task_heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.task_heap:
            priority, neg_taskId, userId = heapq.heappop(self.task_heap)
            taskId = -neg_taskId
            priority = -priority
            if taskId in self.task_map and self.task_map[taskId] == (priority, userId):
                del self.task_map[taskId]
                return userId
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()