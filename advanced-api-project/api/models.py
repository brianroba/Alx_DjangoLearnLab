from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Model to store author information.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model to store book details.
    Each book is linked to an Author via a foreign key, establishing a one-to-many relationship.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title