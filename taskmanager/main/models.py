from django.db import models
from django import forms
import pyodbc

from datetime import date as dt

from django.forms import ModelForm


class ModelSample(models.Model):
    Date = models.DateTimeField("Date")
    Name = models.CharField("Name", max_length=100)
    Count = models.IntegerField("Count")
    Distance = models.IntegerField("Distance")

    def __str__(self):
        return self.Name


class Sample:
    def __init__(self, date, name, count, distance):
        self.Date = date
        self.Name = name
        self.Count = count
        self.Distance = distance



class Sql:
    def __init__(self, database_name, server_name="(LocalDB)\MSSQLLocalDB"):
        driver = '{SQL Server Native Client 11.0}'
        self.conn = pyodbc.connect(
            Trusted_Connection="yes",
            Driver=driver,
            Server=server_name,
            Database=database_name
        )
        self.query = "--{}\n\n-- Made in Python".format(dt.today().strftime("%d-%m-%Y"))

    def manual(self, query, response=False):
        cursor = self.conn.cursor()
        if response:
            return cursor.execute(query).fetchall()
        else:
            return False
