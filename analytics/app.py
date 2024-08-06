import streamlit as st 
import matplotlib.pylot as plt

st.title("Analytics Dashboard")
st.write("v.0.0.1")

#Test Chart
categories = ['A', 'B', 'C', 'D']
values = np.random.randint(10,100, size=(4,))

fig, ax = plt.subplot()
ax.bar(categories, values, color='blue')
ax.set_xlabel('categories')
ax.set_ylable('values')
ax.set_title