
print("Enter String: ", end="")
text = input()

print("Enter a Word to Delete: ", end="")
word = input()

wordlist = text.split()
if word in wordlist:
    text = text.replace(word, "\b")
    print("\nNew String without \"" +word+ "\":")
    print(text)
else:
    print("\n\"" +word+ "\" is not found in the string!")