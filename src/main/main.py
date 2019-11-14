from src.cal import tan_func
import sys


def main():
    value = int(sys.argv[1])
    result = tan_func.tan_fun(value)
    print(result)
