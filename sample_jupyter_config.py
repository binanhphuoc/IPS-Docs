# try:
#     c = get_config()
# except NameError:
#     print("No get_config")

# c.IPKernelApp.module_to_run = './run.py'

get_ipython().profile_dir.startup_dir

try:
    ip = get_ipython()

    def exit_register(fun, *args, **kwargs):
        """ Decorator that registers at post_execute. After its execution it
        unregisters itself for subsequent runs. """
        def callback():
            fun()
            ip.events.unregister('post_execute', callback)
        ip.events.register('post_execute', callback)
    
except NameError:
    from atexit import register as exit_register

# NameError as a result --> get_ipython does not work here
import os
@exit_register
def callback():
    os.system('echo hello > ./hello.txt')
    print('I\'m done!')