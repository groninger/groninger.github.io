
"""
A Rail Fence cipher that works both ways
"""

def scram2Encrypt(plaintext):

    evenChars= ''
    oddChars=''

    charCount = 0
    for ch in plaintext:
        if charCount % 2 is 0:
            #so an even character
            evenChars = evenChars + ch
        else:
            #so odd character
            oddChars = oddChars + ch

        charCount = charCount + 1

    cipherText = oddChars + evenChars
    return cipherText


thing=input("Please text something: ")

msg=scram2Encrypt(thing)
print(msg)



def decryptMessage(cipherText):
    halfLength = len(cipherText)//2
    oddChars = cipherText[:halfLength]
    evenChars=cipherText[halfLength:]
 
    plainText=''
 

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(evenChars)>len(oddChars):
        plainText = plainText +evenChars[-1]
    
    
    return plainText


stuff=input("To decrypted: ")
stuff = decryptMessage(stuff)
print(stuff)


