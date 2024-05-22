from django.db import models

class UserInput(models.Model):
    input_text = models.TextField()

    def __str__(self):
        return self.input_text