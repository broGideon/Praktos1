import math

num = 0
while num!=11:
    print ("Выберети действие")
    print("1. Сложиь 2 числа")
    print("2. Вычесть первое из второго")
    print("3. Перемножить два числа")
    print("4. Разделить первое на второе")
    print("5. Возвести в степень N первое число")
    print("6. Найти квадратный корень из числа")
    print("7. Найти факториал из числа")
    print("8. Найти синус")
    print("9. Найти косинус")
    print("10. Найти тангенс")
    print("11. Выход")
    try:
        num= int(input())
    except:
        print("Введите действие")
    match num:
        case 1:
            try:
                sum1 = float(input("Введите число 1:"))
                sum2 = float(input("Введите число 2:"))
                print('Ответ:', sum1 + sum2)
            except:
                print("Введено неверное значение")
        case 2:
            try:
                sum1 = float(input("Введите число 1:"))
                sum2 = float(input("Введите число 2:"))
                print('Ответ:',sum1 - sum2)
            except:
                print("Введено неверное значение")
        case 3:
            try:
                sum1 = float(input("Введите число 1:"))
                sum2 = float(input("Введите число 2:"))
                print('Ответ:',sum1 * sum2)
            except:
                print("Введено неверное значение")
        case 4:
            try:
                sum1 = float(input("Введите число 1:"))
                sum2 = float(input("Введите число 2:"))
                if sum2 != 0:
                    print('Ответ:',sum1 / sum2)
                else:
                    print('На ноль делить нельзя')
            except:
                print("Введено неверное значение")
        case 5:
            try:
                sum1 = float(input("Введите число 1:"))
                sum2 = float(input("Введите число 2:"))
                print('Ответ:',math.pow(sum1, sum2))
            except:
                print("Введено неверное значение")
        case 6:
            try:
                sum1 = float(input("Введите число:"))
                print('Ответ:',math.sqrt(sum1))
            except:
                print("Введено неверное значение")
        case 7:
            try:
                sum1 = int(input("Введите число:"))
                print('Ответ:',math.factorial(sum1))
            except:
                print("Введено неверное значение")
        case 8:
            try:
                sum1 = float(input("Введите число:"))
                print('Ответ:', math.sin(sum1))
            except:
                print("Введено неверное значение")
        case 9:
            try:
                sum1 = float(input("Введите число:"))
                print('Ответ:', math.cos(sum1))
            except:
                print("Введено неверное значение")
        case 10:
            try:
                sum1 = float(input("Введите число:"))
                print('Ответ:', math.tan(sum1))
            except:
                print("Введено неверное значение")