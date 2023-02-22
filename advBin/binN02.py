print('✅' * 50)
print('''
--------------------------------------------------
# ✅ binN02
# ✅ Python 3.6 alterado: 2017/11/12
# ✅ Objetivo:operação Bitwise
# ✅ Comandos:operadorres & |  and or
# ✅ Funções:class User
#-------------------------------------------------''')
print('✅' * 50)
import pyodbc
connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=WSRVW10\WSRV17;'
                                'Database=xpydb;'
                                'uid=sa;pwd=rsx45831')
cursor = connection.cursor() 
SQLCommand = ("SELECT [idbin],[hexa_pos],[val_pos]\
  FROM [XPYDB].[dbo].[bits]")

cursor.execute(SQLCommand)
results = cursor.fetchone()
while results:
    print (" " +  str(results[0]) + "      " + results[1] + "      " + results[2] + "     " + str(results[3]))
    results = cursor.fetchone()

print('✅' * 50)
print('✅' * 50)
'''
SQLCommand = ("select atributo,vmask from [dbo].[tb_mask]")

cursor.execute(SQLCommand)
results = cursor.fetchone()
while results:
    print (" " +  str(results[0]) + "      " + str(results[1]))
    results = cursor.fetchone()

    
print ("\n\nComplete.")
# Close and delete cursor
cursor.close()
del cursor
'''
# Close Connection
connection.close()
