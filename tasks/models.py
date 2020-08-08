from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title








        # email = request.POST['email']
        # password = request.POST['password']
        # user = User.objects.create_user(name=name, email=email, password=password)