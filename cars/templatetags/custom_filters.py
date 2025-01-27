from django import template
from decimal import Decimal, ROUND_HALF_UP

register = template.Library()

@register.filter
def discount_price(value, percentage):
    try:
        # Преобразуем значение в Decimal для точных вычислений
        discount = Decimal(percentage) / Decimal(100)
        discounted_price = value - (value * discount)
        
        # Округляем результат до 2 знаков после запятой
        discounted_price = discounted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        return discounted_price
    except (ValueError, TypeError, AttributeError):
        return value
