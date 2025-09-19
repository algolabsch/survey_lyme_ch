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
# python -m streamlit run D:\_00_LYME_CH\data\lyme_ch_questionnaire\test_lyme_ch_questionnaire_streamlit.py


# ======================================================================

import streamlit as st
import pandas as pd
import numpy as np
import socket
import uuid
from datetime import date
import json
from ftplib import FTP

#st.title('Lyme Suisse - Questionnaire')


import streamlit_survey as ss

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

st.session_state["date"] = ''
st.session_state["uuid_short"] = ''
st.session_state["age"] = '' 
st.session_state['ushort']=''  

# ---- DEFINE ON SUBMIT FUNCTION ---------------------------
# def submitted():

    


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
        
    st.sidebar.header("Distribution of the 3-B species")
    st.sidebar.text("(Borrelia-Bartonella-Babesia)")
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
    
    
    
    
    
    
    if st.button("Quit Survey"):
        st.markdown("""<meta http-equiv="refresh" content="0; url='https://www.lyme.ch/en'" />""", unsafe_allow_html=True)
    #button[kind="primary"] {background-color: red;}
    
    # Babesia distribution map
    # https://www.frontiersin.org/files/Articles/474717/fevo-07-00401-HTML/image_m/fevo-07-00401-g002.jpg
    img_link = "https://www.frontiersin.org/files/Articles/474717/fevo-07-00401-HTML/image_m/"
    img_image = "fevo-07-00401-g002.jpg"

    st.image(img_link+img_image, caption="Borrelia distribution map")
    
    # Borrelia distribution map
    # https://www.frontiersin.org/files/Articles/474717/fevo-07-00401-HTML/image_m/fevo-07-00401-g002.jpg
    img_link = "https://www.mdpi.com/pathogens/pathogens-10-00230/article_deploy/html/images/"
    img_image = "pathogens-10-00230-g007.png"

    st.image(img_link+img_image, caption="Babesia distribution map")
    
    # Bartonella distribution map
    # https://parasitesandvectors.biomedcentral.com/articles/10.1186/s13071-018-3152-6/figures/1
    # 13071_2018_3152_Fig1_HTML.webp
    img_link = "https://parasitesandvectors.biomedcentral.com/articles/10.1186/s13071-018-3152-6/figures/1"
    #img_image = "13071_2018_3152_Fig1_HTML.webp"

    st.image(img_link, caption="Bartonalla distribution map")




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




with pages:
    
        
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
        
        
        
        survey.radio("Avez-vous déjà  complété ce formulaire sur notre site (www.lyme.ch) ?*", 
                     options=["Oui", "Non"], 
                     index=None, 
                     #label_visibility="collapsed",
                     key = 'Q_0001',
                     horizontal=True)
        
        
        survey.radio('''Autorisez-vous Lyme Suisse à  utiliser vos réponses pour des raisons analytiques (Recherche)?*''', 
                     options=["Oui", "Non"], 
                     index=None, 
                     key = 'Q_0002',
                     horizontal=True)
        
        
    elif pages.current == 1:
        st.header('page 1 - Informations générales', divider=True)
        
        st.session_state['age'] = survey.number_input('Quel est votre âge ?*')
        # ---------------------------------------------
        
        survey.radio('Votre sexe ?*', 
                     options=["Masculin", "Féminin","Autre"],
                     index=None,  
                     key = 'Q_0003',
                     horizontal=True)
        
        #st.write('Votre âge : ', number)
        #survey.selectbox("Selection box:", options=["Option 1", "Option 2", "Option 3", "etc"])
        #st.selectbox('Quel est votre lieu (canton) de résidence ?*',("Vaud", "Fribourg", "Neuchâtel",'Genève','Bern','Tessin','Bern', 'Hors Suisse'))
        st.selectbox('Quel est votre canton de résidence ?*', 
                     options=["Vaud", "Fribourg", "Neuchâtel",'Genève','Bern','Tessin','Bern', 'Hors Suisse'],
                     index=None,  
                     key = 'Q_0004')
        #st.write("You selected:", option)
  
    elif pages.current == 2: 
        st.header('Page 2 - Diagnostiques tests effectués en Suisse', divider=True)
        #st.title('Diagnostiques, tests - page 2')
        
        
        survey.number_input('Durée de la maladie (en années): *',
                            key = 'Q_0005')
        survey.number_input("Durée de l'errance  médicale (en années): *",
                            key = 'Q_0006')
        
        survey.slider("Nb d'année jusqu'au premier diagnostique (en années) ", 
                      min_value=1, 
                      max_value=50,
                      key = 'Q_0007')
        
        # survey.multiselect("Multiple choice:", options=["Option 1", "Option 2", "Option 3", "etc"])
        
        survey.multiselect("Avez-vous, EN SUISSE, reçu des diagnostics différents de la maladie de Lyme ou co-infections (complétez ci-dessous) ?",
                           options=['Fibromyalgie','Syndrome de fatigue chronique', 'Troubles psychosomatiques','Autres maladies infectieuses',
                                    'Maladie auto-immune','Dépression','Troubles anxieux',"Thada", "Autisme", "Dépression",
                                    "Schizophrénie",'Psychoses','Autre','Non'],
                           key = 'Q_0008')
        
        survey.multiselect("Avez-vous, à l'étranger (HORS SUISSE), reçu des diagnostics différents de la maladie de Lyme ou co-infections (complétez ci-dessous) ?",
                           options=['Fibromyalgie','Syndrome de fatigue chronique', 'Troubles psychosomatiques','Autres maladies infectieuses',
                                    'Maladie auto-immune','Dépression','Troubles anxieux',"Thada", "Autisme", "Dépression",
                                    "Schizophrénie",'Psychoses','Autre','Non'],
                           key = 'Q_0009')
        
        #st.write("You selected:", diags_other)
        
        # ------------ diagnostic in Switzerland ---------------------------
        st.write("Utilisez cette barre pour indiquer le nombre de tests effectués (EN SUISSE), et complétez le tableau ci-dessous")   


        # a selection for the user to specify the number of rows
        st.session_state.num_rows_ch = st.slider('CH - Number of rows', min_value=1, max_value=10)
        
        # columns to lay out the inputs
        grid = st.columns(4)
        
        # Function to create a row of widgets (with row number input to assure unique keys)
        def add_row(row):
                            
            with grid[0]:
                
                survey.selectbox("Pathogène recherché", 
                             options=['Borrelia','Bartonella','Babesia','encephalitis virus (TBE-V)','Anaplasma','Rickettsia','Ehrlichia',
                                      'Autre virus','Autre parasite','Autre Bacteria'],
                                      index=None,
                                      key=f'input_col1_ch{row}')
                
                
            with grid[1]:
                survey.selectbox('Test effectué',
                             options=['ELISA', 'Western Blot','IFA','PCR','Elispot','FISH','Immunoblot','Culture','Autre'],
                             index=None,
                             key=f'input_col2_ch{row}')
                             #placeholder="Select contact method..." )
                                      
            with grid[2]:
                survey.selectbox('Résultat des tests',
                                  options=['Positif', 'Négatif','Indéterminé'],
                                  index=None,
                                  key=f'input_col3_ch{row}')

#TypeError: RadioMixin.radio() got an unexpected keyword argument 'step'        

# Loop to create rows of input widgets
        for r in range(st.session_state.num_rows_ch):
            add_row(r)                                                                                                   
                
        # ============================================================================
        
        
        
        # ----------------------------------------------------------------
    # ================================================================================  
    
    elif pages.current == 3:
       
        st.header("Page 3 - Diagnostiques tests effectués à l'étranger", divider=True)       
      
        
        #nb_timetoget_diagnostic = survey.number_input("Délais pour établir vos diagnostics (en mois) ? ")
        #2survey.number_input("Délais pour établir vos diagnostics (en mois) ? ", min_value=0, max_value=50, value=1)
        # a selection for the user to specify the number of rows
        
        
        
        survey.radio('''Avez-vous effectué des tests privés (à l'étranger par ex.) et reçu un diagnostic clair de maladie de Lyme
                                      (et/ou de coinfections éventuelles) par un laboratoire ou un médecin ?''',
                                      options=['Oui', 'Non'], index=None,  
                                      key = 'private_tests',
                                      horizontal=True)
        
        
        #PrÃ©cisez les rÃ©sultats et types de tests effectuÃ©s :  
        st.write("Utilisez cette barre pour indiquer le nombre de tests effectués (A L'ETRANGER), et complétez le tableau ci-dessous")   


        # a selection for the user to specify the number of rows
        st.session_state.num_rows_nch = st.slider('NON CH - Number of rows', min_value=1, max_value=10)
        
        # columns to lay out the inputs
        grid = st.columns(4,gap="medium", vertical_alignment="top", border=True)
        
        # Function to create a row of widgets (with row number input to assure unique keys)
        def add_row(row):
                            
            with grid[0]:
                #survey.radio('Pathogène', options=['Borrelia', 'encephalitis virus (TBE-V)','Bartonella','Babesia','Anaplasma','Rickettsia','Ehrlichia','Autre virus','Autre parasite','Autre Bacteria'], 
                #             horizontal=True, 
                #             key=f'input_col1_nch{row}')
                st.selectbox("Pathogène recherché",
                            ('Borrelia','Bartonella','Babesia','encephalitis virus (TBE-V)','Anaplasma','Rickettsia','Ehrlichia','Autre virus','Autre parasite','Autre Bacteria'),
                             index=None,
                             key=f'input_col1_nch{row}')
                             #placeholder="Select contact method..." )
                        
            with grid[1]:
                
                st.selectbox('Test effectué',
                            ('ELISA', 'Western Blot','IFA','PCR','Elispot','FISH','Immunoblot','Culture','Autre'),
                             index=None,
                             key=f'input_col2_nch{row}')
                             #placeholder="Select contact method..." )
                
                
            with grid[2]:
                
                st.selectbox('Résultat des tests',
                            ('Positif', 'Négatif','Indéterminé'),
                             index=None,
                             key=f'input_col3_nch{row}')
                             #placeholder="Select contact method..." )
                
             
            with grid[3]:
                
                st.selectbox('Test effectués en (Région, pays)',
                            ('Suisse', 'EU (hors Suisse)','USA','Autre'),
                             index=None,
                             key=f'input_col4_nch{row}')
                             #placeholder="Select contact method..." )    
             
#TypeError: RadioMixin.radio() got an unexpected keyword argument 'step'        

# Loop to create rows of input widgets
        for r in range(st.session_state.num_rows_nch):
            add_row(r)                                                                                                                                      
  
    # ================================================================================      
    
     
    elif pages.current == 4:
        
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
        
                    
        
        survey.radio('1. Fièvre, sueurs inexpliqués', options=list_section_01, index=0, horizontal=True, key="Q01")
        q_rate1(st.session_state.Q01)
        #st.write("Q01 = ",Q01)   
        #st.write("LIST SECTION 1 / 0 = ",list_section_01[0])   
        # Read
        #st.write(st.session_state.Q01)        
        
        survey.radio('2. Changement de poids inexpliqué (perte ou prise)', options=list_section_01,index=0, horizontal=True, key="Q02")
        #st.write(st.session_state.Q02)  
        q_rate1(st.session_state.Q02)
               
        survey.radio('3. Fatigue', options=list_section_01, index=0,horizontal=True, key="Q03")
        q_rate1(st.session_state.Q03)
        survey.radio('4. Perte de cheveux inexpliquée', options=list_section_01,index=0, horizontal=True, key="Q04")
        q_rate1(st.session_state.Q04)
        survey.radio('5. Ganglions gonflés', options=list_section_01,index=0, horizontal=True, key="Q05")
        q_rate1(st.session_state.Q05)
        survey.radio('6. Maux de gorge', options=list_section_01,index=0, horizontal=True, key="Q06")
        q_rate1(st.session_state.Q06)
        survey.radio('7. Douleurs testiculaires ou pelviennes', options=list_section_01,index=0, horizontal=True, key="Q07")
        q_rate1(st.session_state.Q07)
        survey.radio('8. Règles irrégulières sans raison apparente', options=list_section_01,index=0, horizontal=True, key="Q08")
        q_rate1(st.session_state.Q08)
        survey.radio('9. Lactation inexpliquée, douleurs mammaires', options=list_section_01,index=0, horizontal=True, key="Q09")
        q_rate1(st.session_state.Q09)
        survey.radio('10. Vessie irritable ou dysfonctionnement urinaire', options=list_section_01,index=0, horizontal=True, key="Q10")
        q_rate1(st.session_state.Q10)
        survey.radio('11. Troubles sexuels, perte de libido', options=list_section_01,index=0, horizontal=True, key="Q11")
        q_rate1(st.session_state.Q11)
        survey.radio("12. Maux d'estomac, indigestions", options=list_section_01, index=0,horizontal=True, key="Q12")
        q_rate1(st.session_state.Q12)
        survey.radio('13. Constipation ou diarrhée', options=list_section_01,index=0, horizontal=True, key="Q13")
        q_rate1(st.session_state.Q13)
        survey.radio('14. Douleurs thoraciques ou intercostales', options=list_section_01,index=0, horizontal=True, key="Q14")
        q_rate1(st.session_state.Q14)
        survey.radio('15. Essoufflement, toux', options=list_section_01,index=0, horizontal=True, key="Q15")                                                         
        q_rate1(st.session_state.Q15)
        survey.radio('16. Palpitations, arythmies cardiaques', options=list_section_01, index=0,horizontal=True, key="Q16")
        q_rate1(st.session_state.Q16)
        survey.radio("17. Antécédents de souffle cardiaque ou d'atteinte valvulaire", options=list_section_01,index=0, horizontal=True, key="Q17")
        q_rate1(st.session_state.Q17)
        survey.radio("18. Douleur ou gonflement d'une ou plusieurs articulations", options=list_section_01,index=0, horizontal=True, key="Q18")                                                                 
        q_rate1(st.session_state.Q18)
        survey.radio('19. Raideur de la nuque ou du dos', options=list_section_01, index=0,horizontal=True, key="Q19")        
        q_rate1(st.session_state.Q19)
        survey.radio('20. Douleurs musculaires ou crampes', options=list_section_01, index=0,horizontal=True, key="Q20")
        q_rate1(st.session_state.Q20)
        survey.radio('21. Tressautement des muscles du visage ou du reste du corps (fasciculations)', options=list_section_01,index=0, horizontal=True, key="Q21")  
        q_rate1(st.session_state.Q21)
        survey.radio('22. Maux de tête',options=list_section_01,index=0, horizontal=True, key="Q22")
        q_rate1(st.session_state.Q22)
        survey.radio('23. Craquements dans le cou', options=list_section_01,index=0, horizontal=True, key="Q23")
        q_rate1(st.session_state.Q23)
        survey.radio('24. Fourmillements, engourdissements, sensations de brûlure ou de « coup de poignard » (paresthésies)', options=list_section_01, index=0,horizontal=True, key="Q24")                                                               
        q_rate1(st.session_state.Q24)
        survey.radio('25. Paralysie faciale', options=list_section_01,index=0, horizontal=True, key="Q25")
        q_rate1(st.session_state.Q25)
        survey.radio('26. Vision double ou floue', options=list_section_01,index=0, horizontal=True, key="Q26")
        q_rate1(st.session_state.Q26)
        survey.radio('27. Audition/oreilles : Bourdonnements, sifflements ou douleur dans les oreilles (acouphènes)', options=list_section_01,index=0, horizontal=True, key="Q27")
        q_rate1(st.session_state.Q27)
        survey.radio('28. Mal des transports accru, vertige', options=list_section_01,index=0, horizontal=True, key="Q28")
        q_rate1(st.session_state.Q28)
        survey.radio("29. Etourdissements, manque d'équilibre, difficultés Ã  marcher", options=list_section_01,index=0, horizontal=True, key="Q29")
        q_rate1(st.session_state.Q29)
        survey.radio('30. Tremblements', options=list_section_01,index=0, horizontal=True, key="Q30")
        q_rate1(st.session_state.Q30)
        survey.radio('31. Confusion, difficultés à penser', options=list_section_01,index=0, horizontal=True, key="Q31")
        q_rate1(st.session_state.Q31)
        survey.radio('32. Difficulté à se concentrer ou à  lire', options=list_section_01, index=0,horizontal=True, key="Q32")
        q_rate1(st.session_state.Q32)
        survey.radio('33. Oublis, mauvaise mémoire à court terme', options=list_section_01,index=0, horizontal=True, key="Q33")
        q_rate1(st.session_state.Q33)
        survey.radio('34. Désorientation ; je me perds ou je ne vais pas au bon endroit', options=list_section_01,index=0, horizontal=True, key="Q34")
        q_rate1(st.session_state.Q34)
        survey.radio('35. Difficulté à parler ou à écrire', options=list_section_01,index=0, horizontal=True, key="Q35")
        q_rate1(st.session_state.Q35)
        survey.radio("36. Sautes d'humeur, irritabilité, dépression", options=list_section_01,index=0, horizontal=True, key="Q36")
        q_rate1(st.session_state.Q36)
        survey.radio('37. Troubles du sommeil, je dors trop ou trop peu, réveil trop matinal', options=list_section_01,index=0, horizontal=True, key="Q37")
        q_rate1(st.session_state.Q37)
        survey.radio("38. Effet aggravant de l'alcool sur l'intensité des symptômes et/ou de la « gueule de bois »", options=list_section_01,index=0,  horizontal=True, key="Q38")
        q_rate1(st.session_state.Q38)       
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
        st.write("Section 2 scores : Q39 =  "+str(st.session_state.Q03))  
        st.write("Section 2 scores : Q40 =  "+str(st.session_state.Q33))  
        st.write("Section 2 scores : Q41 =  "+str(st.session_state.Q18))  
        st.write("Section 2 scores : Q42 =  "+str(st.session_state.Q24))  
        st.write("Section 2 scores : Q43 =  "+str(st.session_state.Q37))  
        
        # ------------ variable applicable only by session --> repeat and adapt variables ---
                
        
        if (q_rate1(st.session_state.Q03) == 3 and q_rate1(st.session_state.Q33) == 3 and q_rate1(st.session_state.Q18) == 3 and q_rate1(st.session_state.Q24) == 3 and q_rate1(st.session_state.Q37) == 3):
            st.session_state.r2_tot = 5
            
        #st.session_state.rtot = st.session_state.rtot + st.session_state.r1_tot + r2_tot   
        
        st.write("Score Total at section 1 =  "+str(st.session_state['r1_tot']))  
        st.write("Score Total at section 2 =  "+str(st.session_state['r2_tot']))  
                
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
            if (key == 'Q44' and st.session_state.Q44) == list_section_03[0]:
                r3=3
            elif (key == 'Q45' and st.session_state.Q45) == list_section_03[0]:
                r3=5
            elif (key == 'Q46' and st.session_state.Q46) == list_section_03[0]:
                r3=2
            elif (key == 'Q47' and st.session_state.Q47) == list_section_03[0]:
                r3=1    
            elif (key == 'Q48' and st.session_state.Q48) == list_section_03[0]:
                r3=4
            elif (key == 'Q49' and st.session_state.Q49) == list_section_03[0]:
                r3=4
            elif (key == 'Q50' and st.session_state.Q50) == list_section_03[0]:
                r3=4
            elif (key == 'Q51' and st.session_state.Q51) == list_section_03[0]:
                r3=3
            elif (key == 'Q52' and st.session_state.Q52) == list_section_03[0]:
                r3=3
            elif (key == 'Q53' and st.session_state.Q53) == list_section_03[0]:
                r3=5
            else:
                r3 = 0
            
            st.session_state.r3_tot = st.session_state.r3_tot + r3
                
            return
                
        #-----------------------------------------------------
        
         # st.session_state
         # st.session_state
        
               
        survey.radio("44. J'ai eu une piqûre de tique, SANS érythrème migrant et SANS symptômes grippaux", options=list_section_03, index=1,  horizontal=True, key="Q44")
        q_rate3('Q44')
        survey.radio("45. J'ai eu une piqûre de tique, AVEC érythème migrant et / ou AVEC symptômes grippaux", options=list_section_03, index=1,  horizontal=True, key="Q45")
        q_rate3('Q45')
        survey.radio("46. Vous vivez dans une zone considérée comme endémique", options=list_section_03, index=1,  horizontal=True, key="Q46")
        q_rate3('Q46')
        survey.radio("47. Un autre membre de la famille a déjà  été diagnostiqué avec la maladie de Lyme ou une autre infection transmise par les tiques", index=1,  options=list_section_03, horizontal=True, key="Q47")
        q_rate3('Q47')
        survey.radio("48. Vous avez des douleurs musculaires migrantes (qui se déplacent)", options=list_section_03, index=1,  horizontal=True, key="Q48")                                                                                                            
        q_rate3('Q48')
        survey.radio("49. Vous avez des douleurs articulaires migrantes (qui se déplacent)", options=list_section_03, index=1,  horizontal=True, key="Q49")                                                                                                           
        q_rate3('Q49')
        survey.radio("50. Vous ressentez des picotements/ brûlures / engourdissements qui migrent et/ou qui vont et viennent?", options=list_section_03, index=1,  horizontal=True, key="Q50")                                                                                                           
        q_rate3('Q50')
        survey.radio("51. Vous avez déjà  reçu un diagnostic de syndrome de fatigue chronique ou de fibromyalgie", options=list_section_03, index=1,  horizontal=True, key="Q51")                                                                                                           
        q_rate3('Q51')
        survey.radio("52. Vous avez reçu un diagnostic préalable d'une maladie auto-immune spécifique", options=list_section_03, index=1,  horizontal=True, key="Q52")   
        q_rate3('Q52')
        st.write("Ref: [lupus, sclérose en plaques ou polyarthrite rhumatoïde, maladie auto-immune non spécifique de type connectivite]")                                                                                                      
        survey.radio("53. Vous avez eu un test de Lyme positif", options=list_section_03, index=1,  horizontal=True, key="Q53") 
        q_rate3('Q53')                                                                                        
    
        
        st.write("Score section 3 =  "+str(st.session_state.r3_tot))  
        
        #st.session_state.rtot = st.session_state.rtot + st.session_state.r3_tot   
        #st.write("Score Total current =  "+str(st.session_state.rtot))  
    # ================================================================================                                                                                                        
                 
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
        list_section_04 = ['0 à 5 jours', '6 à 12 jours','13 à 20 jours, 21 à 30 jours']
        
        st.session_state['r4_tot'] = 0
        r4 = 0
        def q_rate4(state):
            if state == list_section_04[0]:
                r4 = 1
            elif state == list_section_04[1]:
                r4 = 2
            elif state == list_section_04[2]:
                r4 = 3
            
            else:
                r4 = 4
                
            st.session_state['r4_tot'] = st.session_state.r4_tot + r4
            return
        
        survey.radio("54.En ce qui concerne votre santé PHYSIQUE globale, durant combien de temps au cours des trente derniers jours votre santé physique n'était-elle pas bonne ?",
                     options=list_section_04, index=None,  horizontal=True, key="Q54")
        q_rate4(st.session_state.Q54)
        
        survey.radio("55. En ce qui concerne votre santé MENTALE globale,durant combien de jours au cours des trente derniers jours votre santé mentale n'était-­elle pas bonne ?",
                     options=list_section_04, index=None,  horizontal=True, key="Q55")
        q_rate4(st.session_state.Q55)   
        
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
           
        survey.radio("Connaissiez-vous la maladie de Lyme (Borréliose) avant votre première infection ?", options=['Oui', 'Non','Je ne me souviens pas'],index=1,  horizontal=True, key="Q60")
        survey.radio("Connaissiez-vous les éventuelles coinfections (Bartonella, Babesia etc..) avant votre première infection ?", options=['Oui', 'Non','Je ne me souviens pas'],index=1,  horizontal=True, key="Q61")
        survey.radio("Connaissiez-vous les dispositions / précautions nécessaires à  prendre pour éviter le contact avec les tiques ?", options=['Oui', 'Non','Je ne me souviens pas'],index=1,  horizontal=True, key="Q62")
        
        st.multiselect("Possédez-vous (ou possédiez) des animaux de compagnie ?", ['Aucun','Chien','Chat','Autres (mammifères)','Autres (non mammifères)'], key="Q63" )
        
        
        
        
        #st.write("You selected:", animals)
         
        activities = st.multiselect("Vos activités sont-elles liées à  : ",
        ["l'entretien de zones naturelles ?",'autre',"l'assistance aux animaux domestiques (SPA, chenils, refuges, ..) ?",
         'autre',"l'exploitation agricole et animale (bovins etc..) ?",'la foresterie ?'], default=["autre"], key="Q64" )
        
        #st.write("You selected:", activities)

        
    
    
    elif pages.current == 8:
        
        st.header('Page 8 - Lyme Suisse - Questionnaire - Remarques / Commentaires', divider=True) 

        # Strongly Disagree
        # Strongly Agree
        #survey.select_slider("Likert scale:", options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], id="Q2")
        # Area input:

        survey.text_area("Vos remarques, commentaires : ")

        #survey.slider("Slider:", min_value=0, max_value=500, value=50)
        # ---- END OF SURVEY -- SAVE ALL DATA TO FTP FILE ---------------------
        # st.success("Vos réponses sont enregistrées, merci de votre collaboration !")
        
        #submitted = st.form_submit_button("Submit")
        #if submitted:
        
        
        
    elif pages.current == 9:
          
        # ---------------- WRITE DATA TO JSON OBJECT -----------------------
        
        data = survey.to_json()
        json_str = json.dumps(data, indent=4)
        
        # ---- SUBMITTED FINAL DATA AND PROCEDURE -------------------
        ## getting the hostname by socket.gethostname() method
        st.success("Vos réponses sont enregistrées, merci de votre collaboration !")
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
        
        st.session_state['date'] = str(date.today())
        st.write('Date : ',st.session_state['date'])
        # st.write('UUID :' + str(st.session_state['res']))
        # --------------------------------------------------------------------

        # st.write('date : ',st.session_state["date"])
        # st.write('UUID short : ',st.session_state["uuid_short"])
        # st.write('Age : ',st.session_state["age"])
        
        

        st.session_state["filestr"] = ''  
        st.session_state["filestr"] = 'lymech_survey-'+ str(st.session_state['date']) + '-'+ str(st.session_state['ushort']) + '.json'
        st.write('Filestr = ',st.session_state["filestr"])

        with open(st.session_state["filestr"], "w") as f:
            f.write(json_str)

        
        # Create an FTP object and connect to the server
        # LOGIN TO FTP SERVER
        ftpObject = FTP('279.hosttech.eu','algolabs.ch','t4HVn_7ig6yd');
        print(ftpObject.getwelcome());
        # ======= FTP DESTINATION FOLDER ===========================
        ftpResponseMessage = ftpObject.cwd("/lyme-ch.algolabs.ch/questionnaire");
        st.write(ftpResponseMessage);
        # 250 CWD command successfULL 

        # Open the file in binary mode
        # ----------- SEARCH FILE ---------------
        # path_json = "D:/_00_LYME_CH/data/lyme_ch_questionnaire/"
        # filedir = path_json + 'lyme_ch_data_quest.json'
        # file = open(filedir,'rb')                  # file to send

        filepath = st.session_state["filestr"]
        # fileObject = open(filedir, "rb");
        fileObject = open(filepath, "rb");

        file2BeSavedAs = st.session_state["filestr"]
        ftpCommand = "STOR %s"%file2BeSavedAs;
        # Transfer the file in binary mode
        ftpResponseMessage = ftpObject.storbinary(ftpCommand, fp=fileObject);
        st.write(ftpResponseMessage);
        # ----------- REDIRECT TO ANOTHER URL -----------------
        
        #import streamlit.components.v1 as components
        
        # embed streamlit docs in a streamlit app
        # st.components.v1.iframe(src, width=None, height=None, scrolling=False, *, tab_index=None)
        
        #components.iframe("https://www.lyme.ch", width=1600, height=1600, scrolling=True)
        
        st.stop()
        
        if st.button("Quit Survey"):
            st.markdown("""<meta http-equiv="refresh" content="0; url='https://www.lyme.ch'" />""", unsafe_allow_html=True)
        
        
        

    else: # --- last page upload all json data to ftp file ------------------
        print('end -> all answered')     
        

        
       
                                                                                              
# ============= DISPLAYED ON FOOTER PAGES ====================







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







