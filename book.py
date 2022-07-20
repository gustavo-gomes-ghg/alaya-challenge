#!/usr/bin/env python3

class Book:
    """
        Book class

        name  : book name
        year  : publish year
        author: author name
        theme : literature theme
    """

    # Properties
    name   = None
    year   = None
    author = None
    theme  = None

    # constructor
    def __init__(self, name, year, author, theme) -> None:
        self.name   = name
        self.year   = year
        self.author = author
        self.theme  = theme

    # Serializer
    def __repr__(self):
        return str({
            'name'  : self.name,
            'year'  : self.year,
            'author': self.author,
            'theme' : self.theme
        })