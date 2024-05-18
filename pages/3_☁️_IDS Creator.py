
import streamlit as st
from PIL import Image



# =========================================================================================================================
# page config
# =========================================================================================================================

im = Image.open('./resources/img/IDS_logo.ico')
st.set_page_config(
    page_title="IDS Converter",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded",
)


with st.container():
    st.title('📝 Soon')
            
    
     





        





