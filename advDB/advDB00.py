print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advDB00
# ✅ Python 3.6 alterado: 2017/11/05
# ✅ Objetivo:Le x1tb_obj_proc tabela SQL SERVER 2014
# ✅ Comandos:import pypyodbc,SQLCommand
# ✅ Funções:connection.cursor(),cursor.execute(SQLCommand),
# ✅         cursor.fetchone(),connection.close()
#-------------------------------------------------''')
print('✅' * 50)
import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=WSRVW10\WSRV17;'
                                'Database=xpydb;'
                                'uid=sa;pwd=rsx45831')
cursor = connection.cursor() 
SQLCommand = ("SELECT * FROM bits")

cursor.execute(SQLCommand)
results = cursor.fetchone()
while results:
    print ( results)
    results = cursor.fetchone()

print ("\n\nComplete.")
# Close and delete cursor
cursor.close()
del cursor

# Close Connection
connection.close()


