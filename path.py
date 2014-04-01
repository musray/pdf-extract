#import sys, os
#import time
#folder = time.strftime(r"%Y-%m-%d_%H-%M-%S", time.localtime())
#os.makedirs(r'%s/%s' % (os.getcwd(),folder))

# 判断before.pdf和after.pdf文件是否存在
import os

if os.path.exists('after.pdf') and os.path.exists('before.pdf'):
    print "after.pdf has been found"
else:
    print "please put after.pdf file in this derectory"

