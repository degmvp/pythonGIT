print('✅' * 50)
print('''
#-------------------------------------------------------
# ✅ advR007
# ✅ Python 3.6 alterado: 2018/07/29
# ✅ Objetivo:cmd avançado imprime formato table
# ✅ Comandos:LEFT,RIGHT,COLUMNS
# ✅ Funções :getrow,getrows()
#-------------------------------------------------------''')
print('✅' * 50)
class ALIGN:
    LEFT, RIGHT = '-', ''

class Column(list):
    def __init__(self, name, data, align=ALIGN.RIGHT):
        list.__init__(self, data)
        self.name = name
        width = max(len(x) for x in data + [name])
        self.format = ' %%%s%ds ' % (align, width)

class Table:
    def __init__(self, *columns):
        self.columns = columns
        self.length = max(len(x) for x in columns)
    def get_row(self, i=None):
        for x in self.columns:
            if i is None:
                yield x.format % x.name
            else:
                yield x.format % x[i]
    def get_rows(self):
        yield '|'.join(self.get_row(None))
        for i in range(0, self.length):
            yield '|'.join(self.get_row(i))

    def __str__(self):
        return '\n'.join(self.get_rows())   

def test():
    nums = [ '1', '2', '3', '4' ]
    speeds = [ '100', '10000', '1500', '12' ]
    desc = [ '', 'label 1', 'none', 'very long description' ]
    print('-' * 40)
    print (Table(
        Column('NUM', nums),
        Column('SPEED', speeds),
        Column('DESC', desc, align=ALIGN.LEFT)))
    print('-' * 40)
test()
