from glob import glob

from pkg_resources import EGG_DIST


def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)