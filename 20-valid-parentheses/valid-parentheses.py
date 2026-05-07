class Solution:
    def isValid(self, s):

        stack = []

        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            if char in "([{":
                stack.append(char)

            else:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0