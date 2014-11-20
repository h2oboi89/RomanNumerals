class Stack:
    def __init__(self):
        self._items = []
        
    def isEmpty(self):
        return self.size() == 0
        
    def push(self, item):
        self._items.append(item)
        
    def pop(self):
        if self.isEmpty():
            return None
        
        return self._items.pop()
        
    def peek(self):
        if self.isEmpty():
            return None
            
        return self._items[self.size()-1]
        
    def size(self):
        return len(self._items)
        
    def clear(self):
        self._items = []
        
    def __str__(self):
        return '{{{0}}}'.format(', '.join(map(str, self._items)))