import streamlit as st
import datetime
# https://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta-object-from-a-simple-string  

# stime = float: time in seconds to run 1.5 miles
# minsec = string: string representing the stime in format "(m)m:ss"
#          `ret = f"{min}:{sec:02n}`

def stime_to_minsec(stime):
  min = int(stime / 60)
  sec = int(stime % 60)
  ret = f"{min}:{sec:02n}"
  # print(f"{ret=}")
  return ret

def minsec_to_stime(minsec):
  # we specify the input and the format...
  t = datetime.datetime.strptime(minsec,"%M:%S")
  # ...and use datetime's hour, min and sec properties to build a timedelta
  delta = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
  ret = int(delta.total_seconds())
  # print(f"{ret=}")
  return ret

def stime_to_misecpermi(stime):
  stime_1mi = stime / 1.5
  stime_to_misecpermi_ret = (stime_to_minsec(stime_1mi))
  print(f"With 1.5 mile time of {stime} sec, pace in min/mile: {stime_to_misecpermi_ret=} min/mile")
  return stime_to_misecpermi_ret

def minsecpermi_to_stime(minsecpermi):
  stime_1mi = minsec_to_stime(minsecpermi)
  stime = 1.5 * stime_1mi
  print(f"At pace {minsecpermi} min/mile, total seconds to 1.5 miles: {stime} sec")
  return stime

def minsec_min(minsec_str):
   return int(minsec_str.split(':')[0])

def minsec_sec(minsec_str):
   return int(minsec_str.split(':')[1])

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
    print(args)
    print('Base values changed, update stime then propagate out')
    print(f"{st.session_state.min=}, {st.session_state.sec=}")
    st.session_state.stime = 60 * st.session_state.min + st.session_state.sec

    calcminsecmile = stime_to_misecpermi(st.session_state.stime)
    print(f"{calcminsecmile=}")
    st.session_state.milemin = minsec_min(calcminsecmile)
    st.session_state.milesec = minsec_sec(calcminsecmile)
    st.session_state.minsec = stime_to_minsec(st.session_state.stime)

def update_onemile(*args):
    print(args)
    print('onemile values changed, update stime then propagate out')
    print(f"{st.session_state.milemin=}, {st.session_state.milesec=}")
    st.session_state.stime = 1.5 * (60 * st.session_state.milemin + st.session_state.milesec)
    st.session_state.minsec = stime_to_minsec(st.session_state.stime)
    st.session_state.min = int(minsec_min(st.session_state.minsec))
    st.session_state.sec = int(minsec_sec(st.session_state.minsec))


base, onemile, avocado = st.columns(3)
with base:
    st.header('1.5 mile time')
    # st.write(f"1.5 mile pace {min}:{sec}")
    st.number_input('Minutes', key='min', min_value=5, max_value=25, step=1, on_change=update_base)
    st.number_input('Seconds', key='sec', min_value=0, max_value=59, step=1, on_change=update_base)
with onemile:
    st.header('One mile pace')
    st.number_input('Minutes', key='milemin', min_value=4, max_value=18, step=1, on_change=update_onemile)
    st.number_input('Seconds', key='milesec', min_value=0, max_value=59, step=1, on_change=update_onemile)
with avocado:
    st.header("An avocado")
    st.image("avocado-o-512.png")