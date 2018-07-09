#Write a Python program to display a number in left, right and center aligned of width 10.
x=22
print("\n Original number = ",x)
print("Left alligned width 10 bytes :"+"{:<10d}".format(x)+"33")
print("Right aligned width 10 bytes:"+"{:10d}".format(x))
print("Center alligned")
print("11"+"{:^10d}".format(x)+"33")

