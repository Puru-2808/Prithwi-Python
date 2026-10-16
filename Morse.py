while True:

    characters = [
    
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z',

    
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9',

    
    '.', ',', '?', "'", '!', '/',
    '(', ')', '&', ':', ';', '=',
    '+', '-', '_', '"', '$', '@']
    
    morse = [
    
    '.-', '-...', '-.-.', '-..', '.', '..-.',
    '--.', '....', '..', '.---', '-.-', '.-..',
    '--', '-.', '---', '.--.', '--.-', '.-.',
    '...', '-', '..-', '...-', '.--', '-..-',
    '-.--', '--..',

    
    '-----', '.----', '..---', '...--', '....-',
    '.....', '-....', '--...', '---..', '----.',

    
    '.-.-.-', '--..--', '..--..', '.----.',
    '-.-.--', '-..-.', '-.--.', '-.--.-',
    '.-...', '---...', '-.-.-.', '-...-',
    '.-.-.', '-....-', '..--.-', '.-..-.',
    '...-..-', '.--.-.']

    A=int(input("press 1 to convert into morse, press 2 to convert from morse: "))

    if A==1:
        
        text=input("Enter message: ").upper()
        for i in range(len(text)):
            if text[i]==" ":
                print("/", end=" ")
            else:
                for j in range(len(morse)):
                    if characters[j]==text[i]:
                        print(morse[j], end=" ")
                        break
        print()


    elif A==2:

        text=input("Enter message: ")
        codes=text.split()
        for i in range(len(codes)):
            if codes[i]=="/":
                print(" ", end="")
            else:
                for j in range(len(morse)):
                    if morse[j]==codes[i]:
                        print(characters[j], end="")
                        break
        print()

    else:
        print("Invalid choice")

    
    
    b=input("Do you want to continue?(y/n): ").lower()
    while True:
            if b!="y" and b!="n":
                print("Enter valid input")
                b=input("Do uou want to continue?(y/n): ")
            else:
                break
    if b=="n":
            break

print("Be careful who you trust, people you know can hurt you the most")
    
