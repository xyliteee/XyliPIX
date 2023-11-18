import subprocess

def ui2py(filename):
    cmd = f"pyuic5.exe {filename}.ui -o Ui_{filename}.py"
    subprocess.call(cmd,shell= True)
def qrc2py(filename):
    cmd = f"pyrcc5.exe {filename}.qrc -o {filename}_rc.py"
    subprocess.call(cmd,shell= True)

ui2py("LoginPage")
ui2py("DetailsPage")
ui2py("DiscoveryPage2")
ui2py("SettingPage")
ui2py("PicSearchPage")
ui2py("DownloadPage")
ui2py("UserSearchPage")
#qrc2py("Img")