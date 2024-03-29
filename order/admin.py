from django.contrib import admin

# Register your models here.
from order.models import ShopCart, OrderProduct, Order


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['code', 'tableno', 'total', 'status']
    list_filter = ['status']
    readonly_fields = ('user', 'ip', 'total')
    can_delete = False
    inlines = [OrderProductline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']


admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)