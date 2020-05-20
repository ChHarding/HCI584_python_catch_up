### python interpreter 

<sup>(Note for Chris: run md preview with Control-Shift-v with Markdown Preview Enhanced VS Plugin)</sup>


- python is interpreted
- you need a python interpreter installed to run any python code
- if you installed anaconda, the python interpreter executable ("app") is anaconda3/python.exe (win) or anaconda/bin/python (mac) 
<br />

- the interpreter "eats" code __one line at a time__
- a python script (.py file) or a jupyter python cell can contain multiple lines, which are run/executed/interpreted from top to bottom
- typically a script or cell is run via the IDE (Visual Studio code), possible with a debugger
<br />

- You could also use python in the command line (__terminal__):
    - open a terminal (or use the TERMINAL in VSC)
    - To run a script in the same folder e.g. `hello.py`:
        type `python hello.py` and hit Enter
    - Run a super short literal script (1-liner):
        type `python -c "print('hello')"` and hit Enter
    - Start an interactive session:
        - type 'python` and hit enter
        - you'll see `>>>`, which means the interpreter is waiting for you to type in a line of code (interactive python shell)
        - type `print('hello)'  , then hit return
        - your line is interpreted, the result is shown and it's again ready for another line.
        - this is useful if you want to play around or test something
        - to exit the interactive shell, type `exit()`
<br/>
- byte code files  
    - importing modules can create .pyc files in a local `__pycache__` folder
    - .pyc files are not compiled but rather .py files "compressed" into [bytecode](https://opensource.com/article/18/4/introduction-python-bytecode)
    - bytecode is not human readable but substantially smaller than text
    - it's OK to manually delete `__pycache__` folders, they will be recreated if needed

<!--- Example of running code inside the doc
```python {cmd=true matplotlib=true}
print("hello")
```
-->