import streamlit as st
import pandas as pd

st.write('This is all of the celestial bodies supported by my Universal gravitational calculator for interstellar objects')

data = pd.read_csv('BodyData.csv')
st.write(data)