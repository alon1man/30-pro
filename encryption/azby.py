def azby(sentence):
    a_to_z = " abcdefghijklmnopqrstuvwxyz"
    z_to_a = " zyxwvutsrqponmlkjihgfedcba"
    new_stirng = ""
    sentence = sentence.lower()
    for i in sentence:
        temp = a_to_z.find(i)
        if temp == -1:
            new_stirng += i
            continue
        new_stirng += z_to_a[temp]

    return new_stirng
def azby_decrypt(sentence):
    a_to_z = " abcdefghijklmnopqrstuvwxyz"
    z_to_a = " zyxwvutsrqponmlkjihgfedcba"
    newer_stirng = "" 
    sentence = sentence.lower()
    for i in sentence:
        temp = z_to_a.find(i)
        if temp == -1:
            newer_stirng += i
        else: 
            newer_stirng += a_to_z[temp]  
    return newer_stirng


