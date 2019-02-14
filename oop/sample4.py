class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "{} by {}".format(self.title, self.author)
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print ("Object instance deleted")

b = Book(title="Python Rocks!", author='Alex', pages=100 )        
print (b)
print (len(b))

del b