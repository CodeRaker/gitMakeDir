# pip install pygithub
# this script expects that settings file exists in C:\Users\<user>\Documents\gitmakedir

import argparse
import os
import sys
from github import Github

# get path to users documents folder to find settings file
def get_settings():
	if os.name == "nt":
		path_to_settings = os.getenv("HOMEPATH")+"\\Documents\\gitmakedir\\settings.txt"
	elif os.name == "posix":
		path_to_settings = os.getenv("HOMEPATH")+"/Documents/gitmakedir/settings.txt"
	else:
		sys.exit("Could not detect OS")
		
	if os.path.exists(path_to_settings):
		with open(path_to_settings, "r") as f:
			for setting in f:
				if not setting.startswith("#"):
					if "git_user" in setting:
						git_user = setting.split("=")[1]
						git_user = git_user.strip("\n ")
					elif "git_password" in setting:
						git_password = setting.split("=")[1]
						git_password = git_password.strip("\n ")
					elif "git_path" in setting:
						git_path = setting.split("=")[1]
						git_path = git_path.strip("\n ")
			try:
				return git_user, git_password, git_path
			except:
				sys.exit("Check your settings file. git_user, git_password and git_path are required.")

	else:
		sys.exit("Sorry! "+path_to_settings+" seems to be missing. Create it and try again.")

# get and verify directory path to create
def get_path():
	argument_parser = argparse.ArgumentParser()
	argument_parser.add_argument('all', nargs='*')
	arguments = argument_parser.parse_args()
	if len(arguments.all) > 1:
		sys.exit("Sorry! Gitmakedir only takes 1 argument. Check your path.")
	else:
		verified_path = arguments.all[0]
		if "/" in arguments.all[0] or "\\" in arguments.all[0]:
			sys.exit("Sorry! Gitmakedir does not traverse paths, please create the dir in the current working directory eg. gitmakedir <folder>")
		if os.path.exists(arguments.all[0]):
			sys.exit("Sorry! Path exists. Please choose a non-existing path.")
	return verified_path

# create and pull repository
def git_create(directory_path, git_user, git_password, git_path):
	try:
		g = Github(git_user, git_password)
		user = g.get_user()
		repo = user.create_repo(directory_path)
	except Exception as e:
		sys.exit("Sorry! Error creating repository. "+str(e))
	try:
		os.system("git clone "+git_path+directory_path+".git")
	except:
		sys.exit("Sorry! Error cloning into repository")
	
def main():
	git_user, git_password, git_path = get_settings()
	directory_path = get_path()
	git_create(directory_path, git_user, git_password, git_path)

main()