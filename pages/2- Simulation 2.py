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


# defining the modal a component that is responsible for popup messages
modal = Modal(key="Demo Key",title="Is the Ecosystem Sustainable?")

# Comparing two lists to see if the values match even if not in order
def check_if_equal(list_1, list_2):
    """ Check if both the lists are of same length and if yes then compare
    sorted versions of both the list to check if both of them are equal
    i.e. contain similar elements with same frequency. """
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

# sorting a list by number or alphabetha
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# configuring the streamlit page layout as wide
st.set_page_config(layout="wide", page_title="Ecosystem_Management_Simulation")



with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:



    # creating a function to cache the read excel data
    @st.cache_data
    def load_file(path):
        file_df = pd.read_csv(path)
        return file_df

    # creating a function to cache the images from directory to a list
    @st.cache_data
    def img2list(path):
        folder_dir = path
        img_list = []
        for images in os.listdir(folder_dir):
            # check if the image ends with png
            if (images.endswith(".png")):
                img_list.append(images)
        img_list = sorted(img_list, key=numericalSort)
        return img_list    

    # reading the for refrence csv to df
    for_refrence = load_file("./simulation_2/for_refrence.csv")

    # defining numbers
    numbers = re.compile(r'(\d+)')

    #creating an enpty list 
    image_list = []

    # reading the big split picture and the plants and animals pictures into lists
    image_list = img2list("./simulation_2/split_photo")
    sim2_plants = img2list("./simulation_2/plants")
    sim2_animal = img2list("./simulation_2/animals")



    # if the real_img list not in the sessions state then create a new list with the pictures from the split photo encoded
    if 'real_img_list2' not in st.session_state:
        st.session_state['real_img_list2'] = []
        for file in image_list:
            with open("./simulation_2/split_photo//" + file, "rb") as image:
                encoded = base64.b64encode(image.read()).decode()
                st.session_state['real_img_list2'].append(f"data:image/jpeg;base64,{encoded}")

    # add list to the sessions state( a list of selected species)
    if 'list2' not in st.session_state:
        st.session_state['list2'] = []

    # making sure list is never None
    if st.session_state.list2 is None:
        st.session_state['list2'] = []

    # adding the sim2_animal list of images to the sesssion state
    if 'animals2' not in st.session_state:
        st.session_state['animals2'] = sim2_animal

    # adding the sim2_plants list of images to the sesssion state
    if 'plants2' not in st.session_state:
        st.session_state['plants2'] = sim2_plants

    # defining a function to cache the images data as st.image
    @st.cache_data
    def image_load(path, image_name):
        with Image.open(path + str(image_name)) as img:
            st.image(img)

    # creating the side bar with two tabs
    with st.sidebar:
        planet, animal = st.tabs(['Producers','Animals'])   

    # in plants for every image in 'plants' create two columns one with an expander that contains the image and the other with an add button
    # when the add button is pressed add the plant name to the list of species
    with planet:
            for image in st.session_state['plants2']:
                    col1, col2 = st.columns([3,1])
                    with col1:
                        with st.expander(str(image)[:-4]):
                            image_load('./simulation_2/plants/', image)
                    with col2:
                        if st.button('Add', key= str(image)[:-4]):
                            if len(st.session_state.list2) < 8 :
                                if str(image)[:-4] not in st.session_state.list2:
                                    st.session_state.list2.append(str(image)[:-4])

    # in plants for every image in 'animals' create two columns one with an expander that contains the image of the animal and the other with an add button
    # when the add button is pressed add the animal name to the list of species
    with animal:
            for image in st.session_state['animals2']:
                    col1, col2 = st.columns([3,1])
                    with col1:
                        with st.expander(str(image)[:-4]):
                            image_load('./simulation_2/animals/', image)
                    with col2:
                        if st.button('Add', key= str(image)[:-4]):
                            if len(st.session_state.list2) < 8 :
                                if str(image)[:-4] not in st.session_state.list2:
                                    st.session_state.list2.append(str(image)[:-4])

                
    # define two columns to split the main container
    left, right = st.columns([3.5,1], gap='large')

    #writing the headlins and instructions
    with left:  
        multipage_1, multipage_2, multipage_3 = st.columns(3)
        with multipage_1:
            page1 = st.button("Simulation 1")
            if page1:
                switch_page("Simulation1")
        with multipage_2:
            page1 = st.button("Simulation 2", type='primary')
            if page1:
                switch_page("Simulation 2")
        with multipage_3:
            page1 = st.button("Simulation 3")
            if page1:
                switch_page("Simulation 3")
        st.markdown("<h2 style='text-align: left; color: grey;'>Ecosystem Management - Simulation 2</h2>", unsafe_allow_html=True)
        st.markdown('---')
        st.markdown("<h4 style='text-align: left; color: grey;'>Instructions</h4>", unsafe_allow_html=True)

        #instructions text goes here
        st.caption("""Move through the cells of the map with your mouse and read the comments for the environmental conditions associated with the cell.
                    Once you find a cell to place your ecosystem, click on it to select the cell. The relevant conditions will now appear on the top-right menu.""")
    
    # using the clickable images function to create the main picture out of 288 picture,
    #  the titles which are the hoverable texts in each image are taken from the for_refrence df,
    #  the width height and margin are very important in order to have correct image view(calculated by the width of the section divided by the number of columns)
        clicked = clickable_images(
        st.session_state['real_img_list2'],
            titles=["Depth:" + str(for_refrence['alt'][i]) +
                    "\n" + "Temperture:" + str(for_refrence['temp'][i]) +
                    "\n" + "Wind:" + str(for_refrence['wind'][i]) +
                    "\n" + "Salinity:" + str(for_refrence['ph'][i]) +
                    "\n" + "Clarity:" + str(for_refrence['pressure'][i]) +                  
                    "\n" + "Oxygen:" + str(for_refrence['cloud'][i]) +
                    "\n" + "Current:" + str(for_refrence['sunlight'][i]) for i in range(len(st.session_state['real_img_list2']))],
            div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap","width":"664px"},
            img_style={"margin": "0.5px",
                        "width": "40px",
                        "height":"21px",}
        )


    # list 1 of the right species to choose
    True_species1 = ['Green Zoan',
    'Peacock Tail',
    'Red Sea Fern',
    'Kole Tang',
    'Pacific Goliath',
    'Queen Parrotfish',
    'Bull Shark',
    'Convict Surgeon Fish'

    ]

    # list 2 of the right species to choose
    True_species2 = True_species1

    # the optimal conditions, first is min second is max
    optimal_alt =[1001,1400]
    optimal_temp =[26,27.9]
    optimal_wind =[1,9]
    optimal_ph =[4.5,6]



    # working on the right column
    with right:
        # adding a submit primary button(diffrent design)
        submit = st.button('Submit', type = 'primary')

        # header for the conditions
        st.markdown("<h5 style='text-align: left; color: grey;'>Conditions </h5>", unsafe_allow_html=True)

        #creating two more columns
        col_top_left,col_top_mid, col_top_right = st.columns([0.5,3,1.5])

        # creating diffrent check boxes for each condition and listing them
        with col_top_left:
            check_alt = st.checkbox('', key='depth')
            check_temp= st.checkbox('', key='temp')
            check_wind = st.checkbox('', key='wind')
            check_ph  = st.checkbox('', key='salt')
            check_air = st.checkbox('', key='clarity')
            check_cloud = st.checkbox('', key='oxy')
            check_sun = st.checkbox('', key='curr')
            check_list = [check_alt,check_temp,check_wind,check_ph,check_air,check_cloud,check_sun]
            
            # taking the parameters from the clicked image into the conditions part, limiting the condtions view to only 4 at a time
        with col_top_right:
            col_lst = ["Depth:","Tempeture:","Wind:","Salinity:","Clarity:","Oxygen:","Current:"]
            parameters = [str(for_refrence['alt'][clicked]) if clicked > -1 and check_alt and (sum(check_list) <= 4) else "--",
                    str(for_refrence['temp'][clicked]) if clicked > -1 and check_temp and (sum(check_list) <= 4) else "--",
                    str(for_refrence['wind'][clicked]) if clicked > -1 and check_wind and (sum(check_list) <= 4) else "--",
                    str(for_refrence['ph'][clicked]) if clicked > -1 and check_ph and (sum(check_list) <= 4) else "--",
                    str(for_refrence['pressure'][clicked]) if clicked > -1 and check_air and (sum(check_list) <= 4) else "--",
                    str(for_refrence['cloud'][clicked]) if clicked > -1 and  check_cloud and (sum(check_list) <= 4) else "--",
                    str(for_refrence['sunlight'][clicked]) if clicked > -1 and  check_sun and (sum(check_list) <= 4) else "--"]
            data = {"Condtions": col_lst,
                "Values": parameters}
        for i in range(len(parameters)):
            with col_top_mid:
                st.caption(col_lst[i])     
            with col_top_right:
                st.caption(parameters[i])




    # creating a header of Selected species with a count out of eight
    # creating a header of Selected species with a count out of eight
    with right:
        selected = st.container()

    # show each species selected and add a delete button, if the del button is pressed the species is removed from the list
        for i in range(8):
                col3, col4 = st.columns([2,1.2])
                with col4:
                    if st.button('Del', key = str(i) + "del"):
                        if i < len(st.session_state.list2):
                            st.session_state.list2.remove(st.session_state.list2[i])
                with col3:
                    try:
                        st.markdown(st.session_state.list2[i])
                    except IndexError:
                        continue
        with selected:
            Selected = st.markdown("<h5 style='text-align: left; color: grey;'>Selected Species " + str(len(st.session_state.list2)) + "/8</h5>", unsafe_allow_html=True)
        st.markdown('---')
        if st.checkbox('Log Out'):
                st.error('Are you sure you would like to Log Out?')
                authenticator.logout('Log Out','main') 
    # logical test to see if the parameters are in the right range
    if ((parameters[0] != "--") & (parameters[1] != "--") & (parameters[2] != "--") & (parameters[3] != "--")):
        altitude = (float(parameters[0]) >= optimal_alt[0])  & (float(parameters[0]) <= optimal_alt[1])
        temp = (float(parameters[1]) >= optimal_temp[0])  & (float(parameters[1]) <= optimal_temp[1])
        wind = (float(parameters[2]) >= optimal_wind[0])  & (float(parameters[2]) <= optimal_wind[1])
        ph = (float(parameters[3]) >= optimal_ph[0])  & (float(parameters[3]) <= optimal_ph[1])

    # the final test, checking the species and conditions, four diffrent answers using a pop up message
    incomplete = Modal(key="incomplete Key",title="Your ecosystem is incomplete")
    no_sus = Modal(key="no_sus Key",title="Your ecosystem is NOT sustainable")
    success = Modal(key="Congrats! Key",title="Congrats!")

    with left:
        if submit:
            if parameters[0] == "--":
                with incomplete.container():
                    st.markdown('Please make sure you have selected 8 species and the corresponding environmental conditions.')
            elif ((parameters[0] == "--") | (parameters[1] == "--") | (parameters[2] == "--") | (parameters[3] == "--")):
                with incomplete.container():
                    st.markdown('Please make sure you have selected 8 species and the corresponding environmental conditions.')
            elif len(st.session_state.list2) < 8:
                with incomplete.container():
                    st.markdown('Please make sure you have selected 8 species and the corresponding environmental conditions.')
            elif ((check_if_equal(st.session_state.list2,True_species1)) | (check_if_equal(st.session_state.list2,True_species2))) & (altitude & temp & wind & ph):
                with success.container():
                    st.markdown('Your ecosystem is sustainable.')
                    st.balloons()
            else:
                with no_sus.container():
                    st.markdown('Please check your species and environmental conditions, then try again') 
                
elif authentication_status == False:
    st.error('Username/password is incorrect')
    # try:
    #     if authenticator.register_user('Register user', preauthorization=False):
    #         st.success('User registered successfully')
    #         with open('config.yaml', 'w') as file:
    #             yaml.dump(config, file, default_flow_style=False)
    # except Exception as e:
    #     st.error(e)
elif authentication_status == None:
    st.warning('Please enter your username and password')

    # remove the top padding
st.markdown(
            f'''
            <style>
                .css-z5fcl4 {{
                    padding-top: {1}rem;
                }}
            </style>
            ''',unsafe_allow_html=True)

#hiding the multipage in the sidebar
no_sidebar_style = """
    <style>
       .css-79elbk {display: none;}
    </style>
"""
# hide the made with streamlit
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown(no_sidebar_style, unsafe_allow_html=True)


#styling the buttons
#style for the submit button
button = st.markdown("""
<style>
.element-container.css-1biol9.e1tzin5v3:nth-of-type(1) button
{
    border-color: rgb(255, 75, 75);
color: rgb(255, 255, 255);
background-color: rgb(255,75, 75);
}
</style>""", unsafe_allow_html=True)

#style for the submit button when the side bar is closed
button_no_side = st.markdown("""
<style>
.element-container.css-1b6t8kw.e1tzin5v3:nth-of-type(1) button
{
    border-color: rgb(255, 75, 75);
color: rgb(255, 255, 255);
background-color: rgb(255,75, 75);
}
</style>""", unsafe_allow_html=True)

# style for the buttons in general
button_style = st.markdown("""
<style>
div.stButton > button:first-child {
    text-align : center;
    font-size:1px;
    height : 20px;
    margin : 0px;
}
</style>""", unsafe_allow_html=True)

# style for the simulation 1-3 options button
sim_button = st.markdown("""
<style>
.css-firdtp
{
    border-color: rgb(255, 75, 75);
color: rgb(255, 75, 75);
background-color: rgb(255,255, 255);
}
.css-firdtp:hover {
background-color: rgb(255, 51, 51);
color: rgb(255, 255, 255);
</style>""", unsafe_allow_html=True)