#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton:
    """一个Python风格的单例模式"""
    def __new__(cls, clsName, *args, **kwargs):
        if not hasattr(cls,'_inst'):
            cls._inst = super().__new__( cls)
        return cls._inst


class SingleSpam(Singleton):
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s



class Borg:
    """Borg惯用法"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state     # 共享对象的__dict__属性. 当对象空间不存在__shared_state时, 会到类空间寻找.
        # self.__dict__=Borg.__shared_state     # 也可以写成
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass

if __name__ == '__main__':
    s1 = SingleSpam('spam')
    s2 = SingleSpam('eggs')
    print (id(s1), s1)
    print (id(s2), s2)

    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'      # rm1, rm2 state为Idle
    rm2.state = 'Running'   # rm1, rm2 state为Running

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'    # rm1, rm2 state为Zombie

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))    #对象为两个不同的对象, id不一样
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = YourBorg()        # 初始化时state为Init

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))

### OUTPUT ###
# rm1: Running
# rm2: Running
# rm1: Zombie
# rm2: Zombie
# rm1 id: 140732837899224
# rm2 id: 140732837899296
# rm1: Init
# rm2: Init
# rm3: Init
