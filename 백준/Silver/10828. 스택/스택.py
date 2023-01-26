import sys

N = int(sys.stdin.readline())
instructions = []

for _ in range(0, N):
    instructions.append(sys.stdin.readline().strip())

stack = []

def push(elem: int):
    stack.append(elem)

def pop():
    if len(stack) == 0:
        print(-1)
        return

    print(stack.pop(-1))
    return

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
        return

    print(stack[-1])

for instruction in instructions:
    if instruction.split()[0] == 'push':
        push(int(instruction.split()[1]))
    elif instruction == 'pop':
        pop()
    elif instruction == 'size':
        size()
    elif instruction == 'empty':
        empty()
    elif instruction == 'top':
        top()
