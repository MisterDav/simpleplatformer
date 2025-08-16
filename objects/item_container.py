from objects.item import Item

class Item_Container():
    
    def __init__(self, max_size = -1):
        self.max_size = max_size
        self.container = []

    def add(self, item):
        if len(self.container) == self.max_size: return
        self.container.append(item)

    def pop(self):
        if len(self.container) == 0: return None
        val = self.container[-1]
        del self.container[-1]
        return val
    
    def get(self, i):
        if len(self.container) == 0: return None
        return self.container[i % len(self.container)]

    def set(self, i, item):
        if len(self.container) == 0: return
        self.container[i] = item