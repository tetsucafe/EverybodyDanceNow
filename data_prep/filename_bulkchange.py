import glob
import os

path = '/EDN/data/target_frames/'
files = glob.glob(path + '*.png')
for f in files:
  os.rename(f, f.replace('_rendered', ''))
