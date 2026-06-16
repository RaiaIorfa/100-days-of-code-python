l_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
u_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def decrypt(text, shift):
    decode = ""
    for letter in text:
        if letter in l_alphabet:
            shift_position = l_alphabet.index(letter) - shift
            decode += l_alphabet[shift_position]
        elif letter in u_alphabet:
            shift_position = u_alphabet.index(letter) - shift
            decode += u_alphabet[shift_position]
        else:
            decode += letter
    print(f"Here is the encoded result [{decode}]")

def encrypt(text, shift):
    encode = ""
    for letter in text:
        if letter in l_alphabet:
            shift_position = l_alphabet.index(letter) + shift
            encode += l_alphabet[shift_position % len(l_alphabet)]
            # index = l_alphabet.index(letter)
            # index += shift
            # if index > 25:
            #     new_index = index - len(l_alphabet)
            #     encode += l_alphabet[new_index]
            # else:
            #     encode += l_alphabet[index]
        elif letter in u_alphabet:
            shift_position = u_alphabet.index(letter) + shift
            encode += u_alphabet[shift_position % len(u_alphabet)]
            # index = u_alphabet.index(letter)
            # index += shift
            # if index > 25:
            #     new_index = index - len(u_alphabet)
            #     encode += u_alphabet[new_index]
            # else:
            #     encode += u_alphabet[index]
        else:
            encode += letter
    print(f"Here is the encoded result [{encode}]")

print("WELCOME TO CIPHER GENERATOR!")
task = int(input("Type '1' to encrypt or type '2' to decrypt: "))
text = input("Type your message: \n")
shift = int(input("Type the shift number: "))

if task == 1:
    encrypt(text, shift)
elif task == 2:
    decrypt(text, shift)
