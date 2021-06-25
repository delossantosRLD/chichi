from django.db import models

# Create your models here.

class Device(models.Model):

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('On Hand', 'Item with available stocks'),
        ('Deal', 'Item sold'),
        ('Replenishing', 'Item for restocking')
    )

    status = models.CharField(max_length=20, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

class Desktops(Device):
    pass

class Laptops(Device):
    pass

class Mobiles(Device):
    pass


#class Category(models.Model):
#    cat_Name = models.TextField(default="")
#    cat_Desc = models.CharField(default="", max_length=20)
#    class meta:
#        db_table = "Category"

    #def __str__(self):
    #   return self.name    

#class Supplier(models.Model):
#    sup_Name = models.TextField(default="")
#    sup_Address = models.CharField(default="", max_length=50)
#    sup_Contact = models.CharField(default="", max_length=12)
#    class meta:
#        db_table = "Supplier"

    #def __str__(self):
    #   return self.name

#class Employee(models.Model):
#    emp_Firstname = models.TextField(default="")
#    emp_Lastname = models.TextField(default="")
#    emp_Address = models.CharField(default="", max_length=50)
#    emp_Contact = models.CharField(default="", max_length=12)
#    class meta:
#        db_table = "Employee"

    #def __str__(self):
    #   return self.name

#class PurchaseOrder(models.Model):
#    PO_order_date = models.DateField(default=timezone.now)
#    PO_Emp_ID = models.ForeignKey(Employee, default="", on_delete=models.CASCADE)
#    PO_Sup_ID = models.ForeignKey(Supplier, default="", on_delete=models.CASCADE)
#    class meta:
#        db_table = "Purchase Order"

    #def __str__(self):
    #   return self.name    

#class Product(models.Model):
#    ProdCat_ID = models.ForeignKey(Category, default="", on_delete=models.CASCADE)
#    Prod_Name = models.TextField(default="")
#   Prod_Qty = models.IntegerField(blank=True, null=True)
#   Prod_Unit = models.TextField(default="")
#  Prod_Price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
#   Prod_Desc = models.CharField(default="", max_length=20)
#   STATUS_CHOICES = (
#       ('On Hand', 'Item with available stocks'),
#      ('Deal', 'Item sold'),
#       ('Replenishing', 'Item for restocking')
#       )
#   Prod_Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="SOLD")
#   Prod_ID = models.ForeignKey(Supplier, default="", on_delete=models.CASCADE)
#   class meta:
#      db_table = "Product"

    #def __str__(self):
    #   return self.Prod_Name + ' '

#lass OrderDetails(models.Model):
#   PO_order_ID = models.ForeignKey(PurchaseOrder, default="", on_delete=models.CASCADE)
#   OD_price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
#   OD_Qty = models.IntegerField(blank=True, null=True)
#   Prod_ID = models.ForeignKey(Product, default="", on_delete=models.CASCADE)
#   class meta:
#       db_table = "Order Details"

    #def __str__(self):
    #   return self.name

#lass Sale(models.Model):
#   Sale_Prod_ID = models.ForeignKey(Product, default="", on_delete=models.CASCADE)
#   Sale_Emp_ID = models.ForeignKey(Employee, default="", on_delete=models.CASCADE)
#   Sale_date = models.DateField(default=timezone.now)
#   Sale_time = models.TimeField(default=timezone.now)
#   class meta:
#       db_table = "Sale"
