tl = [("abcd", 4), ("zx", 2), ("d", 1), ("abc", 3)]
print(tl)
sl = sorted(tl, key = lambda x : x[1])
tl.sort(key = lambda x : x[1])
print(tl)
