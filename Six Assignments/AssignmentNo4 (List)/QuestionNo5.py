# 5. Write a program that input a string and ask user to delete a given
#  word from a string. 

text = input(" Enter a string: ")

word_to_delete = input("Enter the word to delete...")

new_text = text.replace(word_to_delete , "")

new_text = " ".join(new_text.split())

print(" String after deletion: " , new_text)
