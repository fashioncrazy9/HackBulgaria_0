# count_words.py

def count_words(words):
    result = {}

    
    for word in words:

        if word in result:
            result[word] += 1

        else:
            result[word] = 1
            
    return result

list1 = ["words", "are", "meaningful", "words", "words", "are"]
print(count_words(list1))
