from django import forms
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })
            field.label = field.label.capitalize()   # add another name for label
            field.widget.attrs['style'] = 'margin-bottom: 10px;'
            field.help_text = mark_safe(field.help_text + '<br>') if field.help_text else ''

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })
            field.label = field.label.capitalize()   # add another name for label
            field.widget.attrs['style'] = 'margin-bottom: 10px;'
            field.help_text = mark_safe(field.help_text + '<br>') if field.help_text else ''

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })
            field.label = field.label.capitalize()
        self.fields['code'].label = "Mã đơn hàng"
        self.fields['customer'].label = "Khách hàng"
        self.fields['complete'].label = "Trạng thái đơn"
        self.fields['pay'].label = "Trạng thái thanh toán"
        self.fields['price_policy'].label = "Chính sách giá"
class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })
