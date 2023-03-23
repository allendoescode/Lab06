encode_thing = None
decode_thing = None

#Allen Alexander
def encoder(encode_thing):
    decode_thing = []
    final = ""
    for i in encode_thing:
        decode_thing.append(int(i))
    for i in decode_thing:
        j = i + 3
        final += str(j)
    return final

def decoder(encode_thing):
    result = []
    final = ""
    for i in encode_thing:
        result.append(int(i))
    for i in result:
        j = i - 3
        final += str(j)
    return final


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            encode_thing = input("Please enter your password to encode: ")
            decode_thing = encoder(encode_thing)
            print("Your password has been encoded and stored!")
            continue
        elif option == 2:
            print("The encoded password is " + str(decoded_thing) + " and the original password is " + str(encoded_thing) + ".")
        else:
            print("No")
            continue


if __name__ == "__main__":
  main()

