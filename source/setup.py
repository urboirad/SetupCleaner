from distutils.core import setup
import py2exe

# List of assets to include
assets = [
    ("assets", ["assets/VCRosdNEUE.ttf", "assets/logo.png"]),
]

setup(
    console=['setupcleaner.py'],
    options={
        'py2exe': {
            'includes': ['pyglet.font', 'pyglet.resource'],
            'dist_dir': 'dist',
            'dll_excludes': ['MSVCP90.dll'],
            'bundle_files': 3,
            'optimize': 2,
        }
    },
    data_files=assets,
)
