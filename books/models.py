from django.db import models

class Checkout(models.Model):
    text = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.text[:50]

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = 'books')
    title = models.CharField(max_length=100)
    published = models.DateField()