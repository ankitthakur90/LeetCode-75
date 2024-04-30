def mergeAlternately( word1, word2):
    i =0
    j=0
    str = ""
    while(i < len(word1) and j < len(word2)):
        str+=word1[i]
        str+=word2[j]
        i+=1
        j+=1

    while(i < len(word1)):
        str+=word1[i]
        i+=1
    while(j < len(word2)):
        str+=word2[j]
        j+=1
    return str

word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1,word2))