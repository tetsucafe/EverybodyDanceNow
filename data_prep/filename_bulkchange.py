import glob
import os

path = input('frames path: ')
files = glob.glob(path + '*.png')
for f in files:
  os.rename(f, f.replace('_rendered', ''))
