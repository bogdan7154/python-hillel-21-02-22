# узнаем значение, сумму прибыли и процент налога
profit = float(input("Введите сумму прибыли: "))
tax = float(input("Какой процент составляет налог?"))

# вычисляем сколько составит налог и чистую прибыль после уплаты налога
tax_amount = profit / 100 * tax
marginality = profit - tax_amount

# выводим значения
print("Сумма налога: {:.2f} грн".format(tax_amount))
print("Сумма чистой прибыли: {:.2f} грн".format(marginality))