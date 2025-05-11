# link: https://leetcode.com/problems/valid-parentheses/
class Stack:
    def __init__(self):
        self.my_stack = [] 
    
    def push(self, value):
        self.my_stack.append(value)
        return True

    def pop(self):
        if len(self.my_stack) == 0:
            return None
        return self.my_stack.pop()
    
    def __len__(self):
        return len(self.my_stack)

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        my_stack = Stack()
        for char in s:
            if char in ["(", "{", "["]:
                my_stack.push(char)
            else:
                value = my_stack.pop()
                if value:
                    if value == "(" and char == ")":
                        continue
                    elif value == "{" and char == "}":
                        continue
                    elif value == "[" and char == "]":
                        continue 
                    else:
                        return False
                else:
                    return False
        
        return False if len(my_stack) else True