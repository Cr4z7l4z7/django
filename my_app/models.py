from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
     name = models.CharField(max_length=250, unique=True)
     url = models.URLField(unique = True)

     def __str__(self):
         return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class User(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
