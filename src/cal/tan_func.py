'''math module includes all the mathematical functions'''
import math
import logging

logging.basicConfig(filename='tan_error.log',level=logging.INFO,format='%(name)s - %(levelname)s - %(message)s')


def tan_fun(inp1):
    '''check for the tangent value of a number'''
    try:
        inp1 += 0
    except TypeError as t:
        logging.debug(t.message)
    else:
        tan_f = math.tan(int(inp1))
        r_tan_f = round(tan_f, 9)
        return r_tan_f
