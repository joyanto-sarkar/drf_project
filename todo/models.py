from django.db import models

# Create your models here.

class Todo(models.Model):
    """ todo task model """

    title = models.CharField(max_length = 255)
    description = models.TextField()
    status = models.CharField(max_length = 255)


    def __str__(self):
        """ obj as string representation """
        return self.title
