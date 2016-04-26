def convert_to_binary(eng_data):
    chars = list(eng_data)
    binary = []
    for i in chars:
        binary.append(bin(ord(i))[2:])
        binary.append(" ")
    return ''.join(binary)


def binary_read(bin_data):
    chars = bin_data.split()
    res = []
    for i in chars:
        res.append(chr(int(i, 2)))
    return ''.join(res)

if __name__ == '__main__':

    choice = int(input("Press\n\t1: To read binary data\n\t2: To convert your string to binary\n\tYour Choice: "))
    if choice == 1:
        data = input("Enter binary string :: ")
        unicode = binary_read(data)
        print("Equivalent human string :: "+unicode)

    else:
        data = input("Enter your string :: ")
        bin_data = convert_to_binary(data)
        print("Equivalent binary string :: "+bin_data)

    input()
