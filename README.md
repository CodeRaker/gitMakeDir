# gitmakedir quick guide

Start by compiling the file into an exe file (you don't have to, but makes is work nice with PATH).

* `pip install pyinstaller`
* `pyinstaller gitmakedir.py`
* Add the build directory to your PATH (in System Settings 'Advanced' in Control Panel). 
Now you should be able to use the exe as a command, like:
* `gitmakedir myproject`
This will creake the repository `myproject` and clone it into your current directory. The code does not support long paths, just current directory, so make sure to CD into the directory, where you want the folder to be created.