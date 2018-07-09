string=input("Enter a string: ")
count = 0
for ch in string:
    if(ch in "abcdefghijklmnopqrstuvwxyz"):
        count+=1
print("Number of characters in given string is ",count)
