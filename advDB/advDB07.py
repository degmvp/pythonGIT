print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advDB07
# ✅ Python 3.6 alterado: 2018/01/06
# ✅ Objetivo: CRUD SQL SERVER 2016
# ✅ Comandos:DELETE xpy_tb_cook,pyodbc.connect
# ✅ cur.execute, conn.commit()
# ✅ connection.close()
#-------------------------------------------------''')
print('✅' * 50)     
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=WSRVW10\WSRV17;'
                                'Database=xpydb;'
                                'uid=sa;pwd=rsx45831')

cur = conn.cursor() 

#Delete
cur.execute("DELETE from  xpython where xpy_hst = 11")
            
conn.commit()
conn.close() 
