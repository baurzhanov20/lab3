N = int(input("Enter a positive integer: "))
a, b = 0, 1
while N > 0:
     print(a)
     a, b = b, a + b
     N -= 1


#N = int(input("Введите положительное целое число: ")): В этой строке пользователю предлагается ввести положительное целое число с помощью функции input(). Введенное целое число сохраняется в переменной N.
#a, b = 0, 1: Эта строка инициализирует две переменные, a и b, значениями 0 и 1 соответственно. Эти переменные будут использоваться для генерации последовательности Фибоначчи.
#while N > 0:: Эта строка запускает цикл while, который будет продолжаться до тех пор, пока значение N будет больше 0. Цикл будет выполняться в течение N итераций по мере уменьшения N на каждой итерации.
#print(a): Внутри цикла код выводит текущее значение a. Это следующее число в последовательности Фибоначчи.
#a, b = b, a + b: После печати a код обновляет значения a и b. Он присваивает a значение b и присваивает b сумму предыдущих значений a и b. Этот шаг генерирует следующее число в последовательности Фибоначчи.
#N -= 1: Значение N уменьшается на 1 на каждой итерации цикла, что гарантирует завершение цикла после вывода N чисел Фибоначчи.
#Итак, этот код принимает положительное целое число N в качестве входных данных, а затем использует цикл while для генерации и печати первых N чисел Фибоначчи, начиная с 0 и 1 и продолжая на основе последовательности Фибоначчи.