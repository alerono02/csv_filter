import os
from sys import argv
from src.interface import start_script
from src.func import load_data

if __name__ == '__main__':
    path = os.path.abspath(argv[1])
    data = load_data(path)
    print('Formating to DataFrame...')
    start_script(data)

