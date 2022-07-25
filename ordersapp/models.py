from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete

from django.conf import settings
from mainapp.models import Products

class Order(models.Model):
    STATUS_FORMING = 'FM'
    STATUS_SENT_TO_PROCEED = 'STP'
    STATUS_PROCEEDED = 'PRD'
    STATUS_PAID = 'PD'
    STATUS_READY = 'RDY'
    STATUS_CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (STATUS_FORMING, 'формируется'),
        (STATUS_SENT_TO_PROCEED, 'отправлен в обработку'),
        (STATUS_PAID, 'оплачен'),
        (STATUS_PROCEEDED, 'обрабатывается'),
        (STATUS_READY, 'готов к выдаче'),
        (STATUS_CANCEL, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name='статус', choices=ORDER_STATUS_CHOICES, max_length=3, default=STATUS_FORMING)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Текущий заказ {self.pk}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    def total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity*x.product.price, items)))

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, verbose_name='продукт', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity


@receiver(pre_save, sender=OrderItem)
def product_quntity_update_save(sender, instance, **kwargs):
    if instance.pk:
        instance.product.quantity -= instance.quantity - OrderItem.objects.get(pk=instance.pk).quantity
    else:
        instance.product.quantity -= instance.quantity

    instance.product.save()

@receiver(pre_delete, sender=OrderItem)
def product_quntity_delete_save(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()

    instance.is_active = False
    instance.save()

