import os
import sys

file_path = os.path.join(os.path.dirname(__file__), '..') 
file_dir = os.path.dirname(os.path.realpath('__file__'))
# print(file_dir)
sys.path.insert(0, os.path.abspath(file_path))
data_dir = os.path.join(file_dir,'Data')# file_dir + '/Data/'
# print(data_dir)
 