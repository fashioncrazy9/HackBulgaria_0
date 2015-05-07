# words_count.py

w = input("Enter some text: ")
n = input("Enter total number: ")
n = int(n)

count = 1
words = []

while count <= n:
    word = input("Enter some text: ")

    words = words + [word]

    count += 1

times_found = 0

for word in words:
    if w in word:
        times_found += 1
print(w, "found", times_found, "times")
        
