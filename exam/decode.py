def reverse_dict(a):
    result = {}
    
    for key in a:
        value = a[key]
        result[value] = key
    
    return result

def string_to_char_list(string):
    result = []
    for ch in string:
        result += [ch]
   
    return result

def char_list_to_string(char_list):
    result = ""
    for ch in char_list:
        result += ch
    
    return result

def decode_word(encrypted_word, cipher):
    cipher = reverse_dict(cipher)
    #print(cipher)
    encrypted_word = string_to_char_list(encrypted_word)
    #print(encrypted_word)

    index = 0

    for index in range(0, len(encrypted_word)):
        for key in cipher:
            if key == encrypted_word[index]:
                encrypted_word[index] = cipher[key]
        index += 1


    return char_list_to_string(encrypted_word)

print(decode_word("wfhsftzzuys",{'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}))