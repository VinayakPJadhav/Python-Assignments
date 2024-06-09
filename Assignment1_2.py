# Write a program Which contains one funcation Nmaed as ChkNum() which Accepts one parametre
# as number. if number is even the it Should " Even number " otherwise
# Display "odd Number " on console.



def ChkNum(No):
    if No % 2 == 0:
        print("Even number")
    else :
        print("Odd Number")
    
def main():  
 
    print("Enter the number : ")
    iNO=int(input())
    ChkNum(iNO)  


if __name__ =="__main__":
    main()