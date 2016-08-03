# http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern
# -written-in-python-the-sample-in-wikipedia
"""
In most of other languages Strategy pattern is implemented via creating some
base strategy interface/abstract class and subclassing it with a number of
concrete strategies (as we can see at
http://en.wikipedia.org/wiki/Strategy_pattern), however Python supports
higher-order functions and allows us to have only one class and inject
functions into it's instances, as shown in this example.
"""
import types


class StrategyExample:
    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)  # 给实例动态添加方法

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


if __name__ == '__main__':
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Strategy Example 1'

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Strategy Example 2'

    strat0.execute()
    strat1.execute()
    strat2.execute()


    # 类动态方法绑定
    class A:
        pass


    def hello(self):
        print('hello')


    # a=A()
    # a.hello=hello
    # # a.hello()       # TypeError: hello() missing 1 required positional argument: 'self'
    # a.hello(1)        # 能执行, 但违背了hello()作为对象方法的本质

    # 方式一, 通过类型(注意: 非实例)来动态添加方法
    A.hello = hello
    a = A()
    a.hello()

    # 方式二, 通过types.MethodType()给实例添加动态方法
    a = A()
    a.hello = types.MethodType(hello, a)
    a.hello()

### OUTPUT ###
# Strategy Example 0
# Strategy Example 1 from execute 1
# Strategy Example 2 from execute 2
