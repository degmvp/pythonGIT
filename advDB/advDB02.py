print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advDB02
# ✅ Python 3.6 alterado: 2018/05/31
# ✅ Objetivo:Executando view view V$_xpy_tb_objproc
# ✅ Comandos:import pypyodbc,SQLCommand,input(query)
# ✅ Funções:connection.cursor(),cursor.execute(SQLCommand),
# ✅         cursor.fetchone(),connection.close()
#-------------------------------------------------''')
print('✅' * 50)     
import pyodbc
connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=WSRVW10\WSRV17;'
                                'Database=xpydb;'
                                'uid=sa;pwd=rsx45831')
cursor = connection.cursor() 
              
cursor.execute("SELECT *  FROM XPYDB.dbo.V$_xpy_tb_objproc")

results = cursor.fetchone()
while results:
    print (results)
    results = cursor.fetchone()

print ("\n\nComplete.")

# Close and delete cursor
cursor.close()
del cursor

# Close Connection
connection.close()
