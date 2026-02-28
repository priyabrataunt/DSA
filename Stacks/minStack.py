class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val:int):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val) # minimum Element

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

import json

input_ops = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

min_stack = MinStack()
result = [None]

i = 1
while i < len(input_ops):
    operation = input_ops[i]

    if operation == "push":
        min_stack.push(input_ops[i + 1])
        result.append(None)
        i += 2
    elif operation == "pop":
        min_stack.pop()
        result.append(None)
        i += 1
    elif operation == "top":
        result.append(min_stack.top())
        i += 1
    elif operation == "getMin":
        result.append(min_stack.getMin())
        i += 1
    else:
        raise ValueError(f"Unsupported operation: {operation}")

print(json.dumps(result))