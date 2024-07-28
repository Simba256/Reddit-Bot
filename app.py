# app.py
import subprocess
import streamlit as st





process = None

def start_script():
    global process
    if process is None:
        process = subprocess.Popen(['python', 'Project.py'])
        print("Script started.")
        st.write("Script started.")
    else:
        print("Script is already running.")
        st.write("Script is already running.")

def stop_script():
    global process
    if process is not None:
        process.terminate()
        st.write("Script stopped.")
        process = None
        print("Script stopped.")
    else:
        st.write("No script is running.")
        print("No script is running.")


if st.button('Start Script'):
    start_script()

if st.button('Stop Script'):
    stop_script()

