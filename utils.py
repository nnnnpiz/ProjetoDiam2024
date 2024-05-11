import re
import string


#Constates

FICH_BASE_DIR = "C:/Users/pamen/PycharmProjects/PRIMACASA/pastas/"




def groupIn4(x: list):
    out = []
    for n in range(0, len(x), 4):
        out.append(x[n:n + 4])
    return out


def groupIn4Pythonic(x: list):
    return [x[n:n + 4] for n in range(0, len(x), 4)]





