"""
A little program to encode a message with the vigenere encryption.

The Vigenere encryption takes in a message and a key as parameters and by transposing the key and the 
message onto a so called "Vigenere table", a new encoded text can be "calculated". The Vigenere table 
is a table, where the rows and the columns are labled with one character from the alphabet so that from the
top row to the bottom row the rows are labled from a to z and the same holds true for the columns (this
time from left to right obviously). Now you can find the character for the encoded message by simply
adding the index of the message character to the index of the key character in the alphabet.

I have no idea how to represent Characters as their ASCII value with python, so i had to 
make a alphabet-list called "alpha" to fetch the index of the characters in the standard
english alphabet. And because this is just a very simple/basic code, the code is very messy
and unnecessarily long. But I had fun implementing this encryption-algorithm so that's what
matters I guess.

And as always: The lines printed are all written in german because I am too lazy to 
write everything in english again.
"""

# defining the main function
def main(satz, key):
    # the alphabet list
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", \
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # this list will be used to store the indices of the characters in the message as well as in the 
    # key
    index_dict = []

    # forming pairs of characters and their index in the alphabet list
    i = 0
    key_i = 0
    while i < len(satz):
        word = []
        for j in satz[i]:
            if key_i < len(key):
                word.append([alpha.index(j), alpha.index(key[key_i])])
                key_i += 1
            else:
                key_i = 0
                word.append([alpha.index(j), alpha.index(key[key_i])])
                key_i += 1
        index_dict.append(word)
        i += 1

    # calculating the new characters
    for x in range(len(index_dict)):
        for y in range(len(index_dict[x])):
            index_dict[x][y] = alpha[(index_dict[x][y][0] + index_dict[x][y][1])%len(alpha)]
    
    # the encoded message
    encoded_list = ["".join(i) for i in index_dict]
    
    # print("The encoded message is: ")
    print("DIE VERSCHLÜSSELTE NACHRICHT LAUTET: ", end=" ")
    # printing the message
    for k in encoded_list:
        print(k, end=" ")

# starting point into the program
if __name__ == "__main__":
    # input of the message, which will be encoded
    satz = input("Satz zum Verschlüsseln: \n").split()
    satz = [i.lower() for i in satz]
    # input of a key of your choice
    key = input("Schlüssel: \n").lower()
    print()
    print("----------------------------")
    # print("The message:")
    print("Die Nachricht:", end="\n")
    print(" ", end="")
    # printing the message
    for i in satz:
        if satz.index(i) < len(satz)-1:
            print(i, end=" ")
        else:
            print(i, end="\n")
    print()
    # print("The key:")
    print("Der Schlüssel:\n", key)
    print("----------------------------")
    print()
    # calling the main function where "satz" is the message and "key" the encryption key
    main(satz, key)