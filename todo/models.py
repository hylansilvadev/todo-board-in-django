from django.db import models

class Auditable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Todo(Auditable):
    STATUS = (
        ('O','Para Fazer'),
        ('N','Fazendo'),
        ('C','Feito'),
    )
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    status = models.CharField(max_length=1, default='O', choices=STATUS, blank=False, null=False)

    def __str__(self):
        return self.title