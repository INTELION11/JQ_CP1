    # JQ 1st Cezar Cipher encoder decoder  
    #  user choice for encode decode or quit  
    # set up lists for encoded and decoded messages   
while True:
    choice = input("do you want to \n1. decode\n2. encode\n3. quit\n").strip().lower()  
    encoded_message = []  
    decoded_message = []  
    
        # turn letter into a number with ord  
        # add moved amount to the number  
        # return the moved number  
    def encoder(x, y):  
        coded = ord(x)  
        coded += y  
        return coded  

        # make sure input is an integer  
        # subtract the moved to get original number  
        # turn number back into a letter with chr 
    def decoder(x, y):  
        letter = int(x)    
        letter -= y  
        decoded = chr(letter)  
        return decoded  
        # take message and moved amount from user  
        # encode each letter in the message using encoder  
        # add all encoded numbers to a list and print  
    if choice == "encode" or choice == "2":  
        message = input("what message do you wish to encode? ")  
        number = int(input("by what number? "))  
        list_message = list(message)  
        for letter in list_message:  
            encoded_letter = encoder(letter, number)  
            encoded_message.append(encoded_letter)  
        print(encoded_message)  
             #doit
    # take the list of numbers and moved amount from user  
        # decode each number to a letter using decoder  
        # join all decoded letters to make the message and print  
    elif choice == "decode" or choice == "1":  
        message = input("enter the encoded numbers separated by spaces: ")  
        number = int(input("by what number? "))  
        list_message = message.split()  
        for num in list_message:  
            decoded_letter = decoder(num, number)  
            decoded_message.append(decoded_letter)  
        print("".join(decoded_message))  
        # want to exit  
        # display goodbye message  
        # program stops here  
    elif choice == "quit" or choice == "3":  
        print("thanks for your service")  
    else:  
        print("please try again")  
