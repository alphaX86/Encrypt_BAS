print('Hello there!!')

#Vigenere Cipher Implementation 
baseAlphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

plainText = raw_input("Please enter the plain text")
key = raw_input("Please enter the key word")
keyList = []
keyLength = 0
while keyLength < len(plainText):
    # Adds the users entered key into a list character by character. 
    # Also makes the key the same length as plainText
    for char in key:
        if keyLength < len(plainText):
            keyList.append(str(char))
            keyLength = keyLength + 1

# The variable each processed letter is appended to
completeCipherText = [] 
# This is the value used to temporaily store the ciphertext character during the iteration
cipherCharIndexValue = 0
keyIncrement = 0

# Iterates through the plain text
for plainTextChar in plainText:
        # Adds the base alphabets index value of the key and the plain text char
        cipherCharIndexValue = baseAlphabet.index(keyList[keyIncrement]) + baseAlphabet.index(plainTextChar)
        while cipherCharIndexValue > 25:
             # makes the addition value under 26 as to not go out of range of base alphabet tuple
            cipherCharIndexValue = cipherCharIndexValue - 26 
         # appends the ciphertext character to the completeCipherText variable. 
         # The character is the index of the key + index of the       plainTextChar from baseAlphabet
        completeCipherText.append(baseAlphabet[cipherCharIndexValue])
         # Moves onto the next key
        keyIncrement = keyIncrement + 1
print ''.join(completeCipherText) # Makes the result a strings for printing to the console.


