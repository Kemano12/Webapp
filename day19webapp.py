import streamlit as st

with open('GuiDay17.txt', 'r') as file:
    Guiday17 = file.readlines()


def add_new_line():
    #opening the file in read mode storing it in guiday17
    with open('GuiDay17.txt', 'r') as file:
        Guiday17 = file.readlines()
    #we are entering a new line in the text input and storing it in the variable newline
        newline = st.session_state["new_gui"] +"\n"
    #appending the  guiday 17 with our new line input
        Guiday17.append(newline)
    #Opening the file in write mode and adding out changes in the new file
    with open('GuiDay17.txt', 'w') as file:
        Guiday17 = file.writelines(Guiday17)

st.title("My Todo app")
st.subheader("This app is to increase your productivity")
st.checkbox("Buy grocery.")
##st.checkbox("Throw the trash")

#storing each output line in the checkbox
for gui in Guiday17:
    st.checkbox(gui )


st.text_input(label = "",placeholder = "Add a new todo...",on_change=add_new_line, key = 'new_gui' )
