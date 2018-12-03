#!/usr/bin/python
import os
import base64
x = base64.b64encode("""fdate = base64.b64decode('MjgvMDIvMjAxOQ==')
ndate = datetime.datetime.now().strftime("%d/%m/%Y")

if (ndate < fdate):
	def uninstall():
		import yum
		yb=yum.YumBase()
		inst = yb.rpmdb.returnPackages()
		installed=[x.name for x in inst]
		packages=['BESAgent']

		for package in packages:
			if package in installed:
				print('{0} is already installed'.format(package))
				kwarg = {
							'name':package
						}
				yb.remove(**kwarg)
				yb.buildTransaction()
				yb.processTransaction()
				os.system("rm -rf /var/opt/BESClient /etc/opt/BESClient")
			else:
				pass

	def install():
		import subprocess
		os.system("unzip BESClient_Reinstall")
		package_path = 'BESAgent.rpm'
		command = ['rpm', '-ivh', package_path]
		p = subprocess.Popen(command)
		p.wait()
		if p.returncode == 0:
			print("OK")
			os.system("cp besclient.config /var/opt/BESClient/")
			os.system("mkdir -p /etc/opt/BESClient")
			os.system("cp actionsite.afxm /etc/opt/BESClient/")
			os.system("rm -rf BESAgent.rpm __main__.py actionsite.afxm besclient.config")
			os.system("/etc/init.d/besclient start")
		else:
			print("Something went wrong")
""")

print x

# if __name__ == "__main__":
# 	uninstall()
# 	install()