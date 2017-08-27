from functools import wraps
def api_auth(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        print('decorate_func_'+args[0])
        return func(args[0])
    return decorated_func

@api_auth
def fun(first):
    print('fun_'+first)

if __name__ == '__main__':
    fun("test")