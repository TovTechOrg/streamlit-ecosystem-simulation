import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from PIL import Image
from st_clickable_images import clickable_images
import os
from os import listdir
import base64
import pandas as pd
import glob, os
import re
from split_image import split_image
from streamlit_modal import Modal
from datetime import datetime
from streamlit_extras.switch_page_button import switch_page
import streamlit.web.cli as stcli
import sys


if __name__ == "__main__":
    sys.argv=["streamlit", "run", "Simulation1", "--global.developmentMode=false"]
    sys.exit(stcli.main())
