def isSubsequence(s: str, t: str) -> bool:
    t = iter(t)
    # print(list(i in t for i in s))
    for i in t:
        print(i)

    for j in t:
        print(j)

print(isSubsequence("axc", "ahbgdc"))
