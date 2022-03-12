from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20, db_column="name", primary_key=True)
    branch = models.CharField(max_length=20 ,db_column="branch")
    roll = models.IntegerField(db_column="roll")
    age = models.IntegerField()
    class Meta:
        db_table = 'Person'
    def __str__(self):
        return self