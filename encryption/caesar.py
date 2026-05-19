def caser(sentence, key):
    if isinstance(key, str) and key.isdigit():
        key = int(key)
    elif isinstance(key, (int, float)):
        key = int(key)
    else:
        key = 0

    a_z = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    sentence = sentence.lower()
    
    for i in sentence:
        if not (i.isalpha()):
            new_string += i
            continue
        
        # Calculate shift
        temp = a_z.find(i) + key
        new_string += a_z[temp % 26]
        
    return new_string

def caser_decrypt(sentence,key):
    if isinstance(key, str) and key.isdigit():
        key = int(key)
    elif isinstance(key, (int, float)):
        key = int(key)
    else:
        key = 0

    a_z = "abcdefghijklmnopqrstuvwxyz"
    newer_string = ""
    sentence = sentence.lower()
    
    for i in sentence:
        if not (i.isalpha()):
            newer_string += i
            continue
        
        # Calculate shift (subtracting moves backward)
        temp = a_z.find(i) - key
        newer_string += a_z[temp % 26]
        
        
    return newer_string