from django.db import models




class Contact(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"

    
class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactModel'
        verbose_name_plural = 'ContactModels'


class Testemonial(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="media/")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testemonial'
        verbose_name_plural = "Testemonials"

class HistoryTitle(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "HistoryTitle"
        verbose_name_plural = "HistoryTitles"


class History(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Historyes'

class About(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

class Index(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='media/')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Index'
        verbose_name_plural = "Indexes"



