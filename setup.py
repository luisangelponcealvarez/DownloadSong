from distutils.core import setup
import py2exe

setup(
    windows=[{
        "script": "app.py",
    }],
    options={
        "py2exe": {
            "bundle_files": 1,
            "compressed": True,
            "dll_excludes": ["MSVCP90.dll"]
        }
    },
    zipfile=None
)