# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")
# ordinary()

class decoclass(object):
    def __init__(self, f):
        self.f = f
    def __call__(self, *args, **kwargs):
        print('start')
        self.f(*args, **kwargs)
        print('end')

@decoclass
def hello(name):
    print("hello {}".format(name))

hello("trung")