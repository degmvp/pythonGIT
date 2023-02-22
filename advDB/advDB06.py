print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advDB06
# ✅ Python 3.6 alterado: 2018/01/06
# ✅ Objetivo: CRUD SQL SERVER 2016
# ✅ Comandos:UPDATE xpy_tbsup_cook,pyodbc.connect
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

#UPDATE
cur.execute("UPDATE xpython set xpy_code ='Pyck01' where xpy_hst = 11")
            
conn.commit()
conn.close() 
