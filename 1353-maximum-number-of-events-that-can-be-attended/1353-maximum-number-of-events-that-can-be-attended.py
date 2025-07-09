class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        attended = 0
        final_day = max(event[1] for event in events)
        event_idx = 0
        n = len(events)
        min_heap = []
        for day in range(1, final_day + 1):
            while event_idx < n and events[event_idx][0] == day:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1
            
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
        return attended
            

