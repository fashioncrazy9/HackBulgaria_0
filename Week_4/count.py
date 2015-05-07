# count.py

def count_vowels_consonants(word):

    vowels = 'aeiouyAEIOUY'
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'

    result = { "vowels" : 0,
            "consonants":0
            }
    

    for ch in word:

        if ch in vowels:
            result["vowels"] += 1
    
        elif ch in consonants:
            result["consonants"] += 1
            

    return result

print(count_vowels_consonants("aaaAEcccD"))
