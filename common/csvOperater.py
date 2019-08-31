import csv
import os


def reader(file_name):
    path = os.path.join(os.path.dirname(os.getcwd()), "data", file_name)
    with open(path, 'r') as file:
        table = csv.reader(file)
        ls = []
        for index, row in enumerate(table):
            if index == 0:
                pass
            else:
                ls.append(row)
    return ls


if __name__ == '__main__':
    l = reader("login.csv")
    print(l)
