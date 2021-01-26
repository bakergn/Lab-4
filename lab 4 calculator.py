lang = 'EN'
lang_opt = input('Enter L to change language or other key to continue:  ')
while lang_opt == 'l':
    if lang == 'UA':
        lang = 'EN'
        lang_opt = input('Enter L to change language or other key to continue:  ')
    else:
        lang = 'RU'
        lang_opt = input('Введіть L, щоб змінити мову, або будь яку клавішу, щоб продовжити:  ')
if lang == 'EN':
    f = 'Enter first number:  '
    o = 'Enter operation (+,-, /, *):  '
    s = 'Enter second number:  '
    r = 'Result: '
    e = 'Error'
    v = 'Enter "yes" to continue and other key to finish:  '
if lang == 'UA':
    f = 'Введіть перше число:  '
    o = 'Введіть операцію (+,-, /, *):  '
    s = 'Введіть друге число:  '
    r = 'Результат: '
    e = 'Помилка'
    v = 'Введіть "yes", щоб продовжити, або будь яку іншу клавішу, щоб закінчити:  '
continue_calc = 'yes'
while continue_calc== 'yes':
    f_num = float(input(f))
    oper = input(o)
    sec_num = float(input(s))
    if oper == '+':
        print(r, f_num + sec_num)
    elif oper == '-':
        print(r, f_num - sec_num)
    elif oper == '/':
        print(r, f_num / sec_num)
    elif oper == '*':
        print(r, f_num * sec_num)
    else:
        print(e)
    continue_calc = input(v)
