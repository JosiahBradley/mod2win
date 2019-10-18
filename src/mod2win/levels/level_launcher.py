from mod2win.tools import obf
import sys
from os import path, name as os_name
import subprocess

mod_path = path.dirname(path.dirname(path.abspath(obf.__file__)))


def launch():
    try:
        if os_name.lower() != 'nt':
            subprocess.run(["python", path.abspath(mod_path + f"/levels/level_0{sys.argv[1]}.pyc")], shell=False)
        else:
            subprocess.run(["./venv/Scripts/python", path.abspath(mod_path + f"/levels/level_0{sys.argv[1]}.pyc")], shell=False)
    except FileNotFoundError as e:
        print(f"No level found {e.filename}")
    except Exception as e:
        pass


def scrub():
    for i in range(1, 4):
        in_file = path.abspath(mod_path + f"/levels/level_0{i}.py")
        out_file = path.abspath(mod_path + f"/levels/level_0{i}.b64")
        o = obf.Obf(input_file=in_file, output_file=out_file)
        o.hide()


def restore():
    for i in range(1, 4):
        in_file = path.abspath(mod_path + f"/levels/level_0{i}.b64")
        out_file = path.abspath(mod_path + f"/levels/level_0{i}.py")
        o = obf.Obf(input_file=in_file, output_file=out_file)
        o.unhide()


def _compile():
    for i in range(1, 4):
        in_file = path.abspath(mod_path + f"/levels/level_0{i}.py")
        out_file = path.abspath(mod_path + f"/levels/level_0{i}.pyc")
        o = obf.Obf(input_file=in_file, output_file=out_file)
        o.obf()
