# Project Start

# list of the alphabets

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

select = input("Type'encode' to encrypt or type 'decode' to decrypt :\n ")
message = input("Type your message:\n")
shift = int(input("Enter number of  swap:\n"))

# encryption function

def encrypt (message_para , shift_para):

    # encoded  text
    cipher_text = ""

    # shift the character
    for i in message_para:
        location_letter= alphabet.index(i)
        new_location = location_letter + shift_para
        cipher_text += alphabet[new_location]
    print(f"The encode text is {cipher_text}")


def decrypt(cipher_text,shift_para):
    decode_text= ""
    for i in cipher_text:
        location_letter = alphabet.index(i)
        new_location  =location_letter-shift_para
        decode_text +=alphabet[new_location]
    print(f"The decode message is {decode_text}")


if select == "encode" :
    encrypt(message_para=message,shift_para=shift)
elif select == "decode":
    decrypt(cipher_text=message,shift_para=shift)

