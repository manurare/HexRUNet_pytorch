import sys, _imp
# remove the frozen module
del sys.modules['importlib']._bootstrap
del sys.modules['importlib']._bootstrap_external
del sys.modules['_frozen_importlib']
del sys.modules['importlib._bootstrap']
del sys.modules['importlib._bootstrap_external']
# import the non-frozen module
import importlib._bootstrap
import importlib._bootstrap_external
importlib._bootstrap._install(sys, _imp)
importlib._bootstrap_external._install(importlib._bootstrap)
importlib._bootstrap._bootstrap_external = importlib._bootstrap_external

sys.modules['zipimport']._bootstrap = importlib._bootstrap
sys.modules['zipimport']._bootstrap_external = importlib._bootstrap_external

del sys.modules['importlib.machinery']

from modulefinder import ModuleFinder
import importlib.machinery


file_finder = importlib._bootstrap_external.FileFinder("/home/manuel/Desktop/PHD/code/HexRUNet_pytorch")
spec = file_finder.find_spec("utils")

file_finder = importlib._bootstrap_external.FileFinder("/home/manuel/Desktop/PHD/code/stable-diffusion")
spec2 = file_finder.find_spec("utils")


finder = ModuleFinder()
finder.run_script('just_utils.py')

print("end")