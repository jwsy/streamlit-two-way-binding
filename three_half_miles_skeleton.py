import streamlit as st
import datetime

st.markdown("""
### Choose your objective time or pace
""")

st.session_state.stime = 1004 if 'stime' not in st.session_state else st.session_state.stime
st.session_state.minsec = '17:24' if 'minsec' not in st.session_state else st.session_state.minsec

st.session_state.min = 17 if 'min' not in st.session_state else st.session_state.min
st.session_state.sec = 24 if 'sec' not in st.session_state else st.session_state.sec
st.session_state.milemin = 11 if 'milemin' not in st.session_state else st.session_state.milemin
st.session_state.milesec = 36 if 'milesec' not in st.session_state else st.session_state.milesec

st.write("st.session_state object:" , st.session_state)

def update_base(*args):
    print(f"In update_base, {st.session_state.min}:{st.session_state.sec}")
    pass

def update_onemile(*args):
    print(f"In update_onemile, {st.session_state.milemin}:{st.session_state.milesec}")
    pass

base, onemile, avocado = st.columns(3)
with base:
    st.header('1.5 mile time')
    st.number_input('Minutes', key='min', min_value=5, max_value=25, step=1, on_change=update_base)
    st.number_input('Seconds', key='sec', min_value=0, max_value=59, step=1, on_change=update_base)
with onemile:
    st.header('One mile pace')
    st.number_input('Minutes', key='milemin', min_value=4, max_value=18, step=1, on_change=update_onemile)
    st.number_input('Seconds', key='milesec', min_value=0, max_value=59, step=1, on_change=update_onemile)
with avocado:
    st.header("An avocado")
    st.image("avocado-o-512.png")