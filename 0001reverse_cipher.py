text = "Hello World!" # Text message.
cipher_text = "" # Variable to hold cipher text.

idx = len(text) - 1 # Variable to hold the index of cipher text.

while idx >= 0:
    cipher_text += text[idx]
    idx -= 1

#Printing the text message.
print(text)

#Printing the cipher text message.
print(cipher_text)
