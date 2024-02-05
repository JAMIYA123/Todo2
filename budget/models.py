from django.db import models

class Schedule(models.Model):
    title=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    options=(
        ("inprogress","inprogress"),
        ("pending","pending"),
        ("compleated","compleated")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")
    created_date=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title
