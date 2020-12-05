class Solution:
    def interpret(self, command: str) -> str:
        answer = ""
        g = "G"
        for index in range(len(command)):
            if command[index] == g:
                answer += g
            elif command[index] == "(":
                if command[index+1] == "a":
                    answer += "al"
                else:
                    answer += "o"

        return answer
