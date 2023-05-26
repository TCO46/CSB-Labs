sentence = input("Write a sentence: ")

word_list = sentence.split(" ")


unique_words = []

for i in word_list:
    if i not in unique_words:
        unique_words.append(i)

count = len(unique_words)
print(count)