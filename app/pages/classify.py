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
    icons=['search', 'chat-dots', 'geo-alt'], 
    default_index=1,  # 0 ist "Home"
    orientation="horizontal",
    styles={
        "container": {"border-radius": "0px", "background-color": "transparent", "padding": "0px !important"},
        "nav-link": {"color": "#39FF14", "font-family": "monospace", "font-size": "14px"},
        "nav-link-selected": {"background-color": "#3f6e2e", "color": "#39FF14"}
    }
)




if selected == "Search & Chatbot":
    st.switch_page("chatbot.py")
# Classify ignorieren, da wir schon hier sind
elif selected == "Car Manufacturer":
    st.switch_page("pages/country.py")







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



# Graphic 1 
# Cars Segment sorted by price range

fig_1 = px.histogram( df, x= "New_Segment", color="New_Segment",
             title='Cars Segment sorted by price range')

st.plotly_chart(fig_1, use_container_width= True)



# KPI

cat_1, cat_2, cat_3, cat_4, cat_5, cat_6  = st.columns(6)

#All_category = int(filtered_df['category']["units_sold"].sum())
all_car_make= filtered_df["Car Make"].nunique()
all_car_model = filtered_df["Car Model"].nunique()
prices = filtered_df["Price (in USD)"].unique()[0]
Countries = filtered_df["Country"].unique()[0]
car_Horsepower= filtered_df["Horsepower"].unique()[0]
New_Segments = filtered_df["New_Segment"].unique()[0]


cat_1.write(f'<H6>Car Make: <br>{all_car_make}</h6>', unsafe_allow_html = True)
cat_2.write(f'<H6>Car Model: <br>{all_car_model}</h6>', unsafe_allow_html = True)
cat_3.write(f'<H6>Classify: <br>{prices}</h6>', unsafe_allow_html = True)
cat_4.write(f'<H6>Manufacturer: <br>{Countries}</h6>', unsafe_allow_html = True)
cat_5.write(f'<H6>Horsepower: <br>{car_Horsepower}</h6>', unsafe_allow_html = True)
cat_6.write(f'<H6> Prices: <br>{New_Segments}</h6>', unsafe_allow_html = True)	
# 3. Spalten-Layout erstellen
cat_1, cat_2, cat_3, cat_4, cat_5, cat_6 = st.columns(6)


# Best-selling product
# Daten gruppieren: Durchschnittspreis pro Marke berechnen
df_grouped = filtered_df.groupby('Car Make')['Price (in USD)'].mean().reset_index()

# Plot erstellen
fig_1 = px.bar(
    df_grouped, 
    x='Car Make', 
    y='Price (in USD)', 
    color='Car Make',
    title="Average price per car brand"
)

st.plotly_chart(fig_1,  use_container_width=True)







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