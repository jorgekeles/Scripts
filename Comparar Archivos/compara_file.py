import filecmp
import shutil 
import os

a= filecmp.cmp('Juniper_post_ROA1.CBC1.txt', 'Juniper_pre_ROA1.CBC1.txt', shallow=False) 
print(a)