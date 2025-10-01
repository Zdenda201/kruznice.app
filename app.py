import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# --- Nastavení aplikace ---
st.set_page_config(page_title="Body na kružnici", layout="centered")
st.title("Body na kružnici")

# --- Vstupy od uživatele ---
x_center = st.number_input("Souřadnice středu X [m]", value=0.0)
y_center = st.number_input("Souřadnice středu Y [m]", value=0.0)
radius = st.number_input("Poloměr [m]", value=5.0, min_value=0.1)
num_points = st.slider("Počet bodů", min_value=1, max_value=100, value=8)
color = st.color_picker("Barva bodů", value="#ff0000")

# --- Výpočet souřadnic bodů ---
angles = np.linspace(0, 2*np.pi, num_points, endpoint=False)
x_points = x_center + radius * np.cos(angles)
y_points = y_center + radius * np.sin(angles)

# --- Vykreslení ---
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.plot(x_center, y_center, 'bo', label="Střed")
ax.scatter(x_points, y_points, color=color, label="Body")
circle = plt.Circle((x_center, y_center), radius, color='gray', fill=False, linestyle='--')
ax.add_patch(circle)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.legend()
st.pyplot(fig)

# --- Export do PDF ---
def generate_pdf():
    doc = SimpleDocTemplate("output.pdf")
    styles = getSampleStyleSheet()
    flow = []

    flow.append(Paragraph("<b>Body na kružnici</b>", styles['Title']))
    flow.append(Spacer(1, 12))
    flow.append(Paragraph(f"Střed: ({x_center}, {y_center}) m", styles['Normal']))
    flow.append(Paragraph(f"Poloměr: {radius} m", styles['Normal']))
    flow.append(Paragraph(f"Počet bodů: {num_points}", styles['Normal']))
    flow.append(Paragraph(f"Barva bodů: {color}", styles['Normal']))
    flow.append(Spacer(1, 24))
    flow.append(Paragraph("<b>Autor:</b> Vaše jméno", styles['Normal']))
    flow.append(Paragraph("<b>Kontakt:</b> vas@email.cz", styles['Normal']))
    flow.append(Paragraph("Použité technologie: Python, Streamlit, Matplotlib, ReportLab", styles['Normal']))

    doc.build(flow)
    with open("output.pdf", "rb") as file:
        st.download_button("Stáhnout PDF", file, file_name="body_na_kruznici.pdf")

if st.button("Vytvořit PDF"):
    generate_pdf()

# --- Informace o aplikaci ---
if st.sidebar.button("O aplikaci"):
    st.sidebar.markdown("""
    ### O aplikaci
    Tato aplikace vykresluje body na kružnici podle zadaných parametrů.
    - Vstupy: střed, poloměr, počet bodů, barva bodů.
    - Výstupy: graf s kružnicí a body, export do PDF.

    **Použité technologie:**
    - Python
    - Streamlit
    - Matplotlib
    - ReportLab

    Autor: *Zdeněk Holub 277850@vutbr.cz*
    """)   
