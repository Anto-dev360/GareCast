"""
app.py

Main entry point for GareCast project.

Author: Anthony Morin
Created: 2025-05-23
Project: GareCast
License: MIT
"""

import streamlit as st

from config import settings

st.set_page_config(page_title=settings.STREAMLIT_PAGE_TITLE)

def main():
    st.title("📊 GareCast – Prédiction de l'affluence en gares")
    st.markdown("Ce projet utilise des réseaux de neurones pour estimer la fréquentation hebdomadaire des gares SNCF.")

    # Future logic here (load data, preprocess, predict, visualize)

if __name__ == "__main__":
    main()
