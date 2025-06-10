import streamlit as st
import pandas as pd

st.title("Calculation Table Demo")




# functions for additional table calculations
y = []
def calcy(list):
    for x in list:
        i = x**2
        y.append(i)
    return(y)

x = []
def calcx(list):
    for y in list:
        i = y**(1/2)
        x.append(i)
    return(x)


# Create an initial session state
if 'data1' not in st.session_state:
    st.session_state.data1 = pd.DataFrame()
    st.session_state.data2 = pd.DataFrame()  

    # some initial test data
    dict = {'x': [1,2,3], 'y': [1,4,9]}
    data = pd.DataFrame(dict)
    st.session_state.data1 = data


# this displays initial table, and returns updated table
st.write("The values of the table are updated automatically to match `y=x^2`")
st.write("session_state.data1 on display:")
st.session_state.data2 = st.data_editor(st.session_state.data1)

# makes additional changes to the table
if not st.session_state.data2['x'].equals(st.session_state.data1['x']):
    # if there's a change in x
    y = calcy(st.session_state.data2['x'])
    st.session_state.data2['y'] = y
elif not st.session_state.data2['y'].equals(st.session_state.data1['y']):
    # if there's a change in y
    x = calcx(st.session_state.data2['y'])
    st.session_state.data2['x'] = x



st.header("Behind the Scenes:")

# displays user input and additional changes in table
st.write("Below is an additional session state used as a transition stage for updating the main table. This table should be hidden in actual projects.")
st.write("session_state data2 on display:")
st.write(st.session_state.data2)


# rerun to load changes in main table
if not st.session_state.data1.equals(st.session_state.data2):
    st.write("Session states data1 and data2 are not equal.")
    st.session_state.data1 = st.session_state.data2
    st.rerun()
else:
    st.write("Session states data1 and data2 are equal.")


# number of times the page has run
if 'count' not in st.session_state:
	st.session_state.count = 0
st.session_state.count += 1
st.write("Page run count:", st.session_state.count)


# changes to sessions state are demonstrated here
st.write("Below is st.session_state:")
st.write(st.session_state)