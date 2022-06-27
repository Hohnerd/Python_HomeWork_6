#  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. 
#  приоритет операций стандартный. Функцию eval не использовать!
#  Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
#  Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
#  Пример: 1+2*3 => 7; (1+2)*3 => 9;


import re
 
 
actions = {
  "^": lambda x, y: str(float(x)**float(y)),
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))
}
 
priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
  
def my_eval(expresion: str) -> str:
 
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
 
    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
    return expresion
 
exp = input("Введите арифметическое выражение: ")
print(my_eval(exp)) 
