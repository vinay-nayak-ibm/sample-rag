import streamlit as st
import pandas as pd

csv_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vT95ra61mikEmqFkP44oq2VotHf5CW5NNQTYZ4Q-DZa3CvFAk_GrdBePrxEaL17WHsCsw7mjKiI_Ufo/pub?gid=0&single=true&output=csv'
df=pd.read_csv(csv_file)
st.data_editor(
    df,
    column_config={
        "apps": st.column_config.TextColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        ),
                "C4": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    width=1000,
    height=1000,
    hide_index=True,
)

