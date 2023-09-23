from datetime import datetime

sub = float(input('What is the subtotal?'))

current_date_and_time = datetime.now()
day_of_week = int(1)
print('###################### Invoice ########################')
if day_of_week == 1 or day_of_week == 2:
    discount = 0.1 * sub
    sub -= discount
    print(f'Discount -> {discount:.2f}')
sales_tax = float(0.06) * sub
sub += sales_tax
print(f'Sales tax -> {sales_tax:.2f}')
print(f'Total -> {sub:.2f}')