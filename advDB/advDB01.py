print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advDB01
# ✅ Python 3.6 alterado: 2017/11/05
# ✅ Objetivo:lDigite o codigo da Query
# ✅ Comandos:import pypyodbc,SQLCommand,input(query)
# ✅ Funções:connection.cursor(),cursor.execute(SQLCommand),
# ✅         cursor.fetchone(),connection.close()
#-------------------------------------------------''')
print('✅' * 50)
import pypyodbc
SQLCommand = input('Digite o codigo da Query : ' )
connection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=WSRVW10\WSRV17;'
                                'Database=xpydb;'
                                'uid=sa;pwd=rsx45831')
cursor = connection.cursor() 
cursor.execute(SQLCommand)
results = cursor.fetchone()
while results:
    print (results)
    results = cursor.fetchone()
connection.close()
