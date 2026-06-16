alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def ceaser_cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
         shift_amount *= -1
         
    for letter in original_text:
            if letter in alphabet:
                shift_position = alphabet.index(letter) + shift_amount
                shift_position %= len(alphabet)
                output_text += alphabet[shift_position]
            else:
                output_text += letter
    print(f"Here is the {encode_or_decode}d result [{output_text}]")


print("WELCOME TO CIPHER GENERATOR!")
rerun = 'yes'

while rerun == "yes":
    task = input("Type 'encode' to encrypt or type 'decode' to decrypt: ")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: "))

    ceaser_cipher(original_text=text, shift_amount=shift, encode_or_decode=task)

    rerun = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()