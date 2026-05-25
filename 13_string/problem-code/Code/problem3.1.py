'''
remove extra space and convert it ti titles, 
then check how many "o" are comming in given 
string '''

text = "     i love python programming "

print(text.strip()) 
print(text.title()) 
print(text.count("o"))