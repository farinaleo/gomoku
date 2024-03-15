#   ------------------------------------------------------------------------------------------------------------------ #
#   contact : leo.farina.fr@gmail.com                                                                 ░▄▄▄▄░           |
#   github : https://github.com/farinaleo                                                             ▀▀▄██►           |
#   date : 3/12/24, 8:27 AM                                                                           ▀▀███►           |
#                                                                                                     ░▀███►░█►        |
#                                                                                                     ▒▄████▀▀         |
#   ------------------------------------------------------------------------------------------------------------------ #
#  Copyright (c) 2024.

import os
import time
import inspect

log = True
first_turn = True
log_file = None
log_source = False
nb_call = 0


def log(to_log=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            """
            Decorator for logging functions.
            """
            global first_turn, log, log_file, nb_call, log_source
            result = func(*args)
            if not log or not to_log:
                return result
            else:
                if first_turn:
                    env_var = os.getenv('GOMOKU_LOG')
                    if env_var == 'True' or env_var == 'ALL':
                        log_file = 'logs/[' + str(time.time()) + '].txt'
                        folder = os.path.dirname(log_file)
                        if env_var == 'ALL':
                            log_source = True
                        if folder:
                            os.makedirs(folder, exist_ok=True)
                    else:
                        log = False
                    first_turn = False
                if log:
                    if log_source:
                        frame = inspect.currentframe()
                        outer_frames = inspect.getouterframes(frame)
                        _, filename, lineno, function_name, _, _ = outer_frames[1]
                    log_msg = f'[{nb_call}] at [{time.strftime("%Y-%m-%d %H:%M:%S")}] call: {func.__name__} ' \
                              f' with args: {args} and kwargs: {kwargs}. result: {result}'
                    log_msg += f' || from {filename}::{function_name} line {lineno}\n' if log_source else '\n'
                    with open(log_file, 'a') as f:
                        f.write(log_msg)
                    nb_call = nb_call + 1
                return result

        return wrapper

    return decorator
