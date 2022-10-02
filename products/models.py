from django.db import models

class Service(models.Model):
    service_number = models.IntegerField(default = 0)
    name = models.CharField(max_length = 200, help_text='Enter the service name')
    service_price = models.FloatField(default = 0)

    def set_service_number(self, number):
        self.service_number = number

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    product_id = models.CharField(max_length = 200, blank=True,  help_text='This will be auto generated')
    name = models.CharField(max_length=200, help_text='Enter the product name')
    date_issued = models.DateField('Date Published')
    included_services = models.ManyToManyField(Service, help_text='Select the services for this product')

    def save(self, *args, **kwargs):
        self.set_product_id()
        super(Product, self).save(*args, **kwargs)

    def set_product_id(self):
        self.product_id = self.name[0] + self.date_issued.strftime('%y') + self.date_issued.strftime('%m') + str(self.included_services.all().count())
        for i, n in enumerate(self.included_services.all()):
            n.set_service_number(self.date_issued.strftime('%y') + self.date_issued.strftime('%m') + str(i+1))
            n.save()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['date_issued']