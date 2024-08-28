import subprocess
import sys

# List of packages to check and install if necessary
required_packages = [
    'filetype',
    'PIL', 
    'mutagen',
    'librosa'
]

# Define install_and_import function
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

# Excecution Block
for package in required_packages:
    install_and_import(package)
