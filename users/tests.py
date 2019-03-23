# Create your tests here.

def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("im inner_wrapper", func, *args, *args)
            return func(*args, **kwargs)

        print("im wrapper", func)
        return inner_wrapper

    print("im logging", level)
    return wrapper


def test_1(test):
    def prints():
        print("words=", test)
        return test()

    print("im test_1", test)
    return prints


def test_2():
    says = "测试参数数据!!!"

    # say = logging(level='INFO')(says)
    def print5():
        print(5555, "1111")

    def print3(aaa):
        def print4(*cccc, **bbb):
            print(44444, cccc[0], "-----", bbb)
            return print5()

        print(3333)
        return print4

    @print3
    def print2(str):
        print(2222, str)

    print("say", says)
    print2(says)
    print("say", says)
