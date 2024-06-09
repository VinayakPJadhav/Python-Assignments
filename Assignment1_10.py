# Write a Program which Accept Name From user and Display Length of its name.

def Length(iNo1):
    print(len(iNo1))


def main ():
    iNo=" "
    print("Enter The Name : ")
    iNo=(str(input()))

    Length(iNo)

if __name__=="__main__":
    main()