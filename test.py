import os

path="notebooks/research.ipynb"

print(os.path.split(path)) # it saperates both the dir and file.
dir,file=os.path.split(path)
os.makedirs(dir,exist_ok=True)

with open(path,"w") as f: # write in that dir or file...
	pass