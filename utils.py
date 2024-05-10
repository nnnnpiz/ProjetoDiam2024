import re
import string


#Constates

FICH_BASE_DIR = "C:/Users/pamen/PycharmProjects/PRIMACASA/pastas/"


def transformar_em_tel(tel_str: str):
    return int(re.sub('\s+', '', tel_str))


def groupIn4(x: list):
    out = []
    for n in range(0, len(x), 4):
        out.append(x[n:n + 4])
    return out


def groupIn4Pythonic(x: list):
    return [x[n:n + 4] for n in range(0, len(x), 4)]


def handle_uploaded_file(diretory: str, filename: str, file):
    with open(f'{diretory}/{filename}', "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def pass_tem_requisitos(password: str)-> bool:
    def tem_maiscula(password: str)-> bool:
        for chr in password:#ver se tem uma maiscula
            if(chr in string.ascii_uppercase):
                return True
        return False
    def tem_minuscula(password: str)-> bool:
        for chr in password:#ver se tem uma minuscula
            if(chr in string.ascii_lowercase):
                return True
        return False
    def tem_numero(password: str)-> bool:
        for chr in password:#ver se tem uma minuscula
            if(chr in "1234567890"):
                return True
        return False
    return tem_minuscula(password) and tem_numero(password) and tem_maiscula(password) and len(password) >=10

print(pass_tem_requisitos('A1a'),pass_tem_requisitos('1a'),pass_tem_requisitos('Aa'),pass_tem_requisitos('A1'),sep='\n')

