print('✅' * 50)
print('''
--------------------------------------------------
# ✅ binN01
# ✅ Python 3.6 alterado: 2017/11/12
# ✅ Objetivo:operação Bitwise
# ✅ Comandos:operadorres & |  and or
# ✅ Funções:class User
#-------------------------------------------------''')
print('✅' * 50)
a = 5 #bits = 101

b = 4 #bits = 100

def print_dec_and_bits(value):
    print('Dec: {:d} | bits {:3b}'.format(value, value))

c = a | b # --> Bits 100

print_dec_and_bits(c) #Dec: 5 | bits 101

print('User rigths.........')

view   = 1  # bits 001

edit   = 2  # bits 010

create = 4  # bits 100

class User:
    def __init__(self, rights):
        self.rights = rights

    def can_view(self):
        return view & self.rights

    def can_edit(self):
        return edit & self.rights

    def can_create(self):
        #print(create & self.rights,'valor de create')
        return create & self.rights


viewer  = User(view)
editor  = User(view | edit)
creator = User(view | edit | create

if viewer.can_view():    
              print('sim, viewer pode ver!')
else:
              print('não, viewer não pode ver!')

if editor.can_view():
              print('sim, editor pode ver!')
else:
              print('não, editor não pode ver!')

if creator.can_view():
              print('sim, creator pode ver!')
else:
              print('não, creator não pode ver!')
#--------------------------------------------------

if viewer.can_edit():
              print('não, viewer pode editar!')
else:
              print('não, viewer não pode editar!')

if editor.can_edit():
              print('sim, editor pode editar!')
else:
              print('não, editor não pode editar!')

if creator.can_edit():
              print('sim, creator pode editar!')
else:
              print('não, creator não pode editar!')
              

if viewer.can_create():
              print('sim, viewer pode create!')
else:
              print('não, viewer não pode create!')

if editor.can_create():
              print('sim, editor pode create!')
else:
              print('não, editor não pode create!')

if creator.can_create():
              print('sim, creator pode create!')
else:
              print('não, creator não pode create!')

