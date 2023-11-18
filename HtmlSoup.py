'''from clr_loader import get_coreclr
from pythonnet import set_runtime
rt = get_coreclr(runtime_config="D:\\project\\Python\\Login\\Python\\runtimesetting.json")
set_runtime(rt)
import clr
clr.AddReference(".\\dllHtmlSoup.dll")
from dllHtmlSoup import *'''

import clr
import sys
import os

sys.path.append(os.getcwd())
clr.FindAssembly("dllHtmlSoup.dll") 
dll = clr.AddReference("dllHtmlSoup") 
from dllHtmlSoup import * 