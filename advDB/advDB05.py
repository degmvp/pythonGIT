print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advDB05
# ✅ Python 3.6 alterado: 2018/01/06
# ✅ Objetivo: xpy_tb_cook SQL SERVER 2016
# ✅ Comandos:INSERT INTO xpy_tbsup_cookdbc,pyodbc.connect
# ✅ cur.execute, conn.commit()
# ✅ connection.close()
#-------------------------------------------------''')
print('✅' * 50)     
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=WSRVw10\WSRV17;'
                                'Database=xpydb;'
                                'uid=sa;pwd=rsx45831')

cur = conn.cursor() 

#CREATE , INSERT , UPDATE, SELECT always use execute command
cur.execute("INSERT INTO xpython(xpy_hst,xpy_descr,xpy_code) VALUES('11','Desempacotar uma sequencia em variaveis separadas','Pyck001')")

            
conn.commit()
conn.close() 
