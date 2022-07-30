
import os
import getpass
import pickle


USERNAME = getpass.getuser()
PATH = f'C:\Users\{USERNAME}\Desktop\\Роман\так\Новый текстовый документ.txt'


def resetpath():
    ffffpath = f'C:\Users\{USERNAME}\Desktop\\ffff.txt'

    with open(ffffpath, 'r') as f:
        path = f.read()
    with open(PATH, 'wb') as f:
        pickle.dump(path, f)
    return path


def getpath():

    with open(PATH, 'rb') as f:
        try:
            resp = pickle.load(f)
        except:
            resp = None
        if not resp:
            resp = resetpath()
        return resp


def add_to_startup(file_path: str=None):
    if file_path == None:
        return
    bat_path = rf'C:\Users\{USERNAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        # print('add')
        bat_file.write(r'start "" %s' % file_path)


if __name__ == '__main__':
    add_to_startup(getpath())
