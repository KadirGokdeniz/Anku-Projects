list1=[(0,11,7),(1,2,4),(2,4,5),(3,7,2),(4,3,1),(5,5,0),(6,1,10),(7,1,3),(8,7,0),(9,14,2),("*"),("#")] #(number of ticket, price of item,number  of stock)
account=eval(input("Enter your money in your account:")) #I can't import any card.That's why I am doing this.
def getinput():
    global key
    print("Enter a key:(not # and *)")
    key=int(input())
    return key
getinput()
def confirm1(key):
    key1=list1[key][0]
    return key1
def confirm2(key):
    key2=list1[key][1]
    return key2
def confirm3(key):
    key3=list1[key][2]
    return key3
while key!="*" or "#":
    if confirm3(key)==0:
        print("There is no stock for this item.Please,if you want to try for"+ "another item press # otherwise press *")
        respect1=str(input())
        if respect1=="#":
            getinput()
            continue
        elif respect1=="*":
            break
    elif confirm3(key)!=0:
        if confirm2(key)>account:
            print("There is no enough money in your account.")
            break
        elif account>=confirm2(key):
            account=account-confirm2(key)
            print("In your account,there is",account,"money at"+ " the moment.")
            print("Do you want to buy an extra item? Please"+ ", if you want to try for another item press # otherwise press *")
            respect2=str(input())
            if respect2=="#":
                getinput()      
            elif respect2=="*":
                print("Thanks for shopping.")
                break
   
            
      
           
                 


