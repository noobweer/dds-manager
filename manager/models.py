from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class OperationType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(OperationType, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        unique_together = ('name', 'type')

    def __str__(self):
        return f"{self.type.name} - {self.name}"


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    created_date = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    type = models.ForeignKey(OperationType, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def clean(self):
        super().clean()
        if self.category and self.type:
            if self.category.type != self.type:
                raise ValidationError(
                    {'category': 'Категория должна принадлежать выбранному типу.'}
                )
        elif self.subcategory and self.category:
            if self.subcategory.category != self.category:
                raise ValidationError(
                    {'subcategory': 'Подкатегория должна принадлежать выбранной категории.'}
                )

    def __str__(self):
        return f"{self.type.name} | {self.amount} руб."
