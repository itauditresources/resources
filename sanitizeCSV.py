
import os
import re
from tabulate import tabulate


cwd = os.getcwd()

def init() -> None:
    """
    Print user information 
    """

    print('-'*60)
    print('CLI Application to sanitize the delimiter in csv files')
    print('-'*60)
    print(f'CWD: {cwd}')
    print('-'*60)
    
    table_information = [['Parameter', 'Description', 'Value'], 
    ['Path', 'Provide the file path', '/file.csv or C:/.../file.csv'], 
    ['Flag', 'Absolute or relative path', 'a or r'],
    ['Delimiter', 'Delimiter used in csv file', 'semicolon']]

    print(tabulate(table_information, headers='firstrow', tablefmt='grid'))

    print('\n')

    check_file_path()


def get_file_path() -> str:
    """
    Get either the relative or absolute file path as a character string
    """

    while True:
        try:

            file_path = str(input('File Path: '))
            path_flag = str(input('Absolute or relative path: '))

            if not isinstance(file_path, str):
                raise TypeError('File path needs to be a string')

            if not re.match('', file_path):
                raise ValueError('Provide a valid file name')

            if len(file_path) == 0:
                raise ValueError('Provide a file path')

            if path_flag not in ['a', 'r']:
                raise ValueError('Provide a valid flag (a or r)')

            if path_flag == 'a':
                if not os.path.exists(file_path):
                    raise FileNotFoundError('No file found')

            if path_flag == 'r':
                if not os.path.exists(f'{cwd}\{file_path}'):
                    raise FileNotFoundError('No file found')
        

        except (TypeError, ValueError, FileNotFoundError) as e:
            print(e)

        else:
            break


    if path_flag == 'a':
        return file_path
    else:
        return f'{cwd}\{file_path}'


def check_file_path() -> tuple:
    """
    Check if a file exists and return the name and file extension 
    """

    file_path = get_file_path()

    with open(file=file_path, mode='r+') as file:
        lines = file.readlines()

        last_letter = False
        s = []
        t = []

        for line in lines:
            for letter in line:

                if letter == ';':
                    last_letter = True

                if last_letter and letter == ';':
                    s.append(letter)

                if last_letter and not letter == ';':
                    last_letter = 0

            t.append(letter)

        print(s)  
        print(t)  


                    


if __name__ == '__main__':

    init()