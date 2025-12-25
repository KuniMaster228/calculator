class Calculator:
    def __init__(self):
        pass
    def add(self, a, b):
        return a + b 
    def subtract(self, a, b):
        return a - b 
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Ошибка деления на 0"
        return a / b
      
calculator = Calculator()

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))

result_summ = calculator.add(a, b)
result_raz= calculator.subtract(a, b)
result_umn = calculator.multiply(a, b)
result_del = calculator.divide(a, b)

print('Сумма ', result_summ)
print('Разность ', result_raz)
print('Произведение ', result_umn)
print('Частное ', result_del) 