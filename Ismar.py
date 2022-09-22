gradebook = []
while True:

    command = input('Выберите одну из команд: \n'
                    '1 - time \n'
                    '2 - add and average\n'
                    '3 - step \n'
                    'exit - выйти из программы\n')
    if command == 'exit':
        print('Вы вышли из программы!')
        break
    elif command == '2':
        command1 = input('1 - Добавить \n'
                         '2 - Средняя оценка \n''')
        if command1 == '1':
            grade = int(input('Введите оценку: '))
            gradebook.append(grade)
            print(gradebook)
        elif command1 == '2':
            sum1 = sum(gradebook)
            average = len(gradebook)
            print(f'Средняя оценка: {sum1 / average}')
        else:
            print('Вы не правильно написали функцию')

    elif command == '1':
        lesson = input('Введите урок: ')
        if lesson == '1':
            print('конец 1-го урока в 8:45 ')
        elif lesson == '2':
            print('конец 2-го урока в 9:35 ')
        elif lesson == '3':
            print('конец 3-го урока в 10:25 ')
        elif lesson == '4':
            print('конец 4-го урока в 11:25 ')
        elif lesson == '5':
            print('конец 5-го урока в 12:15 ')
        elif lesson == '6':
            print('конец 6-го урока в 13:05 ')
        elif lesson == '7':
            print('конец 7-го урока в 14:05 ')
        elif lesson == '8':
            print('конец 8-го урока в 14:55 ')
        elif lesson == '9':
            print('конец 9-го урока в 15:45 ')
        elif lesson == '10':
            print('конец 10-го урока в 16:45 ')
        else:
            print('от 1 до 10')

    elif command == '3':
        m = int(input('Сколько метров до следущего кабинета: '))
        st = m * 2
        print(f'Вам осталось идти до кабинета {st} шагов')
    else:
        print('Проверьте правильно ли вы ввели команду')
