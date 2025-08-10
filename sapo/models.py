from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=255,null=True, blank=True)
    brand = models.CharField(max_length=255,null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    qr_code = models.CharField(max_length=255, null=True, blank=True)
    mass = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    tag = models.CharField(max_length=100, null=True, blank=True)
    import_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True, blank=True)
    wholesale_price = models.DecimalField(default=0,max_digits=10, decimal_places=2, null=True, blank=True)
    retail_price = models.DecimalField(default=0,max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    unit_type =(
        ('kg', 'kilogram'),
        ('g', 'gam'),
    )
    unit = models.CharField(max_length=2, choices=unit_type, null=True, blank=True)

    status = models.BooleanField(default=True, null=True, blank=True)
    tax = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
class Customer(models.Model):
    
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    employee_care = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    debit = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True, blank=True)
    tag = models.CharField(max_length=100, null=True, blank=True)
    segment = models.CharField(max_length=100, null=True, blank=True)
    tax_code = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price_policy = models.CharField(max_length=100, null=True, blank=True)
    customer_discount = models.CharField(max_length=100, null=True, blank=True)
    payment = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse('customer_detail', args=[str(self.id)])

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    pay = models.BooleanField(default=False, null=True, blank=True)
    price_policy = models.CharField(max_length=100, null=True, blank=True)
    sale_location = models.CharField(max_length=100, null=True, blank=True)
    employee_sale = models.CharField(max_length=100, null=True, blank=True)
    ship_date = models.DateField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    chanel = models.CharField(max_length=100, null=True, blank=True)
    path = models.CharField(max_length=100, null=True, blank=True)
    reference = models.CharField(max_length=100, null=True, blank=True)
    ship_address= models.CharField(max_length=100, null=True, blank=True)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return str(self.code)
    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])

    
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.order)
	@property
	def get_total(self):
		total = self.product.retail_price * self.quantity
		return total
     

class File(models.Model):
    file = models.FileField(upload_to='files')