class Book:
    """
    A class to represent a Book with title, author, and publication year.
    """
    
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation of the Book for easy reading.
        
        Returns:
            str: Format: "Title by Author, published in Year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation that can recreate the Book instance.
        
        Returns:
            str: Format: "Book('Title', 'Author', Year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"