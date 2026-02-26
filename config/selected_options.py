import json
import os
from config.browser_options import OPTION_MAP

CONFIG_PATH= os.path.join(os.path.dirname(__file__),"selectbrowseroptions.json")

def load_selected_options():
    print(CONFIG_PATH)
    with open(CONFIG_PATH,"r")as f:
        return json.load(f)
SELECTED_OPTIONS=load_selected_options()
#print("Loaded selected options",SELECTED_OPTIONS)





