## fast IO in python 

from atexit import register
import os 
import sys 
from io import BytesIO

sys.stdin = BytesIO(os.read(0,os.fstat(0).st_size))
sys.stdout = BytesIO()

register(lambda: os.write(1,sys.stdout)) # type: ignore

input = lambda : sys.stdin.readline().rstrip('\n')


