from log_config import py_logger
def optional_introduce():
    def d(x, introduce = False):
        if introduce:
            #print(d.__name__)
            py_logger.debug('str(d.__name__)')
        return x
    return d
a = optional_introduce()
print(a(42, introduce=True))
