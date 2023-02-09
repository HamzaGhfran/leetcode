class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        for x in s:
            if x == "(" or x == "[" or x == "{":
                list.append(x)
            elif x == "]" or x == ")" or x == "}":
                if not list:
                    return False
                elif x == ")" and list[-1] ==  "(":
                    list.pop(-1)
                elif x == "}" and list[-1]==  "{":
                    list.pop(-1)
                elif x == "]" and list[-1]==  "[":
                    list.pop(-1)
                else:
                    return False
        if not list:
            return True
        else:
            return False