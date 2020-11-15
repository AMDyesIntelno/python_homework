file1_readlines=None
with open("file1.txt","r") as f:
    file1_readlines=f.readlines()
with open("file2.txt","w") as f:
    for i in file1_readlines:
        f.writelines(i[::-1])