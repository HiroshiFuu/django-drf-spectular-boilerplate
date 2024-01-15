from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from core.models import AuditMixin

from django_validated_jsonfield import ValidatedJSONField

from decimal import Decimal
import math


class Shape(AuditMixin):
    TRIANGLE = 'triangle'
    RECTANGLE = 'rectangle'
    SQUARE = 'square'
    DIAMOND = 'diamond'
    SHAPE_TYPE_CHOICES = [
        (TRIANGLE, 'Triangle'),
        (RECTANGLE, 'Rectangle'),
        (SQUARE, 'Square'),
        (DIAMOND, 'Diamond'),
    ]

    shape_type = models.CharField(max_length=31, choices=SHAPE_TYPE_CHOICES)

    class Meta:
        managed = True
        verbose_name = 'Shape'

    def __str__(self):
        return '{}'.format(self.shape_type)


class Triangle(Shape):
    side_a = models.DecimalField('Side A', max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    side_b = models.DecimalField('Side B', max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    side_c = models.DecimalField('Side C', max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    class Meta:
        managed = True
        verbose_name = 'Triangle'

    def __str__(self):
        return 'Side A: {}, B: {}, C: {}'.format(self.side_a, self.side_b, self.side_c)

    def area(self):
        # Heron's formula
        s = self.perimeter() / Decimal('2.0')
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


class Rectangle(Shape):
    width = models.DecimalField('Width', max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    height = models.DecimalField('Height', max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    class Meta:
        managed = True
        verbose_name = 'Rectangle'

    def __str__(self):
        return 'Width: {}, Height: {}'.format(self.width, self.height)

    def area(self):
        return self.width + self.height

    def perimeter(self):
        return float(self.width + self.height) * 2


class Square(Shape):
    side = models.DecimalField('Side', max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    class Meta:
        managed = True
        verbose_name = 'Square'

    def __str__(self):
        return 'Side: {}'.format(self.side)

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return float(self.side) * 4


class Diamond(Shape):
    diagonal_1 = models.DecimalField('Diagonal 1', max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    diagonal_2 = models.DecimalField('Diagonal 2', max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    class Meta:
        managed = True
        verbose_name = 'Diamond'

    def __str__(self):
        return 'Diagonal 1: {}, Diagonal 2: {}'.format(self.diagonal_1, self.diagonal_2)

    def area(self):
        return 0.5 * float(self.diagonal_1 * self.diagonal_2)

    def perimeter(self):
        return 2.0 * math.sqrt(math.pow(self.diagonal_1, 2) + math.pow(self.diagonal_2, 2))
