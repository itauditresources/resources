#!usr/bin/python

from glob import glob
import os
import re

forwardSlash = '/'
backSlash = '\\'

cwd = os.getcwd()


def init() -> None:
    """
    Print user information 
    """
    print('-'*50)
    print('Slash inverter version 0.0.1')
    print('-'*50)
    print(f'Current working directory: {cwd}\\')
    print('-'*50)

    print(checkSlash())


def getFileName() -> str:
    """
    Request the data files and perform error handling
    """

    while True:

        try: 
            file_name = str(input('Name of the file: '))


            if not isinstance(file_name, str):
                raise TypeError('The file name needs to be a string')

            if len(file_name) == 0:
                raise ValueError('Provide a file name')

            if not re.match('[a-z]+', file_name):
                raise ValueError('Provide a valid file name')

            if not glob(cwd + '/' + file_name, recursive=True):
                raise FileNotFoundError(f'File not found in {cwd}')

        
        except TypeError as e:
            print(e)

        except ValueError as e:
            print(e)

        except FileNotFoundError as e:
            print(e)

        else:
            break

    return file_name


def getPath() -> str:
    """
    Get the physical file 

    Could be extended to change file contents
    """

    file_name = getFileName()

    path = f'{cwd}\\{file_name}'

    return path


def checkSlash() -> str:
    """
    Check for the most common type of slashes in a string
    Invert that slash
    """

    path = getPath()
    fSCount = 0
    bSCount = 0

    for letter in path:

        if letter == forwardSlash:
            fSCount = fSCount + 1

        if letter == backSlash:
            bSCount = bSCount + 1
    


    if fSCount > bSCount:
        path_sanitized = str.replace(path, '/', '\\')

    else:
        path_sanitized = str.replace(path, '\\', '/')


    return path_sanitized


if __name__ == '__main__':

    init()
