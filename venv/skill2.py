import shutil
from shutil import copyfile
source=input("enter file path:")
destination=input("enter path:")
shutil.copy(source,destination)
print("successfully")