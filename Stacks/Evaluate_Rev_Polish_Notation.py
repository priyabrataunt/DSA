
def evalRun(tokens):
    stack = []
    for item in tokens:
            if item == "+":
                stack.append(stack.pop() + stack.pop())
            elif item == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif item == "*":
                stack.append(stack.pop() * stack.pop())
            elif item == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(item))
            
    return stack[0]       

print(evalRun(["1","2","+","3","*","4","-"]))