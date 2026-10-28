class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sign = set()
        sign.add("+")
        sign.add("-")
        sign.add("*")
        sign.add("/")
        stack = []
        output = 0
        first = 0
        sec = 0
        for token in tokens:
            if token in sign:
                sec = stack.pop()
                first = stack.pop()
                if token == "+":
                    output = first + sec
                if token == "-":
                    output = first - sec
                if token == "*":
                    output = first * sec     
                if token == "/":
                    output = int(first / sec)
                stack.append(output)
            else:
                stack.append(int(token))
        output = stack.pop()
        return output