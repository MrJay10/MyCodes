"""
A Python3 program to read and write morse codes
"""

# A dictionary to co-relate each character with morse equivalent
morse = {
"A" : ".-", 
"B" : "-...", 
"C" : "-.-.", 
"D" : "-..", 
"E" : ".", 
"F" : "..-.", 
"G" : "--.", 
"H" : "....", 
"I" : "..", 
"J" : ".---", 
"K" : "-.-", 
"L" : ".-..", 
"M" : "--", 
"N" : "-.", 
"O" : "---", 
"P" : ".--.", 
"Q" : "--.-", 
"R" : ".-.", 
"S" : "...", 
"T" : "-", 
"U" : "..-", 
"V" : "...-", 
"W" : ".--", 
"X" : "-..-", 
"Y" : "-.--", 
"Z" : "--..", 
"0" : "-----", 
"1" : ".----", 
"2" : "..---", 
"3" : "...--", 
"4" : "....-", 
"5" : ".....", 
"6" : "-....", 
"7" : "--...", 
"8" : "---..", 
"9" : "----.", 
"." : ".-.-.-", 
"," : "--..--"
}


def encode():
"""
Converts your string into morse
"""
    message=input("Enter your message (without whitespaces) :: ").upper()
    print("Morse code for "+message+" :: ")
    for i in message:
        print(morse[i],end=' ')
    print()

def decode():
"""
Reads a morse into readable english
"""
    message=input("Enter the morse code (with spaces) :: ")
    alist = message.split()
    for i in alist:
        for m,n in morse.items():
            if n==i:
                print(m,end='')
        print("",end=' ')
    print()

if __name__ == '__main__':
    ch = int(input("Press 1 to encode your message in morse code !\nPress 2 to decode a morse code !\nPress 3 to exit !\n"))

    while ch != 3:
        if ch == 1:
            encode()
        elif ch == 2:
            decode()
        ch = int(input("Press 1 to encode your message in morse code !\nPress 2 to decode a morse code !\nPress 3 to exit !\n"))
