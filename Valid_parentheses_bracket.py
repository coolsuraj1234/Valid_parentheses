s = "[]()" # Random example
if s[0] == ")" or s[0] =="]" or s[0] =="}":
    print("False")

res = []
for i in s:
    if i == "(" or i == "[" or i == "{":
        res.append(i)
    elif (len(res) != 0 and (res[-1] == "(" or res[-1] == "{" or res[-1] == "[" )):
        if ((res[-1] == "(" and i == ")") or (res[-1] == "[" and i == "]") or (res[-1] == "{" and i == "}")):
            res.pop()
        else:
            print("False")
    else:
        print("False")
if len(res) == 0:
    print("True")



