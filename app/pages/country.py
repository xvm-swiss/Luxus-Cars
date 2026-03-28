import streamlit as st # to raun >>> streamlit run app.py
import pandas as pd
import plotly.express as px
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from streamlit_option_menu import option_menu



# Title page
st.set_page_config(
    page_title= 'Dashboard',
    page_icon= ':bar_chart:',
    layout="wide"
)

df = pd.read_csv('cleaned data/Cleaned_Exotic-Cars-.csv')

# 1. Anker direkt beim Navigationsmenü setzen ( Scroll up)
st.markdown("<div id='nav-menu'></div>", unsafe_allow_html=True)


# 1. CSS: Erzwingt 0px oben und 50px unten
st.markdown("""
    <style>
    /* Entfernt den Standard-Abstand von Streamlit oben komplett */
    .block-container {
        padding-top: 2.5rem !important; 
    }

    /* Dein Menü-Block: 0px von oben, 50px nach unten */
    .stHorizontalBlock  {
        
        margin-top: 50px; /* Der gewünschte Abstand nach unten */
        
    }
    </style>
    """, unsafe_allow_html=True)



# Navigator Menü
# "orientation='horizontal'" macht es zu einer Leiste oben
selected = option_menu(
    None, ["Search & Chatbot", "Classify", "Car Manufacturer"], 
     icons=['search', 'gear', 'geo-alt'],  
    default_index=2,  # 0 ist "Home"
    orientation="horizontal",
    styles={
        "container": {"border-radius": "0px", "background-color": "transparent", "padding": "0px !important"},
        "nav-link": {"color": "#39FF14", "font-family": "monospace", "font-size": "14px"},
        "nav-link-selected": {"background-color": "#3f6e2e", "color": "#39FF14"}
    }
)

if selected == "Search & Chatbot":
    st.switch_page("chatbot.py")
# ... (Home muss hier nicht geswitcht werden)

elif selected == "Classify":
    st.switch_page("pages/classify.py")









# Slider als Range (Bereich) definieren
prices = st.sidebar.slider('Price :',
                        min_value=float(df["Price (in USD)"].min()),
                        max_value=float(df["Price (in USD)"].max()),
                        value=(float(df["Price (in USD)"].min()), float(df["Price (in USD)"].max())))

# years = st.sidebar.slider('Year :',
#                         min_value=float(df["Year"].min()),
#                         max_value=float(df["Year"].max()),
#                         value=(float(df["Year"].min()), float(df["Year"].max())))

New_Segments = st.sidebar.multiselect('New_Segment: ',
                                  options= df["New_Segment"].unique(),
                                  default= df["New_Segment"].unique())


countries = st.sidebar.multiselect('Country:',
    options=sorted(df["Country"].unique()),  # Hier wird sortiert
    default=sorted(df["Country"].unique())   # Auch Standardwerte sollten sortiert sein
)



# Wir erstellen eine sortierte Liste der einzigartigen Marken
sorted_makes = sorted(df["Car Make"].unique())

CarMakes = st.sidebar.multiselect(
    'Car Make:',
    options=sorted_makes,
    default=sorted_makes
)


# Deine bestehende Query (jetzt mit den Checkbox-Werten)

filtered_df = df.query(
    'Country in @countries and '  # Hier war vorher 'Year in @years'
    '`Price (in USD)` >= @prices[0] and '
    '`Price (in USD)` <= @prices[1] and '
    '`Car Make` in @CarMakes and '
    'New_Segment in @New_Segments'
)


# Part 1
cat_10, cat_20, cat_30, cat_40, cat_50= st.columns(5)

# Car Manufacturere:
German_car = filtered_df[ filtered_df["Country"] == 'German'].shape[0]
UK_car = filtered_df[ filtered_df["Country"] == 'UK'].shape[0]
Italian_car = filtered_df[ filtered_df["Country"] == 'Italian'].value_counts().sum()
France_car = filtered_df[filtered_df["Country"] == 'France'].value_counts().sum()
Sweden_car = filtered_df[ filtered_df["Country"] == 'Sweden'].value_counts().sum()

cat_10.write(f'<H6>German Car: <br>{German_car}</h6>', unsafe_allow_html = True)
cat_20.write(f'<H6>UK Car: <br>{UK_car}</h6>', unsafe_allow_html = True)
cat_30.write(f'<H6>Italian Car: <br>{Italian_car}</h6>', unsafe_allow_html = True)
cat_40.write(f'<H6>France Car: <br>{France_car}</h6>', unsafe_allow_html = True)
cat_50.write(f'<H6>Sweden Car: <br>{Sweden_car}</h6>', unsafe_allow_html = True)


# part 2
cat_11, cat_21, cat_31, cat_41, cat_51= st.columns(5)

Croatia_car = filtered_df[ filtered_df["Country"] == 'Croatia'].value_counts().sum()
Japan_car = filtered_df[ filtered_df["Country"] == 'Japan'].value_counts().sum()
UAE_car = filtered_df[ filtered_df["Country"] == 'United Arab Emirates'].value_counts().sum()
South_Korea_car = filtered_df[ filtered_df["Country"] == 'South Korea'].value_counts().sum()
US_car = filtered_df[ filtered_df["Country"] == 'US'].value_counts().sum()

cat_11.write(f'<H6>Croatia Car: <br>{Croatia_car}</h6>', unsafe_allow_html = True)
cat_21.write(f'<H6>Japan Car: <br>{Japan_car}</h6>', unsafe_allow_html = True)
cat_31.write(f'<H6>UAE Car: <br>{UAE_car}</h6>', unsafe_allow_html = True)
cat_41.write(f'<H6>South_Korea Car: <br>{South_Korea_car}</h6>', unsafe_allow_html = True)
cat_51.write(f'<H6>US Car: <br>{US_car}</h6>', unsafe_allow_html = True)


# Daten in ein Dictionary packen
data = {
    "Land": ["Deutschland", "UK", "Italien", "USA", "Japan", "Frankreich", "Schweden", "Kroatien", "UAE", "Südkorea"],
    "Anzahl": [German_car, UK_car, Italian_car, US_car, Japan_car, France_car, Sweden_car, Croatia_car, UAE_car, South_Korea_car]
}

# Temporäres DataFrame erstellen
filtered_df = pd.DataFrame(data)

# Balkendiagramm erstellen
fig = px.bar(filtered_df, 
             x='Land', 
             y='Anzahl', 
             color='Land',
             color_discrete_sequence=px.colors.qualitative.Safe,
             title='Anzahl der Autos nach Herkunftsland',
             text_auto=True) # Zeigt die Werte direkt über den Balken an

st.plotly_chart(fig,  use_container_width=True)






# 2. Button zum Navigationsmenü
st.markdown("""
    <a href='#nav-menu' style='text-decoration:none;'>
        <button style='
            background-color: #39FF14; 
            color: white; 
            border: none; 
            padding: 10px 20px; 
            border-radius: 5px;
            cursor: pointer;'>
            Scroll up ↑
        </button>
    </a>
    """, unsafe_allow_html=True)