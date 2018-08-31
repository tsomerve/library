from django.db import models



class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = 'books')
    title = models.CharField(max_length=100)
    published = models.DateField()
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} {self.title}'