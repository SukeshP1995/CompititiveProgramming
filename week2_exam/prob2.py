import functools

inputs = [
        [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
        [[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]],
        [[2,4], [5,1], [3,3], [1,5], [4,2], [6,0]],
        ]


class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def pop(self):
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

def comparator(x, y):
    if x[0]!=y[0]:
        return y[0]-x[0]
    else:
        return x[1]-y[1]
for inp_list in inputs:
    print(inp_list)
    inp_list.sort(key = functools.cmp_to_key(comparator))

    rque = Stack()
    stack = Stack()
    
    for lst in inp_list:
        # e = 
        while lst[1] < rque.size() and rque.size()!=0:
            stack.push(rque.pop())
        while lst[1] > rque.size() and stack.size()!=0:
            rque.push(stack.pop())
        rque.push(lst)

    while stack.size() != 0:
        rque.push(stack.pop())

    result = []
    while rque.size() != 0:
        result.insert(0, rque.pop())
    print(result)