file = "books/frankenstein.txt"

with open(file) as f:
    file_contents = f.read()


def count_words(string):
    words = file_contents.split()
    return len(words)


def count_letters(string):
    s = string.lower()
    dic = {}
    for i in s:
        if i.isalpha():
            dic[i] = dic.get(i, 0)+1
    return dic


list_letters = list(count_letters(file_contents).items())
list_letters.sort(key=lambda x: x[1], reverse=True)

print("--- Begin report of", file, "---")
print(count_words(file_contents), "words found in the document")
print("")

for letter, num in list_letters:
    print("The '", letter, "' character was found ", num, " times", sep='')

print("--- End report ---")
