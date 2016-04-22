word = input("Enter a word")
num_of_vowels = 0
for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        num_of_vowels = num_of_vowels + 1

print("There are", num_of_vowels, "vowels in", word)
