word = input("enter the word: ")
rev_word = word[:: -1]
if word == rev_word:
    print("word is palindrome")
else:
    print("word is not palindrome")
