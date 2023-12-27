def higher_order(func):
    print('Получена функция {} в качестве аргумента'.format(func))
    func()
    print('fff')
    return func


@higher_order
def hello_world():
    print('Hello world!')



