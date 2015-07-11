from django.conf import settings
import time

def log_time(fun):
    def _inner(*args, **kwargs):
        if not settings.SHOW_PERFORM:
            return fun(*args, **kwargs)
        start_time = time.time()
        result = fun(*args, **kwargs)
        delta = time.time() - start_time
        print '\033[93m' +  "%s => %2.4f" % (fun.__name__, delta) + '\033[0m'
        return result
    return _inner
