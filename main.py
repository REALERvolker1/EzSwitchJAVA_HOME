from tkinter import *
from os import system, environ
import ctypes, sys
import win32con
from win32gui import SendMessage
from winreg import (CloseKey, OpenKey, QueryValueEx, SetValueEx, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE,KEY_ALL_ACCESS, KEY_READ, REG_EXPAND_SZ, REG_SZ)

def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False
if is_admin() == False:
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
	exit()
def checkFile():
	try:
		return open('paths.txt',"rt")
	except:
		tempPath = open('paths.txt',"wt")
		tempPath.write("select...")
		tempPath.close()
		return open('paths.txt',"rt")
pathz = checkFile()
paths = pathz.read().split("\n")
pathz.close
print(paths)
root = Tk()
root.wm_title("Switch JAVA path")
root.geometry("300x150")
#selected_var = ""
def savePath():
	val = pathBox.get()
	pathf = open('paths.txt','a')
	pathf.write("\n" + val)
	print(f"{val} saved in paths. Please restart the program at your earliest convenience.")
	#selBox.option_add(val, val)
	pathf.close()
def updateSel(sel):
	global selected_var
	selected_var = sel
	#print(selected_var)
def setHome():
	print(f"Setting JAVA_HOME to {selected_var}")
	subkey = 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
	#command = f"set JAVA_HOME={selected_var}"
	key = OpenKey(HKEY_LOCAL_MACHINE, subkey, 0, KEY_ALL_ACCESS)
	SetValueEx(key, "JAVA_HOME", 0, REG_SZ, selected_var)
	SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
	
desc = "Add a new java install by pasting its file PATH to the \nfollowing textbox. After that, RELOAD the application."
instr = "Select which Java path you want to use from the list."
selected = StringVar(root)
selected.trace_add('write', lambda *paths: updateSel(selected.get().strip()))
selected.set(paths[0])

pathText = Label(root, text=desc, justify=LEFT)
pathText.place(x=10,y=10)
pathBox = Entry(width=30)
pathBox.place(x=10,y=50)
pathSave = Button(root, text="Add", command=savePath)
pathSave.place(x=200,y=45)

selText = Label(root, text=instr, justify=LEFT)
selText.place(x=10,y=70)
selBox = OptionMenu(root, selected, *paths)
selBox.place(x=10,y=90)
selButton = Button(root, text="SET JAVA_HOME", command=setHome)
selButton.place(x=10,y=120)
root.mainloop()