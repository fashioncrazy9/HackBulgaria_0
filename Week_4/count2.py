def count_sounds(word):
    result = {"vowels": 0,
        "consonants": 0}

    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    for ch in word:
        if ch in vowels:
            result["vowels"] +=1
        elif ch in consonants:
            result["consonants"] += 1

    return result

a = "hhhwwwooo"
print(count_sounds(a))