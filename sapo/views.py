
import csv
import decimal
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.views import generic


from .forms import *

from .models import *

# Create your views here.

def index(request):
    return render(request, 'main.html')
def home(request):
    return render(request, 'home.html')

###################--------------------------PRODUCTS----------------------###########################################################
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        stock = request.POST.get('stock')
        retail_price = request.POST.get('retail_price')
        wholesale_price = request.POST.get('wholesale_price')
        import_price = request.POST.get('import_price')
        description = request.POST.get('description')
        unit = request.POST.get('unit')
        mass = request.POST.get('mass')
        image = request.FILES.get('image')
        print(image)
        status = request.POST.get('status')
        tax = request.POST.get('tax')
        print(image)

        new_product = Product(name=name, code=code, category=category, brand=brand, stock=stock, retail_price=retail_price, wholesale_price=wholesale_price, import_price=import_price, description=description, unit=unit, mass=mass, image=image, status=status, tax=tax)
        new_product.save()
        success = 'product "'+name+'" created successfully'
        return HttpResponse(success)
    return render(request, 'sapo/product_form.html')
	
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    context = {'form': form}
    return render(request, 'sapo/product_update.html',context)

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    context = {'product': product}
    return render(request, 'sapo/product_delete.html', context)

def product_list(request):
    const = Product.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')

        if name:
            products = products.filter(Q(name__icontains=name) | Q(name__isnull=True))
        if category:
            products = products.filter(Q(category__icontains=category) | Q(category__isnull=True))
        context = {'products': products, 'const': const}  

        return render(request, 'sapo/product_list.html',context)
    context = {'products': products, 'const': const}
    return render(request, 'sapo/product_list.html', context)

class ProductDetailView(generic.DetailView):
    model = Product # add more models separated by commas





########################------------------CUSTOMER--------------#######################
def add_customer(request):

    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    context = {'form': form}
    return render(request, 'sapo/customer_create.html', context)
def update_customer(request, pk):

    customer = Customer.objects.get(pk=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', pk=customer.pk)
    context = {'form': form}
    return render(request, 'sapo/customer_update.html',context)

def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    context = {'customer': customer}
    return render(request, 'sapo/customer_delete.html', context)

def customer_list(request):
    const = Customer.objects.all()
    customers = Customer.objects.all()
    if request.method == 'POST':
        employee_care = request.POST.get('employee_care')
        segment = request.POST.get('segment')

        if employee_care:
            customers = customers.filter(Q(employee_care__icontains=employee_care) | Q(employee_care__isnull=True))

        if segment:
            customers = customers.filter(Q(segment__icontains=segment) | Q(segment__isnull=True))
        context = {'customers': customers, 'const': const}  

        return render(request, 'sapo/customer_list.html',context)
    context = {'customers': customers, 'const': const}
    return render(request, 'sapo/customer_list.html', context)

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = Order.objects.filter(customer=customer).values()
    print(customer,'\n',orders)
    cart_total = 0
    for order in orders:
        cart_total += order['total']
    context = {'customer': customer, 'orders': orders, 'cart_total': cart_total}
    return render(request, 'sapo/customer_detail.html', context)


############################        ORDER              ############################
def add_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    context = {'form': form}
    return render(request, 'sapo/order_create.html', context)

def update_order(request, pk):

    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', pk=order.pk)
    context = {'form': form}
    return render(request, 'sapo/order_update.html',context)

def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    context = {'order': order}
    return render(request, 'sapo/order_delete.html', context)
def order_list(request):
    const = Order.objects.all()
    orders = Order.objects.all()
    if request.method == 'POST':
        complete = request.POST.get('complete')
        if complete:
            complete = True if complete.lower() == 'true' else False
            orders = orders.filter(complete=complete)

        pay = request.POST.get('pay')
        if pay:
            pay = True if pay.lower() == 'true' else False
            orders = orders.filter(pay=pay)
        context = {'orders': orders, 'const': const}

        return render(request, 'sapo/order_list.html', context)
    context = {'orders': orders, 'const': const}
    return render(request, 'sapo/order_list.html', context)


def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    orderitems = OrderItem.objects.filter(order=order)
    print(orderitems)
    context = {'order': order, 'orderitems': orderitems}
    return render(request, 'sapo/order_detail.html', context)

#################################          ORDERITEM  ODERITIEM             #############################


def update_orderitem(request, pk):

    orderitem = OrderItem.objects.get(pk=pk)
    print(orderitem.order.pk)
    form = OrderItemForm(instance=orderitem)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=orderitem)
        if form.is_valid():
            form.save()
            return redirect('order_detail', pk=orderitem.order.pk)
    context = {'form': form}
    return render(request, 'sapo/orderitem_update.html',context)

def delete_orderitem(request, pk):
    orderitem = OrderItem.objects.get(pk=pk)
    if request.method == 'POST':
        orderitem.delete()
        return redirect('order_detail', pk=orderitem.order.pk)

    context = {'orderitem': orderitem}
    return render(request, 'sapo/orderitem_delete.html', context)

def add_orderitem(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_id = request.POST.get('order')
            order = Order.objects.get(pk=order_id)
            form.instance.order = order
            form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderItemForm()
    context = {'form': form}
    return render(request, 'sapo/orderitem_create.html', context)













#################################       login            #######################################################################
from django.contrib.auth import login 
from django.contrib.auth import authenticate
def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'sapo/login.html')
    else:
        return render(request, 'sapo/login.html')

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('login')































##############################       DIRECT SALE       ####################################################################
def direct_sale(request):
    cus_form=CustomerForm()
    pro_form=ProductForm()
    order_form=OrderForm()

    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    print(request.POST.get('customer_id'))
    if request.method == 'POST' and request.POST.get('customer_id')=='cus':
        cus_form = CustomerForm(request.POST)
        if cus_form.is_valid():
            cus_form.save()
            cus_form = CustomerForm()

    if request.method == 'POST' and request.POST.get('product_id')=='pro':
        pro_form = ProductForm(request.POST)
        if pro_form.is_valid():
            pro_form.save()
            pro_form = ProductForm()
    
    if request.method == 'POST' and request.POST.get('order_id')=='order':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            order_form = OrderForm()
    
    # del request.session['order_direct_id']
    if request.session.has_key('order_direct_id'):
        
        order_direct = Order.objects.get(pk=request.session['order_direct_id'])
        print(request.session['order_direct_id'],'\n',order_direct.id)
        items = order_direct.orderitem_set.all() 
    else:
        order_direct = Order.objects.create()
        order_direct.save()
        request.session['order_direct_id'] = order_direct.id
        items = order_direct.orderitem_set.all() 
    
    context =  {'products': products,'pro_form':pro_form,'cus_form':cus_form,'customers': customers,'orders': orders,'order_form':order_form,'orders':orders,'order_direct':order_direct,'items':items}
    return render(request, 'sapo/direct_sale.html',context)


def updateItem(request):
    data = json.loads(request.body)
    order = Order.objects.get(pk=request.session['order_direct_id'])
    productId = data['productId']  
    action = data['action']
    print(data['customerId'])

    if data['customerId']!='' :
        customerId = data['customerId']
        customer = Customer.objects.get(id=customerId)
        order.customer = customer
        order.save()
    print(data)
    if data['productId']!='':
        product = Product.objects.get(id=productId)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()
    if data['action'] == 'payment':
        order.complete = True
        order.pay = True
        order.save()
        del request.session['order_direct_id']
    return JsonResponse('Item was updated', safe=False)






























#############---------------------------EXPORT CSV----------------------##################

def customer_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customer.csv"'

    writer = csv.writer(response)
    writer.writerow(['Tên', 'Địa chỉ', 'Điện thoại', 'Email'])

    customers = Customer.objects.all().values_list('name', 'address', 'phone', 'email')
    for customer in customers:
        writer.writerow(customer)

    return response



def product_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'

    writer = csv.writer(response)
    writer.writerow(['Mã sản phẩm', 'Tên sản phẩm', 'Đơn vị', 'Giá bán lẻ', 'Giá bán buôn', 'Giá nhập'])

    products = Product.objects.all().values_list('code', 'name', 'unit', 'retail_price', 'wholesale_price', 'import_price')
    for product in products:
        writer.writerow(product)

    return response

def order_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="order.csv"'

    writer = csv.writer(response)
    writer.writerow(['Mã đơn hàng', 'Ngày tạo đơn', 'Tên khách hàng', 'Trạng thái đơn hàng', 'Trạng thái thanh toán', 'Khách phải trả', 'Tổng tiền'])

    orders = Order.objects.all().values_list('code', 'date_created', 'customer_id', 'complete', 'pay', 'ship_address', 'total')
    
    print(orders)
    for order in orders:
        writer.writerow(order)

    return response
def orderitem_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="order_item.csv"'

    writer = csv.writer(response)
    writer.writerow(['Mã đơn hơn', 'Mã sản phẩm', 'Số luong'])

    order_items = OrderItem.objects.all().values_list('order_id', 'product_id', 'quantity')
    for order_item in order_items:
        writer.writerow(order_item)

    return response

############--------------------------IMPORT CSV----------------------##################

import pandas as pd
def create_db_customer(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in df.values]

    for l in list_of_csv:
        Customer.objects.create(
            name=l[0],
            address=l[1],
            phone=l[2],
            email=l[3],
        )
def import_csv_customer(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = File.objects.create(file=file)
        create_db_customer(obj.file)

        return redirect('/customers/')

    return render(request, 'sapo/IMPORT.html')
###########----------product--------------------###########
def create_db_product(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in df.values]

    for l in list_of_csv:
        Product.objects.create(
            code=l[0],
            name=l[1],
            unit=l[2],
            retail_price=l[3],
            wholesale_price=l[4],
            import_price=l[5],
        )
def import_csv_product(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = File.objects.create(file=file)
        create_db_product(obj.file)

        return redirect('/products/')

    return render(request, 'sapo/IMPORT.html')
########----------order-----------------------########
def create_db_order(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in df.values]

    for l in list_of_csv:
        customer = Customer.objects.get(id=l[2])

        Order.objects.create(
            code=l[0],
            date_created=l[1],
            customer=customer,
            complete=l[3],
            pay=l[4],
            ship_address=l[5],
            total=l[6],
        )
def import_csv_order(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = File.objects.create(file=file)
        create_db_order(obj.file)
        return redirect('/orders/')

    return render(request, 'sapo/IMPORT.html')

####################-------order_item-----------------------############
def create_db_orderitem(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in df.values]

    for l in list_of_csv:
        order = Order.objects.get(id=l[0])
        product = Product.objects.get(id=l[1])
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=l[2],
        )
def import_csv_orderitem(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = File.objects.create(file=file)
        create_db_orderitem(obj.file)
        return redirect('/orders/')

    return render(request, 'sapo/IMPORT.html')






















def lobby(request):
    return render(request, 'sapo/lobby.html')


from rest_framework import viewsets, permissions, filters
from sapo.serializers import *
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # Add ordering and search filter backends
    search_fields = ('name', 'code')  # Enable filtering by name and email fields



class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order_items to be viewed or edited.
    """
    queryset = OrderItem.objects.all().order_by('id')
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.AllowAny]