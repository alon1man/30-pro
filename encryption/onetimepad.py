def one_time_pad(text,keyword):
    a_b="abcdefghijklmnopqrstuvwxyz"
    text=text.lower()
    textlist=[]
    keyword=keyword.lower()
    keywordlist=[]
    newtext=""
    for i in text:
        textlist.append(a_b.find(i))
    for i in keyword:
        keywordlist.append(a_b.find(i))
    for i in range(len(textlist)):
        newtext+=a_b[(textlist[i]+keywordlist[i])%26]
    if len(text) != len(newtext):
        newtext ="invalid data"
    return newtext

def one_time_pad_decrypt(ciphertext, keyword):
    a_b = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ciphertext.lower()
    textlist = []
    keyword = keyword.lower()
    keywordlist = []
    newtext = ""

    for i in ciphertext:
        textlist.append(a_b.find(i))
    for i in keyword:
        keywordlist.append(a_b.find(i))
    for i in range(len(textlist)):
        newtext += a_b[(textlist[i] - keywordlist[i]) % 26]

    if len(ciphertext) != len(newtext):
        newtext = "invalid data"

    return newtext