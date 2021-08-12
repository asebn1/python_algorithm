strInput = input()
stack = []

for i in strInput:
    if i == '(' or i == '[':
        stack.append(i)
    else:
        # )
        if i == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                temp = 0
                for idx in range(len(stack)-1, -1, -1):
                    if stack[idx] == '(':
                        stack[-1] = temp*2
                        break
                    else:  # int 형
                        temp += stack[-1]
                        stack.pop()
        # ]
        if i == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                temp = 0
                for idx in range(len(stack)-1, -1, -1):
                    if stack[idx] == '[':
                        stack[-1] = temp*3
                        break
                    else:  # int 형
                        temp += stack[-1]
                        stack.pop()
print(sum(stack))

        