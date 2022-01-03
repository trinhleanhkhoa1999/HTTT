import sys, os
from cx_Freeze import setup, Executable

os.environ["TCL_LIBRARY"] = "<path/to/your/python_directory>/tcl/tcl8.6"
os.environ["TK_LIBRARY"] = "<path/to/your/python_directory>/tcl/tk8.6"

base = None
include_files = [
    "./assets",
    "<path/to/your/python_directory>/DLLs/tcl86t.dll",
    "<path/to/your/python_directory>/DLLs/tk86t.dll"
]

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="MaHoaFile",
    version="1.4",
    description="Ma hoa va giai ma file",
    options={
        "build_exe": {
            "include_files": include_files
            }
    },
    executables=[
        Executable(
            "MaHoaFile.py",
            base=base,
            targetName="MaHoaFile.exe",
            icon="./assets/icon.ico"
        )
    ]
)
