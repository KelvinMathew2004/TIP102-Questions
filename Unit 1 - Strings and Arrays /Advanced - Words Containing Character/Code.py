def words_with_char(words, x):
    res = []
    for i in range(len(words)):
        if x in words[i]:
            res.append(i)
    return res
