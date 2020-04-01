# Basic Subsitution algorithm.

def encrypt(text, s):
    # Result string initialized to store the cipher text.
    result = ""

    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text.

        if char == ' ':
            result += "*"
            # s is the key.

        elif (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
            # s is the key.

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
            # s is the key.

    return result

text = "CEASER CIPHER DEMO"
s = 5

print('Plain text :' + text)
print('Cipher text :' + encrypt(text,s))
