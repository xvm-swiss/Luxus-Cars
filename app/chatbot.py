import streamlit as st # to raun >>> streamlit run app.py
import pandas as pd
import plotly.express as px
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from streamlit_option_menu import option_menu
import os
from groq import Groq
# pip install langchain-groq
# python -m pip install groq

from dotenv import load_dotenv;     load_dotenv()




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



# # Seiten explizit definieren
# pg = st.navigation([
#     st.Page("app.py", title="Search", icon="🔍"),
#     st.Page("pages/classify.py", title="Classify", icon="🤖"),
#     st.Page("pages/country.py", title="Country", icon="🌍"),
#     st.Page("pages/horsepower.py", title="Horsepower", icon="⚡")
# ])

# pg.run()

# Navigator Menü
# "orientation='horizontal'" macht es zu einer Leiste oben
selected = option_menu(
    None, ["Search & Chatbot", "Classify", "Car Manufacturer"], 
    icons=['search', 'gear', 'geo-alt'], 
    default_index=0,  # 0 ist "Home"
    orientation="horizontal",
    styles={
        "container": {"border-radius": "0px", "background-color": "transparent", "padding": "0px !important"},
        "nav-link": {"color": "#39FF14", "font-family": "monospace", "font-size": "14px"},
        "nav-link-selected": {"background-color": "#3f6e2e", "color": "#39FF14"}
    }
)




# WICHTIG: Hier KEIN "if selected == 'Search'"!
if selected == "Classify":
    st.switch_page("pages/classify.py")

elif selected == "Car Manufacturer": # Exakt wie im Menü oben schreiben!
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





#Main Title
st.markdown (
    "<h1 style='text-align: left; color:white; font-family: arial; font_size: 35px'>Luxus Car Models</h1>",
    unsafe_allow_html= True 
)





# Logo image and Text
col1, col2 = st.columns([1,5])
with col1:
    st.image("app/search.png", width=130)

with col2 :
    st.write("## Search for car info")
    st.write("Select Car Make & Model")






# Suche Filter

# 1. Auswahl durch den Nutzer
# 1. Schritt: Auswahl der MARKE (Make)
make_option = st.selectbox(
    ':red[Which brand are you looking for?]',
    filtered_df['Car Make'].unique()
)

# Wir filtern den DataFrame vorab NUR nach der gewählten Marke
mask_make = filtered_df[filtered_df['Car Make'] == make_option]

# 2. Schritt: Auswahl des MODELLS (Model)
# WICHTIG: Wir nutzen hier "mask_make" statt "filtered_df"
model_option = st.selectbox(
    ':red[Which model are you looking for?]',
    mask_make['Car Model'].unique()
)

# 3. Schritt: Das finale Ergebnis filtern
final_selection = mask_make[mask_make['Car Model'] == model_option]

st.write(f':green[You have selected:] **{make_option} {model_option}**')

# Optional: Den gefilterten Datensatz anzeigen
st.dataframe(final_selection)


st.divider()



# CHatbot

st.markdown("""
    <style>
    .main-title { 
        font-size: calc(14px + 2vw) !important; 
        color: #39FF14 !important; 
        font-family: 'Times New Roman', Times, serif !important; 
        text-align: left !important; 
        margin-bottom: 20px;
    }
    </style>
    <h3 class="main-title"> 🤖 Chatbot is 24/7 your digital concierge  </h3>
    <p> I am your digital concierge. Whether you’d like details about a specific model, 
            would like to schedule a personal consultation, or have questions about our 
            exclusive services—I’m here to assist you.</p>
    """, unsafe_allow_html=True)



system_prompt ="""Role: You are "Aura," a specialized Retail Data Assistant designed by Jeffry K. Your primary purpose is to help users analyze Luxus Car data using professional retail KPIs.

Identity & Personality:

Creator: You were developed by Jeffry K. (Full name: Jeffry).

Contact Info: If a user asks for contact details, provide: Phone: +41786916600 | Email: jeffty@xvm.ch

Tone: Professional, analytical, and efficient. You speak like a senior retail consultant who understands fast-fashion dynamics.

Knowledge Base & Tasks:

Tools: You are an expert in Python libraries, specifically Pandas (for data manipulation), NumPy (for calculations), and Plotly/Seaborn (for data visualization).

Key Metrics: You focus on Total Sales, Total Revenue, Sell-through rates, and inventory turnover.

Analysis Style: When asked about data, suggest specific visualizations (e.g., "We should use a Seaborn heatmap to see sales density by region").

Standard Responses:

Question: "Who are you?"

Response: "I am a helpful assistant designed by Jeff K. to provide deep insights into Zara's sales performance and retail analytics."

Constraint: Do not make up data. If the user hasn't provided a specific dataset yet, ask them to describe the columns or upload the file so you can help them write the Pandas code to analyze it.
-----
Luxury Automotive Analyst Persona
Role: You are "Stellar," a specialized Luxury Automotive Market Analyst designed by Jeffry K. Your primary purpose is to help users analyze high-end vehicle market trends, depreciation curves, and sales performance using professional automotive KPIs.


Tone: Sophisticated, precise, and authoritative. You speak like an industry strategist at a top-tier European car manufacturer or a high-end auction house.

Knowledge Base & Tasks
Tools: You are an expert in Python libraries, specifically Pandas (for cleaning vehicle datasets), Matplotlib/Plotly (for price-over-time visualizations), and Scikit-Learn (for predictive pricing models).

Key Metrics: You focus on Residual Value (RV), Days to Turn (DTT), MSRP vs. Transaction Price, and Option-to-Value ratios.

Analysis Style: When asked about market trends, suggest specific data approaches (e.g., "We should use a Matplotlib scatter plot to identify the 'sweet spot' where mileage and depreciation intersect for the Ferrari 488 market").

Standard Responses
Question: "Who are you?"

Response: "I am Stellar, an analytical assistant designed by Jeff K. to provide elite-level insights into the luxury automotive market and help you navigate high-end vehicle data with precision."

Constraints
Integrity: Do not fabricate market prices or historical data.

Data Handling: If the user hasn't provided a specific dataset (e.g., CSV of auction results or inventory logs), ask them to provide the headers or upload the file so you can generate the Python code required for the analysis.

"""

# Eingabefeld für den User
user_input = st.text_area('Enter your message:')

# Button hinzufügen
if st.button('Send'):
    if user_input:
        # Client initialisieren (Achte auf die korrekte Schreibweise: GROQ)
        client = Groq(api_key=os.getenv('GROQ_API_KEY'))

        try:
            chat_completion = client.chat.completions.create(
                messages=[

                     {
                         "role": "system",
                         "content": system_prompt
                     },

                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            
            # Antwort ausgeben
            response = chat_completion.choices[0].message.content
            st.write(response)
            
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a message first.")



# Kleiner Abstand

st.markdown("""
    <style>
    .spacer {
        margin-top: 100px;
    }
    </style>
    <div class="spacer"></div>
""", unsafe_allow_html=True)



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
