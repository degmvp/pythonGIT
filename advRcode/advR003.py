print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advR003
# ✅ Python 3.6 alterado: 2018/07/29
# ✅ Objetivo:Rotina ler arq.txt
# ✅ Comandos:f = open(), with open) as f:,f.readlines()
# ✅ Funções:f.read(size_to_read), open('chips.jpg','rb') as rf:
#-------------------------------------------------''')
print('✅' * 50)

f = open('arq.txt','r')

print(f.name)
print(f)
print(f.mode)
lineH = f.readline()
print(lineH)

f.close()

with open('arq.txt','r') as f:
    f_contents = f.read()
    print(f_contents)
'''
1-) Este é um teste de arquivo txt!
2-) Com multiplas linhas de dados..
3-) Linha tres
4-) Linha quatro
5-) Linha cinco
6-) Linha seis
7-) Linha sete
8-) Linha oito
9-) Linha nove
10) Linha dez
'''
with open('arq.txt','r') as f:
    f_contents = f.readlines()
    print(f_contents)
'''
['1-) Este é um teste de arquivo txt!\n',
 '2-) Com multiplas linhas de dados..\n',
 '3-) Linha tres\n',
 '4-) Linha quatro\n',
 '5-) Linha cinco\n',
 '6-) Linha seis\n',
 '7-) Linha sete\n',
 '8-) Linha oito\n',
 '9-) Linha nove\n',
 '10) Linha dez']
'''
with open('arq.txt','r') as f:
    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')
    
#1-) Este é um teste de arquivo txt!
#2-) Com multiplas linhas de dados..

with open('arq.txt','r') as f:
    for line in f:
        print(line, end='')
     
with open('arq.txt','r') as f:
    size_to_read = 120
    
    f_contents = f.read(size_to_read)
    print(f_contents,end='')

    f_contents = f.read(120)
    print(f_contents,end='')

with open('arq.txt','r') as f:
    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    print('imprime o tamanho da variavel size_to_read : ',f.tell())
    
    while len(f_contents) > 0:
        print(f_contents,end='*')
        f_contents = f.read(size_to_read)

with open('arq.txt','r') as rf:
    with open('arq_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)
'''
with open('chips.jpg','rb') as rf:
    with open('chips_copy.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while  len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
'''
def func_arg(*args,**kwargs):
    print(args)
    print(kwargs)

pro = ['Python','Programação']
dic = {'nome':'Degmar', 'desenvolvedor':'avancado', 'ano ':'2017', 'mes ': 'maio'} 

func_arg(*pro,**dic)
           
