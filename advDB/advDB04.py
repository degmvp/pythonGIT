print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advDB04
# ✅ Python 3.6 alterado: 2018/01/06 -  SQL SERVER 2016
# ✅ Objetivo:Localiza qualquer string dentro de objetos]
# ✅ Comandos:import pypyodbc.connect
# ✅ --tipos validos
# ✅   C = Check Constraint
# ✅   D = Default
# ✅  FN = Function
# ✅   P = Procedure
# ✅  TR = Trigger
# ✅   V = View
# ✅Parametros:Texto a pesquisar,flag 'C,D,FN,P,TR,V)   
#-------------------------------------------------''')
print('✅' * 50)
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=WSRVW10\WSRV17;'
                              'Database=xpydb;'
                                'uid=sa;pwd=rsx45831')

cur = conn.cursor()

cur.execute('dbo.[xprc_seek] banco,p')

row = cur.fetchone()

while row:
      #Index column fields in database always from 0
      print (row[0])
      row = cur.fetchone()
conn.commit()
conn.close() 
