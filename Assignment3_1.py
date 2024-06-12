# Write A Program Which Accpet Number From User and store it into list
# Return Addition of all

def main ():
    list_1=[];
    total=0
    print("Number of element  ")
    size= int(input())
    print("Enter the Values")
    for i in range(0,size):
        iElement=int(input())
        list_1.append(iElement)
        total=total+list_1[i]
        
        
    
    print("Addition is : ",total)
if __name__=="__main__":
    main()

    
