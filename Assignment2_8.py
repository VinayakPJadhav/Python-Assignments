 
# Write A program  Which Accept Number From user And Display Below Pattern.  

def Pattern(iNo2):
    for i in range(1,iNo2+1):    
        for j in range(1,iNo2+1):  
            print(j, end=' ')  
        print(" ")  

def main():
    iNo1=int(input("Enter the Number : "))
    Pattern(iNo1)

if __name__=="__main__":
    main()