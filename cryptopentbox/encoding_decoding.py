import base64

def encoding():
    message = input('Enter your message:\n')
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("\nYou message encoded base64 is:")
    print(base64_message)
    message = input('\nEnter anything to exit :\n')

def decoding():
    try:
        base64_message = input('Enter your message:\n')
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        print("\nYou message decoded from base64 is:")
        print(message)
        message = input('\nEnter anything to exit :\n')
    except:
        print("invalid input do you want to retry?")
        answer ='0'      
        while answer =='0':
            answer = input('y/n:\n')
            if answer == "y":
                print("\nRetrying...\n") 
                decoding()
            elif answer == "n":
                print('\nThanks for using, goodbye.')
                exit
            else:
                print("I don't understand your choice.")
                answer='0'
        
