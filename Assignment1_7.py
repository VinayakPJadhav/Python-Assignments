
def Divisible(iNo):
    if iNo % 5 == 0 :
        print ("True")
    else:
        print("False")

def main():
    iNo1=0
    print("Enter The Number : ")
    iNo1=(int(input()))

    Divisible(iNo1)

if __name__=="__main__":
    main()