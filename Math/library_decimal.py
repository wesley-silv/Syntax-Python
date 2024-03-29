# Using the module to work with decimal numbers.
from decimal import Decimal

gain_June = Decimal('99.92')*8
print(f'Cash in the month of June:',gain_June)

cost_June = Decimal('110.1')*4
print(f'Costs of month of June:',cost_June)

box_opening = gain_June - cost_June
print(f'Received in this month:',box_opening)