from collections import defaultdict

dict = defaultdict(str)

dict["A"] = "g"
dict["@"] = "d"

dict["@"] += "   d"

print(dict)