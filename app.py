import streamlit as st
import numpy as np

st.set_page_config(page_title="Physics Formula Calculator", page_icon="🧮", layout="centered")

st.title("⚡ Physics Formula Calculator")
st.write("Choose a formula and enter values to calculate results instantly!")

# Dropdown menu
formula = st.selectbox(
    "Select a Physics Formula",
    [
        "Kinematics (v = u + at)",
        "Force (F = m * a)",
        "Kinetic Energy (KE = 0.5 * m * v^2)",
        "Potential Energy (PE = m * g * h)",
        "Ohm's Law (V = I * R)"
    ]
)

if formula == "Kinematics (v = u + at)":
    u = st.number_input("Initial velocity (u) [m/s]", value=0.0)
    a = st.number_input("Acceleration (a) [m/s²]", value=0.0)
    t = st.number_input("Time (t) [s]", value=0.0)
    if st.button("Calculate"):
        v = np.array(u) + np.array(a) * np.array(t)
        st.success(f"Final velocity = {v:.2f} m/s")

elif formula == "Force (F = m * a)":
    m = st.number_input("Mass (m) [kg]", value=0.0)
    a = st.number_input("Acceleration (a) [m/s²]", value=0.0)
    if st.button("Calculate"):
        F = np.array(m) * np.array(a)
        st.success(f"Force = {F:.2f} N")

elif formula == "Kinetic Energy (KE = 0.5 * m * v^2)":
    m = st.number_input("Mass (m) [kg]", value=0.0)
    v = st.number_input("Velocity (v) [m/s]", value=0.0)
    if st.button("Calculate"):
        KE = 0.5 * np.array(m) * (np.array(v) ** 2)
        st.success(f"Kinetic Energy = {KE:.2f} J")

elif formula == "Potential Energy (PE = m * g * h)":
    m = st.number_input("Mass (m) [kg]", value=0.0)
    g = st.number_input("Gravitational acceleration (g) [m/s²]", value=9.8)
    h = st.number_input("Height (h) [m]", value=0.0)
    if st.button("Calculate"):
        PE = np.array(m) * np.array(g) * np.array(h)
        st.success(f"Potential Energy = {PE:.2f} J")

elif formula == "Ohm's Law (V = I * R)":
    I = st.number_input("Current (I) [A]", value=0.0)
    R = st.number_input("Resistance (R) [Ω]", value=0.0)
    if st.button("Calculate"):
        V = np.array(I) * np.array(R)
        st.success(f"Voltage = {V:.2f} V")