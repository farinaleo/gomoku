import os
import time

log = True
first_turn = True
log_file = None
nb_call = 0


def log(to_log=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            """
            Decorator for logging functions.
            """
            global first_turn, log, log_file, nb_call
            result = func(*args)
            if not log or not to_log:
                return result
            else:
                if first_turn:
                    env_var = os.getenv('GOMOKU_LOG')
                    if env_var == 'True':
                        log_file = 'logs/[' + str(time.time()) + '].txt'
                        folder = os.path.dirname(log_file)
                        if folder:
                            os.makedirs(folder, exist_ok=True)
                    else:
                        log = False
                    first_turn = False
                if log:
                    log_msg = f'[{nb_call}] at [{time.strftime("%Y-%m-%d %H:%M:%S")}] call: {func.__name__} ' \
                                f' with args: {args} and kwargs: {kwargs}. result: {result} \n'
                    with open(log_file, 'a') as f:
                        f.write(log_msg)
                    nb_call = nb_call + 1
                return result
        return wrapper
    return decorator
