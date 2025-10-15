# -*- coding: utf-8 -*-
"""
Created on Thu 14 sept 2025 update 

@author: master
"""

# Local URL: http://localhost:8501
# Network URL: http://10.11.242.237:8501
# 

# RUN IN COMMAND LINE ->  
# conda activate dev_stat
# python -m streamlit run D:\_00_LYME_CH\data\lyme_ch_questionnaire\lyme_ch_questionnaire_streamlit_v01.py


# ======================================================================

import streamlit as st
import pandas as pd
import numpy as np
import socket
import uuid
from datetime import date
import json
from ftplib import FTP
import pickle 

import streamlit_survey as ss



#st.title('Lyme Suisse - Questionnaire')
# survey = ss.StreamlitSurvey()
# ======PAGED SURVEY=============================

# Paged Surveys
# Survey components can be grouped into pages using the Pages class. 
# The Pages class also supports survey state restoration, so that users 
# can go back and forth between pages without losing their answers:

# Code Example:

# ---------- how to implement forms (difference -> No page update on each click ------------------
# with st.form("my_form"):
#     st.write("Inside the form")
#     slider_val = st.slider("Form slider")
#     checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write("slider", slider_val, "checkbox", checkbox_val)
# st.write("Outside the form")



# -----------------------------------------------------    



# with st.form("lyme_ch_survey"):
    
survey = ss.StreamlitSurvey("Lyme Switzerland - personal anonymous survey")

# ------ add logo ---------------------------

logo_link = "https://static.wixstatic.com/media/b9467e_4188d6a85393431ba1fe7b25dc42d961~mv2.jpeg/v1/fill/w_371,h_110,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/"
logo_image = "Lyme-Suisse_Logo.jpeg"

st.image(logo_link+logo_image, caption="Lyme Switzerland")
#st.logo(
#    logo_image,
#    link=logo_link,
#    icon_image=logo_image)

# ------- INITIALIZE SESSION VARIABLES ---------------------------


# if "parameters" not in mystate:
#     mystate.parameters = {"Parameter A": "", "Parameter B": "", "Parameter C": "", }




# -----------------------------


# ======================================================================================================================

#pages = survey.pages(9, progress_bar=True, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))

#pages = survey.pages(9, progress_bar=True, on_submit=lambda: st.success("Vos réponses sont enregistrées, merci de votre collaboration !"))
pages = survey.pages(10, progress_bar=True, on_submit=lambda: st.success(""))
# pages = survey.pages(9, progress_bar=True, on_submit=submitted())


# Using "with" notation
with st.sidebar:
    # Custom CSS to modify sidebar width
    css = '''
    <style>
        [data-testid="stSidebar"]{
            min-width: 600px;
            max-width: 900px;
        }
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)
        
    st.sidebar.header("Questionnaire Lyme & coinfections")
    
    st.sidebar.text('''Qui sommes-nous ? 
                    Lyme Suisse est une association à but non lucratif, 
                    fondée en 2024 par des patients et pour les patients. 
                    Son objectif est de partager les connaissances actuelles 
                    sur les maladies vectorielles ( maladie de Lyme, 
                    bartonelloses, babésioses, encéphalite à tique, etc) afin
                    d'aider d’autres malades à mieux comprendre leur condition et trouver
                    des issues.
                    Le questionnaire est un outil statistique (et anonyme) indispensable
                    pour nous faire avancer dans la compréhension de ces maladies.
                    Merci de votre collaboration.''')
    
    
    # add_radio = st.radio(
    #     "Choose a shipping method",
    #     ("Standard (5-15 days)", "Express (2-5 days)")
    # )
    # ---- BUTTON TO QUIT SURVEY ------------------------------------
    
    # st.button("Seconday button")  # st.button default type is secondary
    # st.button("Primary button", type="primary")
    # and the, use this CSS selectors to modify their style:
    
    # button[kind="primary"] {
    #   background-color: orange;
    # }
    
    # button[kind="seondary"] {
    #     background-color: purple;
    # }
    
    
    if st.button("Annuler et quitter - toutes les données seront effacées"):
        st.markdown("""<meta http-equiv="refresh" content="0; url='https://www.lyme.ch/en'" />""", unsafe_allow_html=True)
    #button[kind="primary"] {background-color: red;}
    
    # Babesia distribution map
    # https://www.frontiersin.org/files/Articles/474717/fevo-07-00401-HTML/image_m/fevo-07-00401-g002.jpg
    
    # img_link = "https://www.frontiersin.org/files/Articles/474717/fevo-07-00401-HTML/image_m/"
    # img_image = "fevo-07-00401-g002.jpg"

    # st.image(img_link+img_image, caption="Borrelia distribution map")
    
    # Borrelia distribution map
    # https://www.frontiersin.org/files/Articles/474717/fevo-07-00401-HTML/image_m/fevo-07-00401-g002.jpg
    # img_link = "https://www.mdpi.com/pathogens/pathogens-10-00230/article_deploy/html/images/"
    # img_image = "pathogens-10-00230-g007.png"

    # st.image(img_link+img_image, caption="Babesia distribution map")
    
    img_link = "https://www.lymedisease.org/wp-content/uploads/2014/04/"
    img_image = "prevalence-coinfections-small.jpg"

    st.image(img_link+img_image, caption="Lyme & coinfections")
    
    
    
    
    # Bartonella distribution map
    # https://parasitesandvectors.biomedcentral.com/articles/10.1186/s13071-018-3152-6/figures/1
    # 13071_2018_3152_Fig1_HTML.webp
    #img_link = ""
    #img_image = "13071_2018_3152_Fig1_HTML.webp"

    #st.image(img_link, caption="Bartonalla distribution map")




# ---------------- DISPLAY WEB PAGE HEADER ----------------------------------------------

# ------ permanent title ----------------------------------
st.title('Lyme Suisse - Questionnaire')
backgroundColor = "#000000"

# with st.form("My form"):
#     first = st.text_input("First name")
#     last = st.text_input("Last name")
#     if st.form_submit_button("Submit"):
#         st.write(first+" "+last)

st.markdown("""
    <style>
        .stTextInput > label {
            font-size:80%; 
            font-weight:bold; 
            color:green;
        }
        .stMultiSelect > label {
            font-size:80%; 
            font-weight:bold; 
            color:green;
        } 
    </style>
    """, unsafe_allow_html=True)




def validate(name, field_name):
    if not name:
        return False, f"{field_name} is required"
    #if not re.match(r"^[a-zA-Z'\\\\s\\\\-]{2,50}$", name):
    #    return False, f"{field_name} must contain only letters, spaces, hyphens, or apostrophes (2-50 characters)"
    return True, ""




# ====================================================================================
# Understanding widget behavior
# https://docs.streamlit.io/develop/concepts/architecture/widget-behavior
# Save widget values in Session State to preserve them between pages
# If you want to navigate away from a widget and return to it while keeping its value, use a separate key in st.session_state to save the information independently from the widget. In this example, a temporary key is used with a widget. The temporary key uses an underscore prefix. Hence, "_my_key" is used as the widget key, but the data is copied to "my_key" to preserve it between pages.

# import streamlit as st

# def store_value():
    # Copy the value to the permanent key
#     st.session_state["my_key"] = st.session_state["_my_key"]

# Copy the saved value to the temporary key
# st.session_state["_my_key"] = st.session_state["my_key"]
# st.number_input("Number of filters", key="_my_key", on_change=store_value)
# ====================================================================================



with pages:
    
# ------------------------------------------------------------------------------------------------------------        
    if pages.current == 0:
        
        
        
        
        #st.markdown("This is black and :red[this is red!]") 
        #st.markdown("This is black and :red[this is red!]") 
        
        
        #st.title('Introduction')
        st.header('Introduction', divider=True)
        #first = st.text_input("First name")
        #last = st.text_input("Last name")
        #if st.form_submit_button("Submit"):
        #    st.write(first+" "+last)
    
        
    
        # st.markdown("This is black and :red[this is red!]")
        # st.header("This is a header with a divider", divider="gray")
        # st.header("These headers have rotating dividers", divider=True)
        
        # st.header("Two", divider=True)
        # st.header("Three", divider=True)
        # st.header("Four", divider=True)
        
        
        #st.write("Points essentiels :")
        st.header("Points essentiels", divider=True)
        st.write("Ce questionnaire :")
        st.write('- a été developpé pour le diagnostic de la maladie de Lyme ainsi que celui des co-infections')
        st.write("- se réfère au modèle de base du Dr Horowitz (validé par l'autorité médicale américaine)") 
        st.write("- inclut des éléments de diagnostique additionnels")
        st.write("- permet d' établir une point de situation rapide")
        st.write('- est totalement anonyme')
        st.write("- Aucune de vos données personnelles permettant une identification n'est demandée ou enregistrée")
    
               
        #privacy_pol_url = "https://www.streamlit.io"
        
        st.write("Politique de confidentialité  [link](https://www.lyme.ch)")
        
        #st.write("Privacy policy" % privacy_pol_url)
        #st.markdown("Privacy policy" % privacy_pol_url)
        
        # if no : 
        # ------------------------------------------------------
        
        # The index of the preselected option on first render. If None, 
        # will initialize empty and return None until the user selects
        # an option. Defaults to 0 (the first option).
        
        # survey.radio('''Avez-vous effectué des tests privés (Ã  l'étranger par ex.) et reçu un diagnostic clair de maladie de Lyme
        #                               (et/ou de coinfections Ã©ventuelles) par un laboratoire ou un mÃ©decin ?''',
        #                               options=['Oui', 'Non'], index=None,  
        #                               key = 'private_tests',
        #                               horizontal=True)
        
        #◙ streamlit.errors.StreamlitAPIException: st.session_state.Q_0001 cannot be modified after the widget with key Q_0001 is instantiated.
        
        st.session_state["Q0001"] = survey.radio("Avez-vous déjà  complété ce formulaire sur notre site (www.lyme.ch) ?*",
                                             options=["Oui", "Non"], 
                                             index=None, 
                                             #label_visibility="collapsed",
                                             key = 'Q_0001',
                                             horizontal=True)
                                
        
        st.session_state["Q0002"] = survey.radio("Autorisez-vous Lyme Suisse à  utiliser vos réponses pour des raisons analytiques (Recherche)?*",
                                             options=["Oui", "Non"], 
                                             index=None, 
                                             key = 'Q_0002',
                                             horizontal=True)
        
        # ---- WARNING: KEY IS ONLY KEPT ON LOCAL PAGE -> TRANSFER KEY TO PERMANENT SESSION STATE VARIABLE
        
# ------------------------------------------------------------------------------------------------------------        
    elif pages.current == 1:
        st.header('page 1 - Informations générales', divider=True)
        
        st.session_state['Q0003A'] = survey.number_input('Quel est votre âge ?*',key = 'Q_0003A')
        # ---------------------------------------------
        
        st.session_state['Q0003B'] = survey.radio('Votre sexe ?*', 
                                             options=["Masculin", "Féminin","Autre"],
                                             index=None,  
                                             key = 'Q_0003B',
                                             horizontal=True)
        
        #st.write('Votre âge : ', number)
        #survey.selectbox("Selection box:", options=["Option 1", "Option 2", "Option 3", "etc"])
        #st.selectbox('Quel est votre lieu (canton) de résidence ?*',("Vaud", "Fribourg", "Neuchâtel",'Genève','Bern','Tessin','Bern', 'Hors Suisse'))
        st.session_state['Q0004'] = survey.selectbox('Quel est votre canton de résidence ?*', 
                                                 options=["Vaud", "Fribourg", "Neuchâtel",'Genève','Bern','Tessin','Bern', 'Hors Suisse'],
                                                 index=None,  
                                                 key = 'Q_0004')
        #st.write("You selected:", option)
 
# ------------------------------------------------------------------------------------------------------------
    elif pages.current == 2: 
        st.header('Page 2 - Diagnostiques tests effectués en Suisse', divider=True)
        #st.title('Diagnostiques, tests - page 2')
        
        
        st.session_state['Q0005'] = survey.number_input('Durée de la maladie (en années): *',
                                                   key = 'Q_0005')
        st.session_state['Q0006'] = survey.number_input("Durée de l'errance  médicale (en années): *",
                                                   key = 'Q_0006')
        
        st.session_state['Q0007'] = survey.slider("Nb d'année jusqu'au premier diagnostique (en années) ", 
                                              min_value=1, 
                                              max_value=50,
                                              key = 'Q_0007')
        
        # survey.multiselect("Multiple choice:", options=["Option 1", "Option 2", "Option 3", "etc"])
        
        st.session_state['Q0008a'] = survey.multiselect("Avez-vous, EN SUISSE, reçu des diagnostics différents de la maladie de Lyme ou co-infections (complétez ci-dessous) ?",
                                                   options=['Fibromyalgie','Syndrome de fatigue chronique', 'Troubles psychosomatiques','Autres maladies infectieuses',
                                                            'Maladie auto-immune','lupus', 'sclérose en plaques','polyarthrite rhumatoïde',
                                                            'Dépression','Burn-out','Troubles anxieux généralisés',"Thada", "Autisme", "Dépression",
                                                            "Schizophrénie",'Psychoses','Démence','Bipolarité','Autre','Non'],
                                                   key = 'Q_0008a')
        
        st.session_state['Q0008b'] = survey.multiselect("Avez-vous, à l'étranger (HORS SUISSE), reçu des diagnostics différents de la maladie de Lyme ou co-infections (complétez ci-dessous) ?",
                                                   options=['Fibromyalgie','Syndrome de fatigue chronique', 'Troubles psychosomatiques','Autres maladies infectieuses',
                                                            'Maladie auto-immune','lupus', 'sclérose en plaques','polyarthrite rhumatoïde',
                                                            'Dépression','Burn-out','Troubles anxieux généralisés',"Thada", "Autisme", "Dépression",
                                                            "Schizophrénie",'Psychoses','Démence','Bipolarité','Autre','Non'],
                                                   key = 'Q_0008b')
        
        # ----------------- MALADIES INFECTIEUSES --------------------
        st.write('Autre diagnostics antérieurs de maladies infectieuses : ')
        
        options_inf =['Anaplasmose',
                     'Angine bactérienne',
                     'Aspergillose',
                     'Babésiose',
                     'Bartonellose',
                     'Borréliose',
                     'Botulisme',
                     'Bronchiolite',
                     'Bronchiolite',
                     'Brucellose',
                     'COVID-19 (virus SARS-CoV-2)',
                     'Candidoses',
                     'Chlamydiose',
                     'Clostridium difficile',
                     'Coqueluche',
                     'Cryptococcose',
                     'Dengue',
                     'Diphtérie-tétanos',
                     'Echinococcose',
                     'Ehrlichiose monocytique humaine',
                     'Escherichia coli ',
                     'Fièvre Q (Coxiella burnetii)',
                     'Fièvre de la Vallée du Rift',
                     'Fièvre hémorragique Ebola',
                     'Fièvre jaune',
                     'Fièvre typhoïde',
                     'Fièvres entériques (typhoïde et paratyphoïde)',
                     'Fusobacterium',
                     'Gale',
                     'Gonorrhée',
                     'Helicobacter pylori',
                     'Hépatite A, B et C',
                     'Infection à staphylocoque',
                     'Klebsiellose',
                     'Lambliase (Giardia intestinalis)',
                     'Leptospirose',
                     'Listériose',
                     'Légionellose',
                     'Maladie à virus Zika',
                     'Mononucléose infectieuse',
                     'Mononucléose infectieuse du virus Epstein-Barr (EBV)',
                     'Mpox (variole du singe)',
                     'Mycoses cutanées',
                     'Méningite bactérienne',
                     'Méningo-encéphalite à tiques FSME',
                     'Méningocoque',
                     'Paludisme (malaria)',
                     'Paludisme - Malaria',
                     'Peste',
                     'Pneumonie',
                     'Poliomyélite',
                     'Prevotella',
                     'Rougeole',
                     'Scarlatine',
                     'Septicémie Multiple',
                     'Streptocoque',
                     'Syphilis',
                     'Toxoplasmose',
                     'Tuberculose',
                     'Tularémie',
                     'Typhoïde',
                     'VIH/sida',
                     'Zona\tVirus']

        
        
        st.session_state['Q0008c'] = survey.multiselect("Avez-vous antérieurement reçu des diagnostics concernant les maladies infectieuses suivantes (complétez ci-dessous) ?",
                                                   options = options_inf,
                                                   key = 'Q_0008c')
        
       

        #st.write("You selected:", diags_other)
        
        # ------------ diagnostic in Switzerland ---------------------------
        
        
        
        
        
        st.write("Utilisez cette barre pour indiquer le nombre de tests effectués (EN SUISSE), et complétez le tableau ci-dessous")   

        # -------------- ====================== CH SLIDER & GRID ==============================================================
        
        # a selection for the user to specify the number of rows
        #st.session_state['s1_num_rows_ch'] = st.session_state['num_rows_ch']
         
        #st.write('num_rows_ch = ',st.session_state['num_rows_ch'])   
        
        if st.session_state['num_rows_ch'] > 1:
            s1_idx = st.session_state['num_rows_ch']
        else:
            s1_idx = 1
            
            
        st.session_state['num_rows_ch'] = st.slider('CH - Number of rows', min_value=1, max_value=10, value=s1_idx, key='s1_num_rows_ch')
        
        # columns to lay out the inputs
        nb_col_01 = 3
        
        # --- initialize slider 1 keys --------------
         
        
        #st.write('Canton de résidence = ',st.session_state['0004'])     
        
        
        grid_01 = st.columns(nb_col_01)
        
        list_01 = ['','Borrelia','Bartonella','Babesia','encephalitis virus (TBE-V)','Anaplasma','Rickettsia','Ehrlichia',
                   'Autres virus','Autres parasites','Autres Bactéries']
        list_02 = ['','ELISA', 'Western Blot','IFA','PCR','Elispot','FISH','Immunoblot','Culture','Autre']
        list_03 = ['','Positif', 'Négatif','Indéterminé']
        
        # ----------------------------------------------------------------------------------
        
        for r in range(0,st.session_state['num_rows_ch']):
            
            with grid_01[0]:
                idx_ch_01 = list_01.index(st.session_state[f'test_ch_r{r}_c1'])
                #st.write('idx_ch_01 = ',idx_ch_01)
                #st.session_state[f'r{r}_c1'] = st.session_state[f'test_ch_r{r}_c1']
                res1 = st.selectbox("Pathogène recherché",
                                        options=list_01,
                                        index=idx_ch_01,
                                        key=f'r{r}_c1',
                                        # key not useful (disappear when changing page..)
                                        #on_change=keep_values(st.session_state['test_ch_r1_c1'])
                                        )
                st.session_state[f'test_ch_r{r}_c1'] = res1
                #st.write('session_state test_ch_r{r}_c1 = ',st.session_state[f'test_ch_r{r}_c1'])                
           
            with grid_01[1]:
                #st.session_state['idx'] = st.session_state['0009b']
                idx_ch_02 = list_02.index(st.session_state[f'test_ch_r{r}_c2'])
                #st.write('idx_ch_02 = ',idx_ch_02)
                #st.session_state[f'r{r}_c2'] = st.session_state[f'test_ch_r{r}_c2']
                res2 = st.selectbox('Test effectué',
                                        options=list_02,
                                        index=idx_ch_02,
                                        key=f'r{r}_c2'
                                        #on_change=keep_values(st.session_state['test_ch_r1_c2'])
                                        )
                                        #placeholder="Select contact method..." )
                st.session_state[f'test_ch_r{r}_c2'] = res2
                #st.write('session_state test_ch_r{r}_c2 = ',st.session_state[f'test_ch_r{r}_c2'])        
            
                                  
            with grid_01[2]:
                idx_ch_03 = list_03.index(st.session_state[f'test_ch_r{r}_c3'])
                #st.write('idx_ch_03 = ',idx_ch_03)
                #st.session_state[f'r{r}_c3'] = st.session_state[f'test_ch_r{r}_c3']
                res3 = st.selectbox('Résultat des tests',
                                        options=list_03,
                                        index=idx_ch_03,
                                        key=f'r{r}_c3'
                                        #on_change=keep_values(st.session_state['test_ch_r1_c3'])
                                        )
                st.session_state[f'test_ch_r{r}_c3'] = res3
                #st.write('session_state test_ch_r{r}_c3 = ',st.session_state[f'test_ch_r{r}_c3'])        
                             
           
                #st.session_state['idx'] = st.session_state['0009c']
        # st.write('session_state ch test_r0_c1 = ',st.session_state['test_ch_r0_c1']) 
        # st.write('session_state ch test_r0_c2 = ',st.session_state['test_ch_r0_c2'])                                                                                                                      
        # st.write('session_state ch test_r0_c3 = ',st.session_state['test_ch_r0_c3'])
        # st.write('# session_state ch test_r1_c1 = ',st.session_state['test_ch_r1_c1']) 
        # st.write('session_state ch test_r1_c2 = ',st.session_state['test_ch_r1_c2'])                                                                                                                      
        # st.write('session_state ch test_r1_c3 = ',st.session_state['test_ch_r1_c3'])
        
                
#TypeError: RadioMixin.radio() got an unexpected keyword argument 'step'        

                                                                                           
        
        
        # ============================================================================
 
    # ================================================================================  

# ------------------------------------------------------------------------------------------------------------    
    elif pages.current == 3:
       
        st.header("Page 3 - Diagnostiques tests effectués à l'étranger", divider=True)       
      
        #st.write('Canton de résidence = ',st.session_state['0004'])     
        
        #nb_timetoget_diagnostic = survey.number_input("Délais pour établir vos diagnostics (en mois) ? ")
        #2survey.number_input("Délais pour établir vos diagnostics (en mois) ? ", min_value=0, max_value=50, value=1)
        # a selection for the user to specify the number of rows
        
        
        
        st.session_state['Q0010'] = survey.radio("Avez-vous effectué des tests privés (à l'étranger par ex.) et reçu un diagnostic clair de maladie de Lyme (et/ou de coinfections éventuelles) par un laboratoire ou un médecin ?",
                                            options=['Oui', 'Non'], index=None,  
                                            key = 'Q_0010',
                                            horizontal=True)
        
        
        #PrÃ©cisez les rÃ©sultats et types de tests effectuÃ©s :  
        # st.write("Utilisez cette barre pour indiquer le nombre de tests effectués (A L'ETRANGER), et complétez le tableau ci-dessous")  
        
        #st.write('st session state - test_nch_r0_c1 = ',st.session_state['test_nch_r0_c1'] )
        #st.write('st session state - test_nch_r1_c1 = ',st.session_state['test_nch_r1_c1'] )

        # a selection for the user to specify the number of rows
       
        if st.session_state['num_rows_nch'] > 1:
           
            s1_idx_nch = st.session_state['num_rows_nch']
        else:
            s1_idx_nch = 1 
       
        
       
        st.session_state['num_rows_nch'] = st.slider('NON CH - Number of rows', min_value=1, max_value=10, value = s1_idx_nch, key='s2_num_rows_nch')
        
        
        # ---------- initialize session state ---------------------
        
        
        
        
        
        
        # columns to lay out the inputs
        grid_02 = st.columns(4,gap="medium", vertical_alignment="top", border=True)
        
        
        list_04 = ['','Borrelia','Bartonella','Babesia','encephalitis virus (TBE-V)','Anaplasma','Rickettsia','Ehrlichia','Autre virus','Autre parasite','Autre Bacteria']
        list_05 = ['','ELISA', 'Western Blot','IFA','PCR','Elispot','FISH','Immunoblot','Culture','Autre']
        list_06 = ['','Positif', 'Négatif','Indéterminé']
        list_07 = ['','USA','France','Allemagne','Belgique','Autre UE','Autre']
        
        # Function to create a row of widgets (with row number input to assure unique keys)
        # Loop to create rows of input widgets
        for r2 in range(0,st.session_state['num_rows_nch']):
                        
            #add_row(r) 
                            
            with grid_02[0]:
                idx_nch_01 = list_04.index(st.session_state[f'test_nch_r{r2}_c1'])
                # st.write('idx_nch_01 = ',idx_nch_01)
                res1b = st.selectbox("Pathogène recherché",
                                        options=list_04,
                                        index=idx_nch_01,
                                        key=f'nch_r{r2}_c1'
                                        
                                        #key=f'input_col1_notch{row}')
                                        )
                                        #placeholder="Select contact method..." )
                
                st.session_state[f'test_nch_r{r2}_c1'] = res1b
                # st.write('session_state test_nch_r{r2}_c1 = ',st.session_state[f'test_nch_r{r2}_c1'])            
                 
                        
            with grid_02[1]:
                idx_nch_02 = list_05.index(st.session_state[f'test_nch_r{r2}_c2'])
                # st.write('idx_nch_02 = ',idx_nch_02)
                res2b = st.selectbox('Test effectué',
                                         options=list_05,
                                         index=idx_nch_02,
                                         key=f'nch_r{r2}_c2'
                                         )
                                         #placeholder="Select contact method..." )
                st.session_state[f'test_nch_r{r2}_c2'] = res2b
                # st.write('session_state test_nch_r{r2}_c2 = ',st.session_state[f'test_nch_r{r2}_c2'])
                
                
                
            with grid_02[2]:
                idx_nch_03 = list_06.index(st.session_state[f'test_nch_r{r2}_c3'])
                # st.write('idx_nch_03 = ',idx_nch_03)
                res3b = st.selectbox('Résultat des tests',
                                        options=list_06,
                                        index=idx_nch_03,
                                        key=f'nch_r{r2}_c3'
                                        )
                                        #placeholder="Select contact method..." )
                st.session_state[f'test_nch_r{r2}_c3'] = res3b
                # st.write('session_state test_nch_r{r2}_c3 = ',st.session_state[f'test_nch_r{r2}_c3'])
               
                
             
            with grid_02[3]:
                idx_nch_04 = list_07.index(st.session_state[f'test_nch_r{r2}_c4'])
                # st.write('idx_nch_04 = ',idx_nch_04)
                res4b = st.selectbox('Test effectués en (Région, pays)',
                                        options=list_07,
                                        index=idx_nch_04,
                                        key=f'nch_r{r2}_c4'
                                        )
                                        #placeholder="Select contact method..." )   
                st.session_state[f'test_nch_r{r2}_c4'] = res4b
                # st.write('session_state test_nch_r{r2}_c4 = ',st.session_state[f'test_nch_r{r2}_c4'])    
             
#TypeError: RadioMixin.radio() got an unexpected keyword argument 'step'        

        # ================================================================================      
    
# ------------------------------------------------------------------------------------------------------------     
    elif pages.current == 4:
        
        #st.write('Canton de résidence = ',st.session_state['0004'])     
        
        # Q1 = survey.radio("Thumbs up/down:", options=["NA", "👍", "👎"], horizontal=True, id="Q1")
        # if Q1 == "👍":
        #     Q1_1 = survey.text_input("Why did you select '👍'?", id="Q1_1")
        
        
        # -- rating -> 0 None      1 Mild      2 Moderate      3 Severe
        st.session_state['rtot'] = 0
        st.session_state['r1_tot'] = 0
        
        st.header('Page 4 - SECTION 1 (HQ)- Prévalence sur 38 symptômes', divider=True) 
        
        
        # set the initial default value of rtot (total quest rating)
        
        list_section_01 = ['Jamais', 'Faible','Modéré','Sévère']

        def q_rate1(state):
            if state == list_section_01[0]:
                r1 = 0
            elif state == list_section_01[1]:
                r1 = 1
            elif state == list_section_01[2]:
                r1 = 2
            else:
                r1 = 3
            st.session_state.r1_tot = st.session_state.r1_tot + r1
            #st.write("Current rate section 1 = ",r1,' Total rate = ',st.session_state.rtot)  
            return r1
        
            
        # ================ QUESTIONNAIRE HOROWITZ REVU ======================================
        
        survey.radio('1. Fièvre, sueurs inexpliqués', options=list_section_01, index=0, horizontal=True, key="QH01")
        q_rate1(st.session_state.QH01)
                
        survey.radio('2a. Perte de poids inexpliquée ', options=list_section_01,index=0, horizontal=True, key="QH02a")
        #st.write(st.session_state.Q02)  
        q_rate1(st.session_state.QH02a)
        # -----------------------------------
        survey.radio('2b. Prise de poids inexpliquée ', options=list_section_01,index=0, horizontal=True, key="QH02b")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02b)
        
        survey.radio('2c. Prise de poids inexpliquée ', options=list_section_01,index=0, horizontal=True, key="QH02c")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02c)
        
        survey.radio('2d. Corps étrangers dans les yeux ', options=list_section_01,index=0, horizontal=True, key="QH02d")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02d)
        
        survey.radio('2e. saturation en oxygene limite 94 pc ', options=list_section_01,index=0, horizontal=True, key="QH02e")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02e)
        
        survey.radio('2f. crevasses sur les doigts ', options=list_section_01,index=0, horizontal=True, key="QH02f")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02f)
        
        survey.radio('2g. Erythrème migrant (EM) ', options=list_section_01,index=0, horizontal=True, key="QH02g")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02g)
        
        survey.radio('2h. Lésions cutannées - Bartonella Associated Cutaneous Lesions (BACL)  ', options=list_section_01,index=0, horizontal=True, key="QH02h")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02h)
        
        survey.radio('2i. Paresies ', options=list_section_01,index=0, horizontal=True, key="QH02i")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02i)
        
        survey.radio('2j. Hallucinations auditives ', options=list_section_01,index=0, horizontal=True, key="QH02j")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02j)
        
        survey.radio('2k. Paresies ', options=list_section_01,index=0, horizontal=True, key="QH02k")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02k)
        
        survey.radio('2l. Douleurs musculaires profondes sporadiques ', options=list_section_01,index=0, horizontal=True, key="QH02l")
        #st.write(st.session_state.Q02b)  
        q_rate1(st.session_state.QH02l)
        
        # ------------------------------      
        survey.radio(" 3. Fatigue", options=list_section_01, index=0,horizontal=True, key="QH03")
        q_rate1(st.session_state.QH03)
        survey.radio('4. Perte de cheveux inexpliquée', options=list_section_01,index=0, horizontal=True, key="QH04")
        q_rate1(st.session_state.QH04)
        survey.radio('5. Ganglions gonflés', options=list_section_01,index=0, horizontal=True, key="QH05")
        q_rate1(st.session_state.QH05)
        survey.radio('6. Maux de gorge', options=list_section_01,index=0, horizontal=True, key="QH06")
        q_rate1(st.session_state.QH06)
        survey.radio('7. Douleurs testiculaires ou pelviennes', options=list_section_01,index=0, horizontal=True, key="QH07")
        q_rate1(st.session_state.QH07)
        survey.radio('8. Règles irrégulières sans raison apparente', options=list_section_01,index=0, horizontal=True, key="QH08")
        q_rate1(st.session_state.QH08)
        survey.radio('9. Lactation inexpliquée, douleurs mammaires', options=list_section_01,index=0, horizontal=True, key="QH09")
        q_rate1(st.session_state.QH09)
        survey.radio('10. Vessie irritable ou dysfonctionnement urinaire', options=list_section_01,index=0, horizontal=True, key="QH10")
        q_rate1(st.session_state.QH10)
        survey.radio('11. Troubles sexuels, perte de libido', options=list_section_01,index=0, horizontal=True, key="QH11")
        q_rate1(st.session_state.QH11)
        survey.radio("12. Maux d'estomac, indigestions", options=list_section_01, index=0,horizontal=True, key="QH12")
        q_rate1(st.session_state.QH12)
        survey.radio('13. Constipation ou diarrhée', options=list_section_01,index=0, horizontal=True, key="QH13")
        q_rate1(st.session_state.QH13)
        survey.radio('14. Douleurs thoraciques ou intercostales', options=list_section_01,index=0, horizontal=True, key="QH14")
        q_rate1(st.session_state.QH14)
        survey.radio('15. Essoufflement, toux', options=list_section_01,index=0, horizontal=True, key="QH15")                                                         
        q_rate1(st.session_state.QH15)
        survey.radio('16. Palpitations, arythmies cardiaques', options=list_section_01, index=0,horizontal=True, key="QH16")
        q_rate1(st.session_state.QH16)
        survey.radio("17. Antécédents de souffle cardiaque ou d'atteinte valvulaire", options=list_section_01,index=0, horizontal=True, key="QH17")
        q_rate1(st.session_state.QH17)
        survey.radio("18. Douleur ou gonflement d'une ou plusieurs articulations", options=list_section_01,index=0, horizontal=True, key="QH18")                                                                 
        q_rate1(st.session_state.QH18)
        survey.radio('19. Raideur de la nuque ou du dos', options=list_section_01, index=0,horizontal=True, key="QH19")        
        q_rate1(st.session_state.QH19)
        survey.radio('20. Douleurs musculaires ou crampes', options=list_section_01, index=0,horizontal=True, key="QH20")
        q_rate1(st.session_state.QH20)
        survey.radio('21. Tressautement des muscles du visage ou du reste du corps (fasciculations)', options=list_section_01,index=0, horizontal=True, key="QH21")  
        q_rate1(st.session_state.QH21)
        survey.radio('22. Maux de tête',options=list_section_01,index=0, horizontal=True, key="QH22")
        q_rate1(st.session_state.QH22)
        survey.radio('23. Craquements dans le cou', options=list_section_01,index=0, horizontal=True, key="QH23")
        q_rate1(st.session_state.QH23)
        survey.radio('24. Fourmillements, engourdissements, sensations de brûlure ou de « coup de poignard » (paresthésies)', options=list_section_01, index=0,horizontal=True, key="QH24")                                                               
        q_rate1(st.session_state.QH24)
        survey.radio('25. Paralysie faciale', options=list_section_01,index=0, horizontal=True, key="QH25")
        q_rate1(st.session_state.QH25)
        survey.radio('26. Vision double ou floue', options=list_section_01,index=0, horizontal=True, key="QH26")
        q_rate1(st.session_state.QH26)
        survey.radio('27. Audition/oreilles : Bourdonnements, sifflements ou douleur dans les oreilles (acouphènes)', options=list_section_01,index=0, horizontal=True, key="QH27")
        q_rate1(st.session_state.QH27)
        survey.radio('28. Mal des transports accru, vertige', options=list_section_01,index=0, horizontal=True, key="QH28")
        q_rate1(st.session_state.QH28)
        survey.radio("29. Etourdissements, manque d'équilibre, difficultés à  marcher", options=list_section_01,index=0, horizontal=True, key="QH29")
        q_rate1(st.session_state.QH29)
        survey.radio('30. Tremblements', options=list_section_01,index=0, horizontal=True, key="QH30")
        q_rate1(st.session_state.QH30)
        survey.radio('31. Confusion, difficultés à penser', options=list_section_01,index=0, horizontal=True, key="QH31")
        q_rate1(st.session_state.QH31)
        survey.radio('32. Difficulté à se concentrer ou à  lire', options=list_section_01, index=0,horizontal=True, key="QH32")
        q_rate1(st.session_state.QH32)
        survey.radio('33. Oublis, mauvaise mémoire à court terme', options=list_section_01,index=0, horizontal=True, key="QH33")
        q_rate1(st.session_state.QH33)
        survey.radio('34. Désorientation ; je me perds ou je ne vais pas au bon endroit', options=list_section_01,index=0, horizontal=True, key="QH34")
        q_rate1(st.session_state.QH34)
        survey.radio('35. Difficulté à parler ou à écrire', options=list_section_01,index=0, horizontal=True, key="QH35")
        q_rate1(st.session_state.QH35)
        survey.radio("36. Sautes d'humeur, irritabilité", options=list_section_01,index=0, horizontal=True, key="QH36")
        q_rate1(st.session_state.QH36)
        survey.radio("36b. Dépression", options=list_section_01,index=0, horizontal=True, key="QH36b")
        q_rate1(st.session_state.QH36b)
        
        survey.radio('37. Troubles du sommeil, je dors trop ou trop peu, réveil trop matinal', options=list_section_01,index=0, horizontal=True, key="QH37")
        q_rate1(st.session_state.QH37)
        survey.radio("38. Effet aggravant de l'alcool sur l'intensité des symptômes et/ou de la « gueule de bois »", options=list_section_01,index=0,  horizontal=True, key="QH38")
        q_rate1(st.session_state.QH38)       
        # st.session_state
        st.write("Section 1 : Score total = ",st.session_state['rtot']) 
        
        # SECTION 2: MOST COMMON LYME SYMPTOMS SCORE
        # If you rated a 3 for each of the following in section 1, give yourself 5 additional points:
        # 39.(3) Fatigue
        # 40. (33) Forgetfulness, poor short-term memory
        # 41. (41) Joint pain or swelling
        # 42. (24) Tingling, numbness, burning, or stabbing sensations
        # 43. (37)Disturbed sleep: too much, too little, early awakening
        st.session_state.r2_tot = 0
        st.write("Section 2 scores : QH39 =  "+str(st.session_state.QH03))  
        st.write("Section 2 scores : QH40 =  "+str(st.session_state.QH33))  
        st.write("Section 2 scores : QH41 =  "+str(st.session_state.QH18))  
        st.write("Section 2 scores : QH42 =  "+str(st.session_state.QH24))  
        st.write("Section 2 scores : QH43 =  "+str(st.session_state.QH37))  
        
        # ------------ variable applicable only by session --> repeat and adapt variables ---
                
        
        if (q_rate1(st.session_state.QH03) == 3 and q_rate1(st.session_state.QH33) == 3 and q_rate1(st.session_state.QH18) == 3 and q_rate1(st.session_state.QH24) == 3 and q_rate1(st.session_state.QH37) == 3):
            st.session_state.r2_tot = 5
            
        #st.session_state.rtot = st.session_state.rtot + st.session_state.r1_tot + r2_tot   
        
        st.write("Score Total section 1 =  "+str(st.session_state['r1_tot']))  
        st.write("Score Total section 2 =  "+str(st.session_state['r2_tot']))  
                
        #st.write("Score Total current (1+2) =  "+str(st.session_state.rtot))  
        
    # ================================================================================      
    
    elif pages.current == 5:
               
        
        # --------------- SECTION 3 ----------------------------------
                
        #        SECTION 3: LYME INCIDENCE SCORE
        # If true, transpose points
        # here:
        # Now please circle the points for each of the following statements you can agree with:
        # 44. You have had a tick bite with no rash or flulike symptoms. 3 points
        # 45. You have had a tick bite, an erythema migrans, or an undefined rash, followed by flulike
        # symptoms. 5 points
        # 46. You live in what is considered a Lyme-endemic area. 2 points
        # 47. You have a family member who has been diagnosed with Lyme and/or other tick-borne
        # infections. 1 point
        # 48. You experience migratory muscle pain. 4 points
        # 49. You experience migratory joint pain. 4 points
        # 50. You experience tingling/burning/numbness that migrates and/or comes and goes. 4 points
        # 51. You have received a prior diagnosis of chronic fatigue syndrome or fibromyalgia. 3 points
        # 52. You have received a prior diagnosis of a specific autoimmune disorder (lupus, MS, or rheumatoid
        # arthritis), or of a nonspecific autoimmune disorder. 3 points
        # 53. You have had a positive Lyme test (IFA, ELISA, Western blot, PCR, and/or borrelia culture). 5
        # points
        
        
        # SECTION 3: LYME INCIDENCE SCORE
        
        st.header("Page 5 SECTION 3 - Questions sur l'incidence - Score Courant = "+ str(st.session_state.rtot), divider=True) 
        
        list_section_03 = ["Oui", 'Non']
        
        st.session_state.r3_tot = 0
        
        def q_rate3(key):
            if (key == 'QH44a' and st.session_state.QH44a) == list_section_03[0]:
                r3=1
            
            elif (key == 'QH44b' and st.session_state.QH44b) == list_section_03[0]:
                r3=1
                
            elif (key == 'QH44c' and st.session_state.QH44c) == list_section_03[0]:
                r3=1    
                
            #elif (key == 'QH45' and st.session_state.QH45) == list_section_03[0]:
            #    r3=5
            elif (key == 'QH46' and st.session_state.QH46) == list_section_03[0]:
                r3=2
            elif (key == 'QH47' and st.session_state.QH47) == list_section_03[0]:
                r3=1    
            elif (key == 'QH48' and st.session_state.QH48) == list_section_03[0]:
                r3=4
            elif (key == 'QH49' and st.session_state.QH49) == list_section_03[0]:
                r3=4
            elif (key == 'QH50' and st.session_state.QH50) == list_section_03[0]:
                r3=4
            elif (key == 'QH51a' and st.session_state.QH51a) == list_section_03[0]:
                r3=3
            elif (key == 'QH51b' and st.session_state.QH51b) == list_section_03[0]:
                r3=3    
                
            elif (key == 'QH52' and st.session_state.QH52) == list_section_03[0]:
                r3=3
            elif (key == 'QH53' and st.session_state.QH53) == list_section_03[0]:
                r3=5
            else:
                r3 = 0
            
            st.session_state.r3_tot = st.session_state.r3_tot + r3
                
            return
                
        #-----------------------------------------------------
        
         # st.session_state
         # st.session_state
        
               
        survey.radio("44a. J'ai eu une piqûre de tique", options=list_section_03, index=1,  horizontal=True, key="QH44a")
        q_rate3('QH44a')
        
        survey.radio("44b. J'ai eu un érythrème migrant", options=list_section_03, index=1,  horizontal=True, key="QH44b")
        q_rate3('QH44b')
        
        survey.radio("44c. J'ai eu des symptômes grippaux", options=list_section_03, index=1,  horizontal=True, key="QH44c")
        q_rate3('QH44c')
        
        
        #survey.radio("45. J'ai eu une piqûre de tique, AVEC érythème migrant et / ou AVEC symptômes grippaux", options=list_section_03, index=1,  horizontal=True, key="QH45")
        #q_rate3('QH45')
        
        
        
        survey.radio("46. Vous vivez dans une zone considérée comme endémique", options=list_section_03, index=1,  horizontal=True, key="QH46")
        q_rate3('QH46')
        survey.radio("47. Un autre membre de la famille a déjà  été diagnostiqué avec la maladie de Lyme ou une autre infection transmise par les tiques", index=1,  options=list_section_03, horizontal=True, key="QH47")
        q_rate3('QH47')
        survey.radio("48. Vous avez des douleurs musculaires migrantes (qui se déplacent)", options=list_section_03, index=1,  horizontal=True, key="QH48")                                                                                                            
        q_rate3('QH48')
        survey.radio("49. Vous avez des douleurs articulaires migrantes (qui se déplacent)", options=list_section_03, index=1,  horizontal=True, key="QH49")                                                                                                           
        q_rate3('QH49')
        survey.radio("50. Vous ressentez des picotements/ brûlures / engourdissements qui migrent et/ou qui vont et viennent?", options=list_section_03, index=1,  horizontal=True, key="QH50")                                                                                                           
        q_rate3('QH50')
        
        survey.radio("51a. Vous avez déjà reçu un diagnostic de syndrome de fatigue chronique, hypersomnie", options=list_section_03, index=1,  horizontal=True, key="QH51a")                                                                                                           
        q_rate3('QH51a')
        survey.radio("51b. Vous avez déjà reçu un diagnostic de fibromyalgie", options=list_section_03, index=1,  horizontal=True, key="QH51b")                                                                                                           
        q_rate3('QH51b')
        
        survey.radio("52. Vous avez reçu un diagnostic préalable d'une maladie auto-immune spécifique", options=list_section_03, index=1,  horizontal=True, key="QH52")   
        q_rate3('QH52')
        
        st.write("Ref: [lupus, sclérose en plaques ou polyarthrite rhumatoïde, maladie auto-immune non spécifique de type connectivite]")                                                                                                      
        survey.radio("53. Vous avez eu un test de Lyme positif", options=list_section_03, index=1,  horizontal=True, key="QH53") 
        q_rate3('QH53')                                                                                        
    
        
        st.write("Score section 3 =  "+str(st.session_state.r3_tot)) 
        
        
        #st.session_state.rtot = st.session_state.rtot + st.session_state.r3_tot   
        #st.write("Score Total current =  "+str(st.session_state.rtot))  
    # =======================================================================================================================                                                                                                        
# ------------------------------------------------------------------------------------------------------------
                 
    elif pages.current == 6:
        
        
        # -----------------totals of previous section 3---------------------------
        # st.session_state['key'] = 'value'
        
        
        
        # =================================================================================
        
        # 54. Thinking about your overall physical health, for how many of the past thirty days was your
        # physical health not good?________ days
        # Award yourself the following points based on the total number of days:
        # 0–5 days = 1 point
        # 6–12 days = 2 points
        # 13–20 days = 3 points
        # 21–30 days = 4 points
        # 55. Thinking about your overall mental health, for how many days during the past thirty days was your
        # mental health not good?________ days
        # Award yourself the following points based on the total number of days:
        # 0–5 days = 1 point
        # 6–12 days = 2 points
        # 13–20 days = 3 points
        # 21–30 days = 4 points
        
        st.header('Page 6 - Section 4: Score de santé globale', divider=True) 
        list_section_04 = ['0 à 5 jours', '6 à 12 jours','13 à 20 jours', '21 à 30 jours']
        st.session_state['r4'] = 0
        st.session_state['r4_tot'] = 0
        #st.session_state['r4'] = 0
        # st.write("INIT- r4 tot session state =  "+str(st.session_state['r4_tot']))  
        # st.write("INIT- r4   =  "+str(r4))  
        # state = ''
        def q_rate4(state):
            if state == list_section_04[0]:
                # st.session_state['r4'] = 1
                st.session_state['r4']=1
            elif state == list_section_04[1]:
                # st.session_state['r4'] = 2
                st.session_state['r4']=2
            elif state == list_section_04[2]:
                # st.session_state['r4'] = 3
                st.session_state['r4']=3
            
            elif state == list_section_04[3]:
                # st.session_state['r4'] = 4
                st.session_state['r4']=4
            else:
                print('')
                
            #print('r4 = ',st.session_state['r4'])
            st.session_state['r4_tot'] = st.session_state.r4_tot + st.session_state['r4']
            return
        
        survey.radio("54.En ce qui concerne votre santé PHYSIQUE globale, durant combien de temps au cours des trente derniers jours votre santé physique n'était-elle pas bonne ?",
                     options=list_section_04, index=None,  horizontal=True, key="QH54")
        q_rate4(st.session_state.QH54)
        
        survey.radio("55. En ce qui concerne votre santé MENTALE globale,durant combien de jours au cours des trente derniers jours votre santé mentale n'était-­elle pas bonne ?",
                     options=list_section_04, index=None,  horizontal=True, key="QH55")
        q_rate4(st.session_state.QH55)   
        
        # ----------- COMPUTE TOTAL SCORE -----------------------------------------
        st.session_state.rtot = st.session_state.r1_tot + st.session_state.r2_tot + st.session_state.r3_tot + st.session_state.r4_tot 
                
        
        st.write("Score section 4 =  "+str(st.session_state['r4_tot']))  
        st.write("Score Total  (1-4) =  "+str(st.session_state['rtot']))  
        
          
        
        st.text('''
        Résultat indicatif:
                
        - Si votre score est de 46 ou plus, vous présentez une forte probabilité de souffrir 
          d'une maladie transmise par les tiques et devez consulter un professionnel de santé 
          pour une évaluation plus approfondie.
          
        - Si votre score est compris entre 21 et 45, vous souffrez probablement d'une maladie transmise
          par les tiques et devez consulter un professionnel de santé pour une évaluation plus approfondie.
          
        - Si votre score est inférieur à 21, il est peu probable que vous souffriez d'une maladie transmise par les tiques.        
        ''')
        
        # - If you scored 46 or more, you have a high probability of a tick-borne disorder and should see a healthcare
        #   provider for further evaluation.
        # - If you scored between 21 and 45, you possibly have a tick-borne disorder and should see a healthcare
        #   provider for further evaluation.
        # - If you scored under 21, you are not likely to have a tick-borne disorder.
       
            
    elif pages.current == 7:
        
        st.header('Page 7 - Section 5: Questions complémentaires', divider=True) 
           
        st.session_state['Q0060'] = survey.radio("Connaissiez-vous la maladie de Lyme (Borréliose) avant votre première infection ?", options=['Oui', 'Non','Je ne me souviens pas'],index=1,  horizontal=True, key="Q_0060")
        st.session_state['Q0061'] = survey.radio("Connaissiez-vous les éventuelles coinfections (Bartonella, Babesia etc..) avant votre première infection ?", options=['Oui', 'Non','Je ne me souviens pas'],index=1,  horizontal=True, key="Q_0061")
        st.session_state['Q0062'] = survey.radio("Connaissiez-vous les dispositions / précautions nécessaires à  prendre pour éviter le contact avec les tiques ?", options=['Oui', 'Non','Je ne me souviens pas'],index=1,  horizontal=True, key="Q_0062")
        
        st.session_state['Q0063'] = survey.multiselect("Possédez-vous (ou possédiez) des animaux de compagnie ?",
                                    options=['Aucun','Chien','Chat','Autres (mammifères)','Autres (non mammifères)'],
                                    key="Q_0063" )
        
        
        
        
        #st.write("You selected:", animals)
         
        st.session_state['Q0064'] = survey.multiselect("Vos activités sont-elles liées à  : ",
                                        options=['Autres',"l'entretien de zones naturelles ?","l'assistance aux animaux domestiques (SPA, chenils, refuges, ..) ?",'autre',"l'exploitation agricole et animale (bovins etc..) ?",'la foresterie ?'], 
                                        key="Q_0064" )
        
        #st.write("You selected:", activities)

        
    
    
    elif pages.current == 8:
        
        st.header('Page 8 - Lyme Suisse - Questionnaire - Remarques / Commentaires', divider=True) 

        # Strongly Disagree
        # Strongly Agree
        #survey.select_slider("Likert scale:", options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], id="Q2")
        # Area input:

        st.session_state['Q0065'] = survey.text_area("Vos remarques, commentaires : ", key="Q_0065")

        #survey.slider("Slider:", min_value=0, max_value=500, value=50)
        # ---- END OF SURVEY -- SAVE ALL DATA TO FTP FILE ---------------------
        # st.success("Vos réponses sont enregistrées, merci de votre collaboration !")
        
        #submitted = st.form_submit_button("Submit")
        #if submitted:
        
        
        
    elif pages.current == 9:
        
        
          
        # st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", icon=None, width="stretch")
        
        
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        st.write(f"Hostname: {hostname}")
        st.write(f"IP Address: {ip_address}")
      
        # Generate unique ID -> 1 UUID random IDs
        st.session_state['res'] = [str(uuid.uuid4()) for _ in range(2)]
        st.markdown(':blue[UUID :]' + str(st.session_state['res']))
        st.session_state['uuid_short'] = str(st.session_state.res[:8])
        ushort = ''
        ushort = str(st.session_state['res'])
        ushort = ushort[3:9]
        st.session_state['ushort'] = ushort
        st.write('UUID short : '+ st.session_state['uuid_short'])
        st.write('Ushort : '+ st.session_state['ushort'])

        # ----------------------------------------------------------
        today = str(date.today())
        st.session_state['date'] = str(date.today())
        st.write('Date : ',st.session_state['date'])
        # st.write('UUID :' + str(st.session_state['res']))
        
        
        # --------------------------------------------------------------------

        # st.write('date : ',st.session_state["date"])
        # st.write('UUID short : ',st.session_state["uuid_short"])
        # st.write('Age : ',st.session_state["age"])
        
        

        st.session_state["filestr"] = ''  
        st.session_state["filestr"] = 'lymech_survey-'+ str(st.session_state['date']) + '-'+ str(st.session_state['ushort']) + '.json'
        
        st.session_state["filestr_tests"] = ''  
        st.session_state["filestr_tests"] = 'lymech_survey-'+ str(st.session_state['date']) + '-'+ str(st.session_state['ushort']) + '-tests.json'
        
        st.write('Filestr = ',st.session_state["filestr"])
        st.write('filestr_tests = ',st.session_state["filestr_tests"])
        filestr = st.session_state["filestr"]
        filestr_tests = st.session_state["filestr_tests"]
        
        #st.session_state["Q0065b"] = survey.text_input('Votre email (facultatif) :',value='', key = 'Q_0065b')
        st.session_state["Q0066"] = survey.text_input('Date :',value=today, key = 'Q_0066')
        st.session_state["Q0067"] = survey.text_input('Short UUID :',value=ushort, key = 'Q_0067')
        st.session_state["Q0068"] = survey.text_input('Hostname :',value=hostname, key = 'Q_0068')
        st.session_state["Q0069"] = survey.text_input('IP Adress :',value=ip_address, key = 'Q_0069')
        st.session_state["Q0070"] = survey.text_input('Filestr :',value=filestr, key = 'Q_0070')
        st.session_state["Q0071"] = survey.text_input('Filestr_tests :',value=filestr_tests, key = 'Q_0071')
        
        # ---------------- WRITE DATA TO JSON OBJECT -----------------------
        #import streamlit as st
        
        #st.write(st.session_state)
        
        #st.set_page_config(layout="wide")
        
        # edited_df = st.data_editor(st.session_state['survey'], num_rows="dynamic")
        
        # --------------SAVE SESSION STATE DICTIONNARY --------------------------------------------
          
        
        st.write('ST - DICT --> ')
        
        st_dict = {}
        st_dict = {'date':st.session_state['Q0066'],
                   'suuid':st.session_state['Q0067'],
                   'hostname':st.session_state['Q0068'],
                   'ip':st.session_state['Q0069'],
                   'filestr':st.session_state['Q0070'],
                   'filestr_tests':st.session_state['Q0071'],
                   'age':st.session_state['Q0003A'],
                   'sex':st.session_state['Q0003B'],
                   'canton':st.session_state['Q0004'],
                   'animals':st.session_state['Q0063'],
                   'activites':st.session_state['Q0064'],
                   'duration_illness':st.session_state['Q0005'],
                   'duration_med_wand':st.session_state['Q0006'],
                   'duration_first_diag':st.session_state['Q0007'],
                   'diag_ch':st.session_state['Q0008a'],
                   'diag_abroad':st.session_state['Q0008b'],
                   'test_abroad':st.session_state['Q0010'],
                   'rtot':st.session_state['rtot'],
                   'r1_tot':st.session_state['r1_tot'],
                   'r2_tot':st.session_state['r2_tot'],
                   'r3_tot':st.session_state['r3_tot'],
                   'r4_tot':st.session_state['r4_tot'],
                   'num_rows_ch':st.session_state['num_rows_ch'],
                   'num_rows_nch':st.session_state['num_rows_nch'],
                   'nb_col_ch':st.session_state['nb_col_ch'],
                   'nb_col_nch':st.session_state['nb_col_nch'],                  
                   }
        
                
        for i in range(0,st.session_state['nb_max_row_qch']):
            for j in range(1,st.session_state['nb_col_ch']):
                #st.write('st session state ch -> : ',st.session_state[f'test_ch_r{i}_c{j}'] )
                # st.write('push to scoredict..')
                st_dict.update({
                    f'test_ch_r{i}_c{j}':st.session_state[f'test_ch_r{i}_c{j}'],})
                
                                
        for i in range(0,st.session_state['nb_max_row_nqch']):
            for j in range(1,st.session_state['nb_col_nch']):
                # st.write('st session state nch -> : ',st.session_state[f'test_nch_r{i}_c{j}'] )
                # st.write('push to scoredict..')
                st_dict.update({
                    f'test_nch_r{i}_c{j}':st.session_state[f'test_nch_r{i}_c{j}'],})
        
        
        
        
        # for key, value in st_dict.items():
        #     st.write('key = ',key,'   value = ', value)
        
        # st.write('write full dict -> ')
        # st.write(st_dict)
        
        st.write('============ write TEST DICT TO FILE ======================')
                       
        # ------------save locally (only for testing)----------------------------------------        
        # path_dict = "D:/_00_LYME_CH/data/lyme_ch_questionnaire/"
        # filedir = path_json +  st.session_state["filestr_tests"]
        
        # save session state dict to file
        
        # writing dictionary to a file as JSON
        # with open(filedir, 'w') as f:
        #     json.dump(st_dict, f)
        
        

        # --- CREATE TO FILES (JSON DICT FILES) INTO MEMORY--------------------
        st.write('CREATE FIRST FILE----------------')
        data = survey.to_json()
        json_str = json.dumps(data, indent=4)
        
        with open(st.session_state["filestr"], "w") as f1:
            #f.write(json_str)
            f1.write(json_str)
            

        # --- CREATE TEST DATA FILE  --------------------
        st.write('CREATE SECOND FILE----------------')
        json_str_2 = json.dumps(st_dict, indent=4)
        
        with open(st.session_state["filestr_tests"], "w") as f2:
            #f.write(json_str)
            f2.write(json_str_2)
        
        
        # -------------OPEN FTP CONNEXTION -----------------------


        # Create an FTP object and connect to the server
        # LOGIN TO FTP SERVER
        ftpObject = FTP('279.hosttech.eu','algolabs.ch','t4HVn_7ig6yd');
        print(ftpObject.getwelcome());
        # ======= FTP DESTINATION FOLDER ===========================
        ftpResponseMessage = ftpObject.cwd("/lyme-ch.algolabs.ch/questionnaire");
        st.write(ftpResponseMessage);
        
        # ------------UPLOAD FIRST FILE -----------------------
        filepath = st.session_state["filestr"]
        st.write('filepath  = ',filepath)
        
        # fileObject = open(filedir, "rb");
        fileObject = open(filepath, "rb");

        file2BeSavedAs = st.session_state["filestr"]
        ftpCommand = "STOR %s"%file2BeSavedAs;
        # Transfer the file in binary mode
        ftpResponseMessage = ftpObject.storbinary(ftpCommand, fp=fileObject);
        st.write(ftpResponseMessage);
        
        
        # ------------UPLOAD SECOND FILE - TEST DATA ------------------
        
        # ======= FTP DESTINATION FOLDER ===========================
        ftpResponseMessage = ftpObject.cwd("/lyme-ch.algolabs.ch/questionnaire_tests");
        st.write(ftpResponseMessage);     
        
        st.write('SAVE ON FTP SERVER -> Save  LYME TESTS data........')
        
        filepath_tests = st.session_state["filestr_tests"]
        st.write('filepath_tests  = ',filepath_tests)
        # fileObject = open(filedir, "rb");
        fileObject = open(filepath_tests, "rb");
        
        # [Errno 2] No such file or directory: 'lymech_survey-2025-10-06-867d48-tests.json'
        # Traceback:
        # File "D:\_00_LYME_CH\data\lyme_ch_questionnaire\test_lyme_ch_questionnaire_streamlit_v2.py", line 1141, in <module>
        #     fileObject = open(filepath_tests, "rb");


        file2BeSavedAs = st.session_state["filestr_tests"]
        ftpCommand = "STOR %s"%file2BeSavedAs;
        # Transfer the file in binary mode
        ftpResponseMessage = ftpObject.storbinary(ftpCommand, fp=fileObject);
        st.write(ftpResponseMessage);
        
        
        # ----------- REDIRECT TO ANOTHER URL -----------------
        
        #import streamlit.components.v1 as components
        
        # embed streamlit docs in a streamlit app
        # st.components.v1.iframe(src, width=None, height=None, scrolling=False, *, tab_index=None)
        
        #components.iframe("https://www.lyme.ch", width=1600, height=1600, scrolling=True)
        
        
        # ---- SUBMITTED FINAL DATA AND PROCEDURE -------------------
        ## getting the hostname by socket.gethostname() method
        st.success("Vos réponses sont enregistrées, merci de votre collaboration !")
        
        st.stop()
        #if st.button("Quit Survey"):
        #    st.markdown("""<meta http-equiv="refresh" content="0; url='https://www.lyme.ch'" />""", unsafe_allow_html=True)
        
        

    else: # --- last page upload all json data to ftp file ------------------
        print('end -> all answered')     
        

        
       
                                                                                              
# ============= DISPLAYED ON FOOTER PAGES ====================

def survey_init(key):
    if key not in st.session_state:
        #st.write('key : ',key,'  is empty')
        st.session_state[key] = ''
    return
    
list_key_0 = ['date','uuid_short','age','ushort',]

for lk0 in list_key_0:
    survey_init(lk0)
 


def survey_init_dict(key):
    if key not in st.session_state:
        #st.write('key : ',key,'  is empty')
        st.session_state[key] = ''
    return
    
list_key_0 = ['date','uuid_short','age','ushort',]

for lk0 in list_key_0:
    survey_init(lk0)

# --- init INTEGER sliders CH AND NON CH -------------

def survey_init_int(key):
    if key not in st.session_state:
        #st.write('key : ',key,'  is empty')
        st.session_state[key] = 1
    return


#survey_init_int('s1_num_rows_ch')
survey_init_int('num_rows_ch')
survey_init_int('num_rows_nch')
survey_init_int('nb_max_row_qch')
survey_init_int('nb_max_row_nqch')
survey_init_int('nb_col_ch')
survey_init_int('nb_col_nch')


def survey_init_0(key):
    if key not in st.session_state:
        #st.write('key : ',key,'  is empty')
        st.session_state[key] = 0
    return

survey_init_0('rtot')
survey_init_0('r1_tot')
survey_init_0('r2_tot')
survey_init_0('r3_tot')
survey_init_0('r4_tot')


# ---------------- INITIALIZE SESSION DICT --------------------------

# init data session_state for H questionnaire ------    
st.session_state['nb_max_row_qch'] = 10
st.session_state['nb_max_row_nqch'] = 10
st.session_state['nb_col_ch'] = 4
st.session_state['nb_col_nch'] = 5

for i in range(0,st.session_state['nb_max_row_qch']):
    for j in range(1,st.session_state['nb_col_ch']):
        print(i,' , ',j,' ',f'test_chr{i}_c{j}')
        survey_init(f'test_ch_r{i}_c{j}')
    


for i in range(0,st.session_state['nb_max_row_nqch']):
    for j in range(1,st.session_state['nb_col_nch']):
        print(i,' , ',j,' ',f'test_nchr{i}_c{j}')
        survey_init(f'test_nch_r{i}_c{j}')






# ------------- init session state dictionnary ---------------



# ------------------------------------------------------------------
# st.write('st session state - nb max row qch = ',st.session_state['nb_max_row_qch'])
# st.write('st session state - nb_col_ch = ',st.session_state['nb_col_ch'])

# st.write('st session state - nb max row nqch = ',st.session_state['nb_max_row_nqch'])
# st.write('st session state - nb_col_nch = ',st.session_state['nb_col_nch'])





# st.write('st session state ch test_ch_r0_c1 -> : ',st.session_state[f'test_ch_r0_c1'] )
# st.write('st session state ch test_ch_r0_c2 -> : ',st.session_state[f'test_ch_r0_c2'] )
# st.write('st session state ch test_ch_r0_c3 -> : ',st.session_state[f'test_ch_r0_c3'] )

# st.write('st session state ch test_ch_r1_c1 -> : ',st.session_state[f'test_ch_r1_c1'] )
# st.write('st session state ch test_ch_r1_c2 -> : ',st.session_state[f'test_ch_r1_c2'] )
# st.write('st session state ch test_ch_r1_c3 -> : ',st.session_state[f'test_ch_r1_c3'] )

# st.write('st session state ch test_ch_r2_c1 -> : ',st.session_state[f'test_ch_r2_c1'] )
# st.write('st session state ch test_ch_r2_c2 -> : ',st.session_state[f'test_ch_r2_c2'] )
# st.write('st session state ch test_ch_r2_c3 -> : ',st.session_state[f'test_ch_r2_c3'] )


# st.write('st session state ch test_nch_r0_c1 -> : ',st.session_state[f'test_nch_r0_c1'] )
# st.write('st session state ch test_nch_r0_c2 -> : ',st.session_state[f'test_nch_r0_c2'] )
# st.write('st session state ch test_nch_r0_c3 -> : ',st.session_state[f'test_nch_r0_c3'] )

# ------------- init session state dictionnary ---------------




# The survey automatically gives each component a unique ID. Survey component labels and 
# values are stored in the survey.data dictionary, which can be saved to a JSON 
# file using the survey.to_json method:

    
# Session State is a way to share variables between reruns, 
# for each user session. In addition to the ability to store
#  and persist state, Streamlit also exposes the ability to manipulate
#  state using Callbacks. Session state also persists across apps inside a multipage app.

# ---- SHOW VISITOR IP ADDRESS ----------------------------------

## importing socket module
# import socket
## getting the hostname by socket.gethostname() method
# hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
# ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
# print(f"Hostname: {hostname}")
# print(f"IP Address: {ip_address}")

# st.write(f"Hostname: {hostname}")
# st.write(f"IP Address: {ip_address}")



# import web

# class index:
#     def GET(self):
#         print web.ctx['ip'] 
#         return web.ctx['ip']
    






# Generate unique ID -> 1 UUID random IDs
# import uuid
# st.session_state['res'] = [str(uuid.uuid4()) for _ in range(2)]
# st.markdown(':blue[UUID :]' + str(st.session_state['res']))



# st.session_state['uuid_short'] = str(st.session_state.res[:8])
# ushort = ''
# ushort = str(st.session_state['res'])
# ushort = ushort[3:9]

# st.session_state['ushort'] = ushort
 
# st.write('UUID short : '+ st.session_state['uuid_short'])
# st.write('Ushort : '+ st.session_state['ushort'])

# ----------------------------------------------------------
# from datetime import date
# st.session_state['date'] = str(date.today())
# st.write('Date : ',st.session_state['date'])
# st.write('UUID :' + str(st.session_state['res']))
 

# --------------------------------------------------------------------

# st.session_state['uuid short'] = str(st.session_state.res)[:8]



# st.write('date : ',st.session_state["date"])
# st.write('UUID short : ',st.session_state["uuid_short"])
# st.write('Age : ',st.session_state["age"])











# import json
# data = survey.to_json()
# st.json(json)


# data = {
#     "name": "ALGOLABS",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phone": "9976770500"
# }



# json_str = json.dumps(data, indent=4)




# st.session_state["filestr"] = ''  

# st.session_state["filestr"] = 'lymech_survey-'+ str(st.session_state['date']) + '-'+ str(st.session_state['ushort']) + '-'+ str(st.session_state['age'])



# st.write('Filestr = ',st.session_state["filestr"])








# ================================================================================

# with open(st.session_state["filestr"], "w") as f:
#     f.write(json_str)


# ================== UPLOAD FILE TO FTP SERVER ==========================

# ============= HOSTTECH CONFIGURATION =============================
# ---------------------------------------------------------------------------
# FTP Zugangsdaten (algolabs.ch)
# FTP Host / Server 279.hosttech.eu
# Benutzername algolabs.ch (in Plesk änderbar)
# Passwort t4HVn_7ig6yd (in Plesk änderbar)
# Startverzeichnis /httpdocs
# Port 21
# Um Daten auf deinen Server hochzuladen, nutze bitte
# die FTP-Zugangsdaten. Du kannst für den Upload entweder
# unser WebFTP nutzen (im Control Panel Plesk) oder einen
# externen FTP Client verwenden.

# --------------------------------------------------------------------

# Home directory
# lyme-ch.algolabs.ch
# questionnaire

# in binary mode

# from ftplib import FTP
# Create an FTP object and connect to the server
# LOGIN TO FTP SERVER

# ftpObject = FTP('279.hosttech.eu','algolabs.ch','t4HVn_7ig6yd');
# print(ftpObject.getwelcome());

# ======= FTP DESTINATION FOLDER ===========================
# ftpResponseMessage = ftpObject.cwd("/lyme-ch.algolabs.ch/questionnaire");

# print(ftpResponseMessage);
# 250 CWD command successfULL 

# Open the file in binary mode
# ----------- SEARCH FILE ---------------
# path_json = "D:/_00_LYME_CH/data/lyme_ch_questionnaire/"
# filedir = path_json + 'lyme_ch_data_quest.json'
# file = open(filedir,'rb')                  # file to send

# filepath = st.session_state["filestr"]
# fileObject = open(filedir, "rb");
# fileObject = open(filepath, "rb");

# file2BeSavedAs = st.session_state["filestr"]

# ftpCommand = "STOR %s"%file2BeSavedAs;

# Transfer the file in binary mode
# ftpResponseMessage = ftpObject.storbinary(ftpCommand, fp=fileObject);

# print(ftpResponseMessage);


# Python 3 -------- USE THIS TO RETRIEVE FILE FROM FTP --------------------

# import urllib.request

# urllib.request.urlretrieve('ftp://server/path/to/file', 'file')


# ======================================================================================
# ======================================================================================
# ======================================================================================







