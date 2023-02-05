bookinfo = [] 
class bookshelf: 
    global book_info 
    def __init__(self,author,book_name,price,year): 
        self.bkauthor = author 
        self.bkname = book_name 
        self.bkprice = price 
        self.bkyear = year 
    def add_book(self):  
        
        print("Book Author : " + self.bkauthor)
        print("Book Name : " + self.bkname)
        print("Book Price : " + str(self.bkprice))
        print("Book Year: " + str(self.bkyear))
        print("Book Added") 
        book_info = [self.bkauthor,self.bkname,str(self.bkprice),str(self.bkyear)] 
        print("Book Appended In List = " + str(book_info))  
        
        
bokrot = bookshelf("Ruskin Bond","My Friend Ramu",1500,2011)
bokrot.add_book() 
bokrot1 = bookshelf("R.K. Narayan","Swami and Friends",1800,1991)
bokrot1.add_book()    
bokrot2 = bookshelf("J.K. Rowling","Harry Potter and the Deathly Hallows",2032,2006)
bokrot2.add_book()
bokrot3 = bookshelf("Ruskin Bond","My Friend Ramu",500,2006)
bokrot3.add_book()