# Write a Program Which accept number From User And Store It Into List.
# Accept One Another MNumber From User And Check Frequency of that Number from list

def main ():
    list_1=[];
    print("Number of element ")
    size= int(input())
    for i in range(0,size):
        iElement=int(input("Enter the Values: "))
        list_1.append(iElement)

    iNo=int(input("Enter Number "))

    def countX(list_1,iNo):
        count=0
        for i in list_1:
            if (i==iNo):
                count=count+1
                return count

    print(countX(list_1,iNo))

    
        
    
    
    
if __name__=="__main__":
    main()