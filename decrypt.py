"""
This program basically decrypts a Vigenere-encrypted message. The procedure is very similar
to encrypting a message but as you can see in Line 32, the "+" changes to a "-". If you want to 
get an understanding of what the Vigenere-encryption is, you can look up my "vigenere.py" code. In
that document I try to explain the basic concept a little bit. Also the rest I said in that code
holds true for this piece of computer-language.
"""

def decode(satz, key):
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", \
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    index_dict = []

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

    for x in range(len(index_dict)):
        for y in range(len(index_dict[x])):
            index_dict[x][y] = alpha[(index_dict[x][y][0] - index_dict[x][y][1])%len(alpha)] # - was + for encryption
    
    encoded_list = ["".join(i) for i in index_dict]
    
    print("DIE ENTSCHLÜSSELTE NACHRICHT LAUTET: ", end="")
    for k in encoded_list:
        print(k, end=" ")	

if __name__ == "__main__":
    satz = input("Satz zum Entschlüsseln: \n").split()
    satz = [i.lower() for i in satz]
    key = input("Schlüssel: \n").lower()
    print()
    print("----------------------------")
    print("Die Nachricht:", end="\n")
    print(" ", end="")
    for i in satz:
        if satz.index(i) < len(satz)-1:
            print(i, end=" ")
        else:
            print(i, end="\n")
    print()
    print("Der Schlüssel:\n", key)
    print("----------------------------")
    print()
    decode(satz, key)