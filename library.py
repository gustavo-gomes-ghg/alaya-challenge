#!/usr/bin/env python3

from book import Book

class Library:

    # global lists
    books    = []
    authors  = []
    themes   = []

    # Base book class object
    base_book = Book('', '', '', '')

    # constructor
    def __init__(self) -> None:
        """
            empty constructor
        """
        pass

    # Setter - write book
    def writeBook(self, nome, ano, autor, tema):
        """
            Write book in book list
        """
        newBook = Book(nome, ano, autor, tema)
        
        self.books.append( newBook )

    # Setter - write author
    def writeAuthor(self, name):
        """
            Write author in author list
        """
        
        self.authors.append( name )

    # Setter - write theme
    def writeTheme(self, theme):
        """
            Write theme in theme list
        """
        
        self.themes.append( theme )

    # Getter - get book
    def getBook(self, filter_name, filter_value):
        """
            get book from book list
        """

        # check for available filters
        if ( not filter_name in list(self.base_book.__dict__.keys()) ):
            return None

        # find objects
        return filter( lambda v: getattr(v, str.lower(filter_name) ) == filter_value, self.books )


# To be able to run as script
if ( __name__ == '__main__' ) :

    library = Library()

    library.writeBook('xalala', 2022, 'Boneco', 'Teste')
    library.writeBook('livro2', 2018, 'Gustavo', 'Ficcao cientifica')
    library.writeBook('livro3', 2019, 'Ricardo', 'Teste')
    library.writeBook('livro4', 2022, 'Gustavo2', 'Testedsdsdsdsds')

    # Query "database"
    objects = library.getBook('theme', 'Teste')

    # Parse response
    _response = list( objects ) if ( objects is not None ) else None

    # return
    print( _response  )