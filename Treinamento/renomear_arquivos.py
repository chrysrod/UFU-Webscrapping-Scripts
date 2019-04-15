import os

for diretorio in os.listdir("path"):
	os.chdir("path" + diretorio)
	for item in os.listdir("path" + "\\" + diretorio):
		if ~os.path.isdir(item):
			os.rename(item,item[:len(item)-4]+".jpg")

for diretorio in os.listdir("path"):
	os.chdir("path" + "\\" + diretorio)
	for item in os.listdir("path + "\\" + diretorio):
		if ~os.path.isdir(item):
			os.rename(item,item[:len(item)-4]+".png")