# Cezar Cipher encoder decoder

#separator = ", "
#my_string = separator.join(my_list)

choice = input("do you want to \n1. decode\n2. encode?\n3. quit\n").strip().lower()
encoded_message = []
decoded_message = []


#encoder
def encoder(x,y):
    coded = ord(x)
    coded += y
    return coded
def decoder(x,y):
    letter += number
    decoded = chr(letter)
    return decoded

#def (variable)
#letter = ord("variable")
#if user choise is encode
#ask for message
#ask for number
#make message list
#coede_num = ord("message")
if choice == "encode":
    message = input("what message do you wish to encode?")
    number = input("by what number?")
    list_message = list(message)
    for letter in list_message:
        encoded_letter = encoder(letter,number)
        encoded_message.append(encoded_letter)
elif choice == "decode":
    message = input("what message do you wish to encode?")
    number = input("by what number?")
    list_message = list(message)
    for letter in list_message:
        decoded_letter = decoder(letter,number)
        decoded_message.append(decoded_letter)
elif choice == "quit":
    print("thanks for your service")
else:
    print("please thry again")
