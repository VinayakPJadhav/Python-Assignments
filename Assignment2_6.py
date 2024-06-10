# Write A program  Which Accept Number From user And Display Below Pattern.
def Pattern(iNo2):
       for i in range(iNo2 + 1, 0, -1):    
        for j in range(0, i - 1):  
            print("*", end=' ')  
        print(" ")  

def main():
    iNo1=int(input("Enter the Number : "))
    Pattern(iNo1)

if __name__=="__main__":
    main()