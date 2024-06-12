# Write A Program Which Accpet Number From User and store it into list
# Return Maximum of all

def main ():
    list_1=[];
    print("Number of element ")
    size= int(input())
    for i in range(0,size):
        iElement=int(input("Enter the Values: "))
        list_1.append(iElement)

    
    print("Minimum is : ",min(list_1))
        
    
    
    
if __name__=="__main__":
    main()
