import os


def dnafiles(file):
    alter_not = open(file)

    data = (alter_not.read())

    dnalist = (data.split('\n'))

    alter_not.close()

    return dnalist


def soldier(apath, afile, ext):
    file = afile

    path = apath

    os.chdir(path)

    i = 0

    var = dnafiles(file)

    for f in os.listdir():

        f_name, f_ext = os.path.splitext(f)

        if f_ext == f'.{ext}':
            newname = f'{str(i)}{f_ext}'

            i += 1

            os.rename(f, newname)

            continue

        if f_name not in var:
            nn = f_name.capitalize()

            new_name = f'{nn}{f_ext}'

            os.rename(f, new_name)


if __name__ == '__main__':
    path = input('Enter Path Name:')

    file = input('Enter File Name Which Contain Name Of Files Not TO Alter: ')

    ext = input('Enter Extension/Formate: ')

    soldier(path, file, ext)
