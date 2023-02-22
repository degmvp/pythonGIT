print('✅' * 50)
print('''
--------------------------------------------------
# ✅ advDB03
# ✅ Python 3.6 alterado: 2018/31/05
# ✅ Objetivo:Cria tabela xpy_tb_cook SQL SERVER 2016
# ✅ Comandos:import pyodbc,pyodbc.connect
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

#CREATE 
cur.execute('CREATE TABLE xpython([xpy_hst] [smallint]not NULL,[xpy_descr] [varchar](max) NULL,[xpy_code] [char](15) NULL)')
cur.execute('ALTER TABLE [dbo].[xpython] ADD  CONSTRAINT [PK_xpy_hst] PRIMARY KEY CLUSTERED([xpy_hst] ASC)')
            
conn.commit()
conn.close()
