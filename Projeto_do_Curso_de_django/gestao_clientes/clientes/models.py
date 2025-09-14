from django.db import models
from django.core.mail import send_mail

class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('deletar_clientes', 'Deletar clientes'),
        )

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name
    
    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)

        send_mail(
            "Novo cliente cadastrado",
            "o cliente %s foi cadastrado" % self.first_name,
            "REMOVIDO@gmail.com",  #quando eu quiser é so colocar o meu email
            ["REMOVIDO@gmail.com"],  #quando eu quiser é so colocar o meu email
            fail_silently=False,
        )

    def __str__(self):
        return self.first_name + ' ' + self.last_name


