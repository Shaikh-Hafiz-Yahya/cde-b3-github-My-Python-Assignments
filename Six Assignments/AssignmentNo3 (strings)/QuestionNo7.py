# 7. A palindrome is a string that reads the same backward as forward. For example, the words dad, 
# madam and radar are all palindromes. Write a programs that determines whether the string is a 
# palindrome. 
# Note: do not use reverse() method   

text = input("Enter a string: ")

is_palindrome = True   #e.g: Palindrome words ki examples(civic,madam,radar,'1001',..)

for i in range(len(text) // 2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{text} is a Palindrome..")
else:
    print(f"{text} is NOT a Palindrome...")
