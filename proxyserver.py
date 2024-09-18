import socket
import sys
import threading

#repr- это встроенная функция в Python, которая возвращает формальное(удобное) строковое представление указанного объекта.Выводит либо (str) либо (<str>)
#chr-receives symbol code based(получает символ на основе  кода)
HEX_FILTER = ''.join([(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])   #We connect string(list) using separator...also, if the symbol not printable, then (.),because encoding ASCII

def hexdump(src, length=16, show=True): #show- выведет символ в удобном формате
    if isinstance(src, bytes): # we check whether the object belongs to a certain class(проверяем принадлежность объекта к определенному классу)
        src = src.decode()

    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length]) #the part(часть) of the line to be output
#translate = подставляем вместо каждого символа в необработанной строке его строковое представление
        printable = word.translate(HEX_FILTER)
        heka = "".join([f'{ord(c):02x}' for c in word])
        hexwidth = length*3
        results.append(f"{i:04x} {heka:<{hexwidth}} {printable}")
    if show:
        for line in results:
            print(line)
    else:
        return results


