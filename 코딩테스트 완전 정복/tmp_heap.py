import heapq


class MaxHeap : 
    def __init__(self) :
        self.heap = []
        
        
    def push(self, value) :
            heapq.heappush(self.heap, -value)
            
            
    def pop(self) : 
            return -heapq.heappop(self.heap)
        

max_heap = MaxHeap ( )

MaxHeap.push(max_heap, 10)
MaxHeap.push(max_heap, 1100)

print(MaxHeap.pop(max_heap))