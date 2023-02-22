print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advR006
# ✅ Python 3.6 alterado: 2017/11/15
# ✅ Objetivo:Rotina ler arquivo .txt
# ✅ Comandos:import csv, next()
# ✅ Funções :append(),rturn,X[],Y{}
#-------------------------------------------------''')
print('✅' * 50)
import csv

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('csvpy.txt', 'r')
    leitor = csv.reader(arquivo)

    next(leitor)

    for home,como_funciona,contato, comprou in leitor:

        dado = [int(home),int(como_funciona)
            ,int(contato)]
        X.append(dado)
        Y.append(int(comprou))
        print(X)
        print(Y)

    return X, Y
carregar_acessos()
