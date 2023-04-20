# -*- coding: utf-8 -*-
"""
Author: Robert Bachmeier
File: Resume_online
Version 1.1
Date: 20-04-2023
"""

#Import Packages#

from pathlib import Path
import streamlit as st
from PIL import Image
import requests # pip install requests to get lottie files direct from the webpage
from streamlit_lottie import st_lottie # install streamlit-lottie
import json

# --- define a function to include lottie-animations from lottie webpage to your streamlit page ---

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- define a function to include lottie-animations from files to your steamlit page ---

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# --- PATH SETTINGS --- 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'Lebenslauf_Robert_Bachmeier_Deutsch.pdf'
profile_pic = current_dir / 'assets' / 'profile_pic_revised.png'

# --- GENERAL SETTINGS AND VARIABLES---

PAGE_TITLE = 'Digitaler Lebenslauf | Robert Bachmeier'
PAGE_ICON = ':man_in_tuxedo:'
NAME = 'Robert Bachmeier'
DESCRIPTION = '''Data Analyst and Senior Controller Asset Management, 
                 improve customer portfolios by providing meaningful insights.'''
EMAIL = 'robert_bachmeier@yahoo.de'

SOCIAL_MEDIA = {
                'Linkedin': 'https://www.linkedin.com/in/robert-bachmeier-828383224/',
                'Xing' : 'https://www.xing.com/profile/Robert_Bachmeier9/cv',
                'github' : 'https://github.com/RoBac1993'}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- STYLE SETTINGS ---
# --- LOAD CSS; PDF & PROFILE PICTURE ---

with open (css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

with open (resume_file, 'rb') as pdf_file: 
           PDFbyte = pdf_file.read()
           profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---

col1, col2 = st.columns(2, gap='small')

with col1:
        st.image(profile_pic, width=230)
        
with col2: 
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = '📄 Download Lebenslauf',
        data = PDFbyte,
        file_name=resume_file.name,
        mime = 'application/octet-stream'
        )    
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---

st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
     cols[index].write(f'[{platform}]({link})')

st.write('---')
     
# --- Professional Experience --- 

#create an expanding page element regarding professional experience
with st.expander('Berufserfahrung', True):

    st.write('---')
    
    st.subheader('Spezialist Investmentcontrolling und Perfomancemeasurement - Commerzbank AG')
    icons = ['1-square-fill'] , st.write(':round_pushpin: Frankfurt am Main, Deutschland | :date: 06/2018 - 03/2023')
    st.write(
    '''
    - ► Portfolioanalysen bezüglich definierter Risikoparameter
    - ► Erstellung von Performance- und Risikoanalysen
    - ► Vertragscontrolling und Prüfung individueller Anlagerichtlinien 
    - ► Durchführung von Geschäftsanalysen 
    - ► Weiterentwicklung des vorhandenen Datenhaushalts 
    - ► Sicherstellung der Einhaltung von regulatorischen Vorgaben 
        ''')   
        
    st.write('\n')
    st.subheader('Business Analyst Digital Operations Journey - Commerzbank AG')
    st.write(':round_pushpin: Frankfurt am Main, Deutschland | :date: 05/2017 - 06/2018')
    st.write('''
         - ► Digitalisierung End-to-End Prozesse im Dokumentenmanagement
         - ► Fachliche Funktionalitätsbeschreibung digitaler Services 
         - ► Konzeption logischer Regelwerke zur Dokumentenverarbeitung 
         - ► Erstellung fachlicher Datenmodelle
         - ► Koordination fachlicher Testabnahmen
         ''')

    st.write('\n')
    st.subheader('Privatkundenberater - Commerzbank AG')
    st.write(':round_pushpin: Regensburg, Deutschland | :date: 01/2012 - 04/2017')
    st.write('''
         - ► Eigenverantwortliche Betreuung eines Kundenstammes
         - ► Akquisition neuer Kunden und Ausbau bestehender Geschäftsbeziehungen 
         - ► Serviceorientierte Bearbeitung von Kundenwünschen im Rahmen des Dienstleistungsspektrums
         ''')

    st.write('\n')
    st.subheader('Ausbildung zum Bankkaufmann - Commerzbank AG')
    st.write(':round_pushpin: Regensburg, Deutschland | :date: 09/2009 - 01/2012')
    st.write('''
         - ► Durchführung standardisierter Bankdienstleistungen im Privatkundengeschäft
         - ► Unterstützung von Privat- & Unternehmenskundenberater im täglichen Filialgeschäft 
         ''')

# --- Education --- 

#create an expanding page element regarding Education
with st.expander('Ausbildung', True):

    st.write('---')

    st.write(':round_pushpin: Frankfurt am Main, Deutschland | :date: 02/2019 - 07/2020')
    st.subheader('Master of Science in Finance | Frankfurt School of Finance & Management')
    st.write('''
         - ► **Schwerpunkt: Risk Management**
         - Structured Products & Interest Rate Models, Portfolio Risk Management, Risk Modelling, Data Analytics & Machine Learning, Risk Governance, Credit Risk Default Models & Credit Derivatives 
         ''')

    st.write('\n')
    st.write(':round_pushpin: Frankfurt am Main, Deutschland | :date: 09/2016 - 08/2018')
    st.subheader('Bachelor of Science in Betriebswirtschaft | Frankfurt School of Finance & Management')
    st.write('''
         - Asset Management, Risk Management, Business Strategy, Stochastik, Corporate Finance, Accounting and Capital Markets, Leadership an Ethics in Global Business
         ''')
         
    st.write('\n')
    st.write(':round_pushpin: Regensburg, Deutschland | :date: 11/2014 - 10/2015')
    st.subheader('Bankbetriebswirt | Frankfurt School of Finance & Management')
    st.write('''
         - Dienstleistungsmanagement, Portfoliomanagement, Ertrags- & Risikomanagement, Privatkundengeschäft, Private Banking
         ''')
         
    st.write('\n')
    st.write(':round_pushpin: Regensburg, Deutschland | :date: 04/2012 - 02/2014')
    st.subheader('Bankfachwirt | Frankfurt School of Finance & Management')
    st.write('''
         - Frankfurt School of Finance & Management Allgemeine Betriebswirtschaft, Bankbetriebswirtschaft, Recht, Volkswirtschaft, Privatkundengeschäft
         ''')

# --- Kenntnisse ---

#create an expanding page element regarding Education
with st.expander('Kenntnisse und Fähgikeiten', True):
    st.write('---')

    st.subheader('Sprachen')

    st.write(
        """<style>
        [data-testid="stHorizontalBlock"] {
            align-items: center;
            }
        </style>
        """,
        unsafe_allow_html=True
        )

# Create different columns across multiple lines to align content 
    language1, language_bar1 , language_level1 = st.columns([1, 4, 1])
    language2, language_bar2 , language_level2 = st.columns([1, 4, 1])  

    with language1: # skill
         st.write('Deutsch')
    with language_bar1: #Progressbar of the skill
         st.write('\n') 
         Deutsch_bar = st.progress(100)
    with language_level1: # level of skill
         st.write('10') 
        
    with language2: # skill
         st.write('Englisch')
    with language_bar2: #Progressbar of the skill
         st.write('\n') 
         Englisch_bar = st.progress(80)
    with language_level2: # level of skill
         st.write('8')

# Create different columns across multiple lines to align content    
    st.subheader('IT-Kenntnisse')
    skills1, skill_bar1 , skill_level1 = st.columns([1, 4, 1])
    skills2, skill_bar2 , skill_level2 = st.columns([1, 4, 1])
    skills3, skill_bar3 , skill_level3 = st.columns([1, 4, 1])
    skills4, skill_bar4 , skill_level4 = st.columns([1, 4, 1])

    with skills1:
         st.write('MS-Office')
    with skill_bar1:
         st.write('\n') 
         MS_bar = st.progress(100)    
    with skill_level1:
         st.write('10') 
    
    with skills2:
        st.write('Python')
    with skill_bar2:
        st.write('\n') 
        Python_bar = st.progress(80)
    with skill_level2:
        st.write('8')
    
    with skills3:
        st.write('SAS')
    with skill_bar3:
         st.write('\n')
         SAS_bar = st.progress(80)
    with skill_level3:
        st.write('8') 
          
    with skills4:
        st.write('SQL')
    with skill_bar4:
        st.write('\n') 
        SQL_bar = st.progress(50)
    with skill_level4:
        st.write('5')     
     
# --- Honors & Awards --- 

#create an expanding page element regarding Honors & Awards
with st.expander('Auszeichungen', True):

     st.write('---')

     #URL für den Link der Auszeichnung der Quoniam GmbH
     url = "https://www.frankfurt-school.de/de/home/newsroom/news/2018/Juni/quoniam-hochschulpreis"
     
     st.write(':office: Quoniam Asset Management GmbH | :date: 05/2018')
     st.subheader('Quoniam Hochschulpreis 2018')
     st.write( '[Auszeichnung für die Entwicklung einer Smart Beta Portfoliostrategie mit dem Faktor "Growth in Net Operating Assets](%s)' %url) 

     st.write(':office: Commerzbank AG | :date: 05/2014')
     st.subheader('Handlungsbevollmächtiger Commerzbank AG')

# --- Hobbys --- 

#create an expanding page element regarding Honors & Awards
with st.expander('Hobbys', True):
     st.write('---')

     # create mulitple columns with a small gap to align them
     fitness, e_sports, reading, hiking = st.columns(4, gap='small')    

     #create the lottie files for the icons within the section hobbys
     
     lottie_fitness_url = load_lottieurl('https://lottie.host/94b76f9b-2e96-4f3b-89e4-d480836c1350/k1GRBWMpOd.json')#online url
     lottie_fitness_file = load_lottiefile("lottiefiles/fitness.json") #filepath for homepage with github
          
     with fitness:
          st_lottie(
             lottie_fitness_file,
             speed= 1,
             loop = True,
             quality = 'high',     # medium; high
             width = None,
             height = 100,
             key = "fitness icon"
             )
          st.markdown("<p style='text-align: center; ;'> Fitnessstudio </p>", unsafe_allow_html=True)
                      # '''
     lottie_e_sports_url = load_lottieurl('https://lottie.host/13f92670-2a67-4155-ac0e-96382cab333b/tHS6oZ7i3e.json') #online url
     lottie_e_sports_file = load_lottiefile("lottiefiles/esport.json") #filepath for homepage with github
     with e_sports:
          st_lottie(
            lottie_e_sports_file,
            speed= 1,
            loop = True,
            quality = 'high',     # medium; high
            width = None,
            height = 100,
            key = "e_sports icon"
            )
          st.markdown("<p style='text-align: center; ;'> E-Sports </p>", unsafe_allow_html=True)
             
     lottie_reading_url = load_lottieurl('https://lottie.host/4dd2c353-bd4f-4fdc-9339-347d51e086ca/XxwfuiTs39.json')   #online url
     lottie_reading_file = load_lottiefile("lottiefiles/reading.json") #filepath for homepage with github
     with reading:
          st_lottie(
           lottie_reading_file,
           speed= 1,
           loop = True,
           quality = 'high',     # medium; high
           width = None,
           height = 100,
           key = "reading icon"
           )
          st.markdown("<p style='text-align: center; ;'> Lesen </p>", unsafe_allow_html=True)

     lottie_hiking_url = load_lottieurl('https://lottie.host/c6f2ad68-d646-4f5d-924b-36113dc00672/OSG09IN4H7.json') #online url
     lottie_hiking_file = load_lottiefile("lottiefiles/hiking.json") #filepath for homepage with github
     with hiking:
          st_lottie(
           lottie_hiking_file,
           speed= 1,
           loop = True,
           quality = 'high',     # medium; high
           width = None,
           height = 100,
           key = "hiking icon"
           )
          st.markdown("<p style='text-align: center; ;'> Wandern </p>", unsafe_allow_html=True)
          
# --- End of the code --- #