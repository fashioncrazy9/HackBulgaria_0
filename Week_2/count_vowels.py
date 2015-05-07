word = input("Enter a word: ")
vowels_in_word = []
vowels = "aeiouyAEIOUY" 


for ch in word:
    if ch in vowels:
        vowels_in_word += [ch]
        
print(len(vowels_in_word))