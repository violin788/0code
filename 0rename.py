import os,sys
cwd = os.getcwd()
files = os.listdir(cwd)
#print(files)
"""
iden=[]
iden.append([".jpg","sta"])
iden.append([".png","sta"])
iden.append([".mp4","dyn"])
"""
find = "-history"
new_val = ""

for file in files:
    if find in file:
        print(file)
        os.remove(file)
        continue
        """
        old_name = file
        new_name = old_name.replace(find,new_val)
        try:
            os.rename(old_name, new_name)   
        except:
            continue
        #sys.exit()
        """
