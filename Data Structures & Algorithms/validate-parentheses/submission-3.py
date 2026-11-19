class Solution:
    def isValid(self, s: str) -> bool:
        lengt = len(s) 
        #remmber the last open bracket
        openBrackets = ""
        for i in range(lengt):
            if s[i] == "[":
                openBrackets = openBrackets + "["
            elif s[i] == "(":
                openBrackets += "("
            elif s[i] == "{":
                openBrackets += "{"
            elif s[i] == "]" and openBrackets != "":
                if openBrackets[-1] == "[":
                    openBrackets = openBrackets[:-1]
                else:
                    return False
            elif s[i] == ")" and openBrackets != "":
                if openBrackets[-1] == "(":
                    openBrackets = openBrackets[:-1]
                else:
                    return False
            elif s[i] == "}" and openBrackets != "":
                if  openBrackets[-1] == "{":
                    openBrackets = openBrackets[:-1]
                else:
                    return False
            else:
                return False
        if openBrackets == "":
            return True
        else:
            return False
