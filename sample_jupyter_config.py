import IPython
ipython_path = IPython.paths.locate_profile(profile='default')

# Copy start.py to the the folder above

# Read contents of ipython_config.py
try:
    f = open("{:s}/ipython_config.py".format(ipython_path), "r")
    if f.mode == "r":
        contents = f.read()
        print(contents)
except FileNotFoundError:
    f = open("{:s}/ipython_config.py", "w+")
    f.write("Test this module")
    f.close()

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
    # Do something when Jupyter exits
    print("Exiting Jupyter Notebook...")