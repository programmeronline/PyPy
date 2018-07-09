string = input("Enter a string: ")
print(string[:1]+string[1:].replace(string[0],'$',len(string)))
