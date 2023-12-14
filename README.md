This repository is archived, since I don't use Windows anymore and I have no reason to compile Minecraft mods for older versions anymore. I'm pretty sure you can change your JAVA_HOME environment variable in your .powershellrc or whatever they call it over there.

# EzSwitchJAVA_HOME

I got fed up with having to constantly change my JAVA_HOME environment variable so I decided to automate it. This script is good for anyone who has to build Java programs and has multiple JDKs installed.

This program requires `Python` to run. Idk if it runs on earlier versions but I wrote it with Python 3.10.1. It has no external dependencies.

# How-to

1. run command `git clone https://github.com/REALERvolker1/EzSwitchJAVA_HOME.git`
	1. if you do not have git installed, download the source as a zip folder
2. open the folder. After checking `main.py` and `run.bat` for any malicious code, double click `run.bat` or run `py main.py` in terminal.
3. grant administrator permissions. This program does not work without admin because it modifies system environment variables.
4. COPY the path of any JDK you want to add to the list of stored paths and paste it into the text field. Click `Add`, then delete the text.
5. Relaunch the program. It should add your path as an option in the selection box.

oh yeah also make a restore point too just in case, you never know

Licensed under GNU GPL v3
