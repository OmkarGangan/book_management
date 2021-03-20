# declare class of Book
class Book:
    
    # member method,object method
    def bid(self):
        
        # data member,instance variable,object variable
        self.bid = input('Enter Book Id =>')
        
    # member method,object method
    def bname(self):
        
        # data member,instance variable,object variable
        self.bname = input('Enter Book Name =>')
        
    # member method,object method
    def bprice(self):
        
        # data member,instance variable,object variable
        self.bprice = input('Enter Book Price =>')
        
    # member method,object method
    def getbook(self):
        print('Book Id:',self.bid)
        print("Book Name => ",self.bname)
        print("Book Price => ",self.bprice)
    
# list to append books
bookss = []

# declare function
def main():
    print('1 for Add Book')
    print('2 for Show Books')
    print('3 for Edit Book')
    print('4 for Remove Book')
    print('5 for Exit')
    
    # infinite loop while
    while True:
        
        # accept choice from user
        ch = int(input('Enter your choice =>'))
        
        # add book
        if ch == 1:
            
            # infinite loop while
            while True:
                
                # create an object for Book class
                b = Book()
                
                # call member method
                b.bid()
                b.bname()
                b.bprice()
                
                # append object to list
                bookss.append(b)
                print('Book has been added successfully.')
                
                # ask user to add books 
                ch = input('Do you want to add book? y/n =>')
                
                # user want to add book
                if ch in ['y','Y']:
                    # continue to add book
                    continue
                # user dont want to add book
                else:
                    # break the while loop
                    break
        # show book
        elif ch == 2:
            # check if book availavle in list or not
            if len(bookss)>0:
                # iterate through list of books available
                for i in bookss:
                    # call member method of selected ith book
                    print('--------------------------------------------')
                    i.getbook()

            # book not available
            else:
                print('Books not found')
          
        # edit book
        elif ch == 3:
            
            # accept book id from user
            bid = input('Enter book id you want to edit =>')
            
            # iterate through list of books available
            for i in bookss:
                
                # if user entered book available
                if bid == i.bid:
                    
                    # create object of book
                    b = Book()
                    # update price and name of book
                    b.bname()
                    b.bprice()
                    # update book id with same id as before
                    b.bid=i.bid
                    # remove old book from inventory
                    bookss.remove(i)
                    # append edited book to inventory
                    bookss.append(b)
                    print('Book has been edited successfully.')
                    break
                    
            # book not available
            else:
                print('Books not found')
           
        # remove book
        elif ch == 4:
            # accept book id from user
            bid = input('Enter Bood id you want to remove =>')
            # iterate through list of books available
            for i in bookss:
                # if user entered book available
                if bid == i.bid:
                    # remove that book from inventory
                    bookss.remove(i)
                    print('Book of Book Id {} is removed'.format(i.bid))
                    break
              
            # book not available
            else:
                print('Book not found')
        
        # quit
        elif ch == 5:
            
            # break the main infinite while loop
            break
        
        # invalid choice
        else:
            print('Try Again')        

# calling declared function
main()
