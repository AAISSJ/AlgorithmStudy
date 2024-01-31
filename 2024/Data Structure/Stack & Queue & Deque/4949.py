while True : 
    string = input()
    if string=='.':
        break 

    stack = []
    answer = True
    for char in string : 
        if char in "([":
            if char == "(":
                stack.append(")")
            elif char=="[":
                stack.append("]")
        elif char in ")]":
            if not stack :
                answer = False
                break
            elif stack[-1]==char:
                stack.pop()
            else: 
                answer = False
                break
  
    if not stack and answer :
        print("yes")  
    else: 
        print("no")
