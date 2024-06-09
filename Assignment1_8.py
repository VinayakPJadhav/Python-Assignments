# Write a Program which Accept Number from user and print number of "  *  " on screen.

def Pattern(iNo):
    i=0
    for i in range(0,iNo):
        print("*")

    


def main():
    iNo=0
    print("Enter The Number : ")
    iNo=(int(input()))

    Pattern(iNo)

if __name__=="__main__":
    main()