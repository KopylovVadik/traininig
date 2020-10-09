""""
Даны два числа A и B. Вам нужно вычислить их сумму
В этой задаче для работы с входными и выходными данными вы можете использовать и файлы и потоки на ваше усмотрение.
Первая и единственная строка входа содержит числа A и B, разделенные пробелом.
В единствегнной строке выхода вывидите сумму числел

"""
text = open("input.txt", "r").read()

numbersStr = text.splitlines()

lastnumber = 0

for numberStr in numbersStr:
    for i, number in enumerate(numberStr.split()):
        number = int(number)

        if (i == 1):
            print(lastnumber + number)
        else:
            lastnumber = number