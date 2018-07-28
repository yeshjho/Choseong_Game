from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], includes = ["sys", "PyQt5", "time", "threading", "random"], include_files = ["GUI.ui", "ChoseongPic/", "Play.png", "Rule.png", "wheel.png", "Option.ui", "Rule.ui", "text.txt", "bscore.txt", "misc.txt"])
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
executables = [
    Executable('Main.py', base=base)
]
setup(
    name='ChoSeong Game',
    version = '1.0',
    description = 'A PyQt Word Game',
    options = dict(build_exe = buildOptions),
    executables = executables
)