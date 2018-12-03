from shutil import copyfile, make_archive, move, rmtree
from app import upload_path
from zipfile import ZipFile
from flask import url_for
import os, time

def mcopy():
	os.chdir(os.path.dirname(__file__))
	copyfile("static/py/__main__.py", upload_path+"__main__.py")

def build():
	# zf = zipfile.ZipFile("static/py/myzipfile.zip", "w")
	# for dirname, subdirs, files in os.walk(upload_path):
	#     # zf.write(dirname)
	#     zf.write(files)
	#     # for filename in files:
	#     #     zf.write(os.path.join(dirname, filename))
	# zf.close()
	# make_archive('static/py/BESClient_Reinstall', 'zip', os.path.basename(upload_path+"__main__.py"))
	
	time.sleep(1)
	os.chdir(upload_path)
	with ZipFile("BESClient_Reinstall","w") as zip:
		zip.write("__main__.py")
		zip.write("BESAgent.rpm")
		zip.write("actionsite.afxm")
		zip.write("besclient.config")
	os.chdir(os.path.dirname(__file__))
	move(upload_path+"BESClient_Reinstall",os.path.dirname(__file__)+"/static/public/BESClient_Reinstall")
	for filename in os.listdir(upload_path):
		os.unlink(upload_path+filename)
	# os.system("zip static/py/BESClient_Reinstall "+upload_path+"__main__.py")