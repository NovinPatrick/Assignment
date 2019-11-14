from src.cal import tan_func
import sys
import logging
logging.basicConfig(filename='tan_error.log',level=logging.INFO,format='%(name)s - %(levelname)s - %(message)s')

def main():
    try:
        value = int(sys.argv[1])
        result = tan_func.tan_fun(value)
        print(result)
    except ValueError as e:
        logging.debug(e.message)
    except TypeError as e:
        logging.debug(e.message)
    except Exception as e:
        logging.debug(e.message)
