# 8. Write a program that display following output: 
# SHIFT 
# HIFTS 
# IFTSH 
# FTSHI 
# TSHIF 
# SHIFT  

text = "SHIFT"

# Loop to generate shifts:
for i in range(len(text)):
    shifted = text[i:] + text[:i]
    print(shifted)
