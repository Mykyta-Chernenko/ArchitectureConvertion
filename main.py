from decimal import Decimal
ind = 10
from_10 = {x:str(x) for x in range(ind)}
symbol = 'A'
while ord(symbol) <= ord('Z'):
    from_10[ind]= symbol
    symbol = chr(ord(symbol) + 1)
    ind += 1
to_10 = {value:key for key,value in from_10.items()}
def convert(number, convert_from, convert_to,accuracy):
    convert_to = int(convert_to)
    convert_from = int(convert_from)
    if number[0]=='.':
        return f'0.{convert_float(number[1,],convert_from,convert_to)}'
    number_int, number_float = number.split('.')
    return f'{convert_integer(number_int,convert_from,convert_to)}.{convert_float(number_float,convert_from,convert_to)}'


def convert_integer(number, convert_from, convert_to):
    number_10 = 0
    for ind, st in enumerate(number):
        number_10 += to_10[st.upper()] * (convert_from ** (len(number) - 1 - ind))
    lst_to = []
    while number_10 != 0:
        lst_to += [from_10[number_10 % convert_to]]
        number_10 //= convert_to
    lst_to.reverse()
    if len(lst_to) == 0:
        lst_to = ['0']
    return "".join(lst_to)


def convert_float(number, convert_from, convert_to, accuracy=10):
    number_10 = Decimal(0.0)
    for ind, st in enumerate(number):
        number_10 += (to_10[st.upper()] * (Decimal(convert_from) ** (-ind - 1)))
    lst_to = []
    ind = 0
    while number_10 != 0 and ind < accuracy:
        number_10 *= convert_to
        lst_to += [from_10[number_10 // 1]]
        number_10 -= number_10 // 1
        ind += 1
    if len(lst_to) == 0:
        lst_to = ['0']
    return "".join(lst_to)


def check(number, c_from):
    check_lst= [value for key,value in from_10.items() if key < c_from] +['.']
    return all(symbol.upper() in check_lst for symbol in number)

def main():
    while True:
        try:
            while True:
                number = input("Введите исходное число: ")
                c_from = int(input("Введите исходную систему исчесления: "))
                if check(number, c_from):
                    break
                print("Введите корректные данные ")
            c_to = int(input("Введите желаемую систему исчесления: "))
            if '.' in number:
                accuracy = int(input("Введите точность после запятой: "))
                print(convert(number,c_from,c_to,accuracy))
            else:
                print(convert_integer(number,c_from,c_to))
        except:

            print("Введите корректные данные ")

main()
