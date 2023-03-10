print('✅' * 50)
print('''
#---------------------------------------
# ✅ AppB04
# ✅ Python 3.6 alterado: 2017/08/13
# ✅ Objetivo: decorator-->Caches a function's return
#---------------------------------------''')
print('✅' * 50)
import collections
import functools


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


@memoized
def fat(n):
    i = 1
    fat = 1
    while i <= n:
        fat = fat * i
        i += 1
        print('Fatorial(%d) = %d' % (n, fat))
    return n


print(fat(10))