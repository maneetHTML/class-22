def mw (words):
    ctr =0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print(lst)
    return ctr
count = mw (['abc', 'cfc','xyz', 'aba', '1221','mam','def','jij'])
print("Number of words having first and last character same:", count)