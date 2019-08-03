# gitmakedir quick guide

Start by compiling the file into an exe file (you don't have to, but makes is work nice with PATH).

On Windows:
* `pip install pyinstaller`
* `pyinstaller gitmakedir.py`
* Add the build directory to your PATH (in System Settings 'Advanced' in Control Panel). 
Now you should be able to use the exe as a command, like:
* `gitmakedir myproject`
This will creake the repository `myproject` and clone it into your current directory. The code does not support long paths, just current directory, so make sure to CD into the directory, where you want the folder to be created.

On MacOS or Linux:
* Add the path to `gitmakedir.py` in your bash_profile as an alias
* Create a new repository and clone into with `gitmakedir myproject`
This will creake the repository `myproject` and clone it into your current directory. The code does not support long paths, just current directory, so make sure to CD into the directory, where you want the folder to be created.