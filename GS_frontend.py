'''import streamlit as st
import pandas as pd
import xlsxwriter
import GS_backend

st.title('Global Search')

search_query = st.text_input("Enter search query:")
num_profiles = st.number_input("Number of profiles", min_value=1, step=1, format="%d")

if st.button('Search'):
    # Scrape profiles from both sources
    linkedin_profiles = GS_backend.scrape_linkedin_profiles(search_query, num_profiles)
    
    # Create a Pandas DataFrame for each source
    df_linkedin = pd.DataFrame(linkedin_profiles)
    df_linkedin = df_linkedin[['Name', 'Title', 'Location', 'Experience', 'Education', 'Skills','LinkedIn_URL','Phone','Email']]
    
    st.dataframe(df_linkedin , use_container_width=True, width=1200,hide_index=True)'''

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_chromedriver():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        # Corrected the way options are passed to the Chrome driver
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get("https://www.google.com")
        st.write(driver.title)
        driver.quit()
    except Exception as e:
        st.error(f"Error running ChromeDriver: {e}")

st.title("Test ChromeDriver on Streamlit Cloud")
test_chromedriver()


    

