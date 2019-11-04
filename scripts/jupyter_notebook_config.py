import os
import IPython

ROOT_DIR = os.popen('pipenv --where').read().strip()
# Change Working Directory
c.NotebookApp.notebook_dir = os.path.normpath(os.path.join(ROOT_DIR,"./Docs"))

# Create blank config files
os.system('ipython profile create')
ipython_path = IPython.paths.locate_profile(profile='default')

# Read contents of ipython_config.py
original_content = ''
f = open("{:s}/ipython_config.py".format(ipython_path), "r")
if f.mode == "r":
    original_content = f.read()

# To put ./startup.py into the InteractiveShell's list of startup files
# Edit contents of ipython_config.py as follows:
startup_fullpath = os.path.normpath(os.path.join(ROOT_DIR,'./scripts/startup.py'))
configText = "\n\
if c.InteractiveShellApp.exec_files:\n\
    c.InteractiveShellApp.exec_files.append('{:s}')\n\
else:\n\
    c.InteractiveShellApp.exec_files = ['{:s}']\n\
".format(startup_fullpath, startup_fullpath)

f = open("{:s}/ipython_config.py".format(ipython_path), "a+")
if f.mode == "a+":
    f.write(configText)
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
# exit_register is used to register the post-exit callback function
# In other words, the callback function below is called on Jupyter exit
import os
@exit_register
def callback():
    # Write the original config back when Jupyter exits
    f = open("{:s}/ipython_config.py".format(ipython_path), "w+")
    if f.mode == "w+":
        f.write(original_content)
        f.close()