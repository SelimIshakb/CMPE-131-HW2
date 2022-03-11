f = open("document.txt", "r", encoding="utf8")
txt = f.read()
f.close()
unique_words = {}

for key in txt.split():
    if key in unique_words:
        unique_words[key] += 1
    else:
        unique_words[key] = 1

words_list = list(unique_words.items())
n = len(words_list)
i = 0

while i < n:
    j = 0
    while j < n-i-1:
        if words_list[j][1] > words_list[j + 1][1]:
            temp = words_list[j + 1]
            words_list[j + 1] = words_list[j]
            words_list[j] = temp
        elif words_list[j][1] == words_list[j + 1][1] and words_list[j][0] < words_list[j + 1][0]:
            temp = words_list[j + 1]
            words_list[j + 1] = words_list[j]
            words_list[j] = temp
        j += 1
    i += 1

words_list.reverse()
print()
for word_tuple in words_list[:5]:
    print(word_tuple[0] + ":", word_tuple[1])