print('✅' * 50)
print('''
--------------------------------------------------
# ✅ binN03
# ✅ Python 3.6 alterado: 2017/11/12
# ✅ Objetivo:operação Bitwise
# ✅ Comandos:operadorres & |  and or
# ✅ Funções:class User
#-------------------------------------------------''')
print('✅' * 50)
import pyodbc
connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=WINSRV14\WSRV14;'
                                'Database=xpydb;'
                                'uid=sa;pwd=rsx45831')
global x
print('## 1- quem comprou carro ?')
print('-' * 76)
cursor = connection.cursor() 
SQLCommand = ("SELECT cfirst,clast,car,OptionsMask \
FROM dbo.COrders WHERE OptionsMask & 1 = 1") 

cursor.execute(SQLCommand)
results = cursor.fetchone()
while results:
    print (" " +  str(results[0]) + "      " + results[1] + "      " + results[2] + "     " + str(results[3]))
    results = cursor.fetchone()

print('✅' * 50)
print('✅' * 50)
    
print ("##Informe o analitico da compra!")
x = int(input('Numero da mascara -->: '))

cursor = connection.cursor() 
SQLCommand = ("declare @v int \
set @v = 51\
select @v & bin_val as bitwise,idbin as [Bit_Pos],descrição from bits \
where @v & bin_val = bin_val")

cursor.execute(SQLCommand)
results = cursor.fetchone()
while results:
    print (" " +  str(results[0]) + "      " + str(results[1]) + "      " + str(results[2]))
    results = cursor.fetchone()

cursor.close()
del cursor

# Close Connection
connection.close()

