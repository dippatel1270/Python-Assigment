# Write a Python program to search for a word in a string using re.search()
import re
str1 =  "Tops technologies are provide best education for IT field"
pattern = "for"
ans = re.search("Tops,str1")
print(ans)
ans = re.search("are,str1")
print(ans)
ans = re.search("best",str1)
print(ans)

# Write a Python program to match a word in a string using re.match().

ans = re.match("o",str1)
print(ans)
ans = re.match("a",str1)
print(ans)
ans = re.match("e",str1)
print(ans)


