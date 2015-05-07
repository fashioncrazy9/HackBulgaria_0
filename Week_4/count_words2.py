def count_words2(words):

    result = {}

    for word in words:

        if word in result:
            result[word] += 1
        else:
            result[word] = 1


    return result

test_list = ['we', 'we', 'they', 'one']

print(count_words2(test_list))