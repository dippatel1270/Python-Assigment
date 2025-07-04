# Write a Python program to read the contents of a file and print them on the console.
file = open("demo.txt","r")
print(file.read())
file.close()

# Write a Python program to write multiple strings into a file

file = open("demo2.txt","w")
file.writelines("Hello World!\nGood morning")
file.close()