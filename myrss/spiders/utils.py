def param_transform(arr):
    def decotate(func):
        @functools.wraps(func)
        def check(*args, **kwargs):
            return func(arr.find_all('td'))
        return check
    return 