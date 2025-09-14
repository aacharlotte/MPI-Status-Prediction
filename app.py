import streamlit as st

st.title("My Streamlit App")
st.write("Hello, world! 🚀")
st.checkbox("Check me!")

# Step 3: Add your Ngrok auth token (replace with your real one!)
!ngrok config add-authtoken 32hSqDCkHcpMd3oQPEVARMAAacG_2vPjwDwdTfxCLK2V4o6cm

# Step 4: Run the Streamlit app in the background
!streamlit run app.py --server.port 8501 &

# Step 5: Create a public URL with Ngrok
from pyngrok import ngrok
public_url = ngrok.connect(8501)
print("App URL:", public_url)
