class MyCircularQueue:
    # [1,2,3]
    def __init__(self, k: int):
        self.q = []
        self.k = k
        self.count = 0 #count num of items in q

    def enQueue(self, value: int) -> bool:
        if self.count == self.k:
            return False
        self.q.append(value)
        self.count += 1
        return True
        
    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.q.remove(self.q[0])
        self.count -= 1
        return True
        
    def Front(self) -> int:
        return self.q[0] if self.q else -1

    def Rear(self) -> int:
        return self.q[-1] if self.q else - 1

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        return True if self.count == self.k else False
        




# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()