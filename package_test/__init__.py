

def test_init_method1(msg):
    print("test_init_method1:", msg)


if __name__ == '__main__':
    import test1
    import test2
    print(__name__)
    test1.test1method1("from main")
    print("package_test作为主程序运行")
else:
    import package_test.test1
    import package_test.test2
    print(__name__)
    print("package_test初始化")
    # t21("from init")
