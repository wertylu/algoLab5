import os


def read_from_file(file):
    with open(file, 'r') as input_file:
        data = input_file.readlines()
    return data


def write_to_file(result, file_name):
    try:
        os.remove(file_name + ".out")
    except FileNotFoundError:
        pass
    with open(file_name + '.out', "a", ) as f:
        f.write("Pattern match : ")
        for i in range(len(result)):
            f.write(str(result[i]))
            f.write(str(','))
        f.close()
