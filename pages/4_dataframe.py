import streamlit as st
import pandas as pd

def _max_width_():
    max_width_str = "max-width: 1000px;"
    st.markdown(
        f"""
    <style>
    .block-container {{
        {max_width_str}
        }}
    .custom-widget {{
        display: grid;
        border: 1px solid black;
        padding: 12px;
        border-radius: 5%;
        color: #003366;
        margin-bottom: 5px;
        min-height: 251.56px;
        align-items: center;
    }}
    .row-widget.stCheckbox {{
        display: grid;
        justify-content: center;
        align-items: center;
        border: solid 2px black;
        border-radius: 3%;
        height: 50px;
        background-color: #DF1B88;
        color: #FFFFFF;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

_max_width_()


csv_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vT95ra61mikEmqFkP44oq2VotHf5CW5NNQTYZ4Q-DZa3CvFAk_GrdBePrxEaL17WHsCsw7mjKiI_Ufo/pub?gid=0&single=true&output=csv'
df=pd.read_csv(csv_file)

num_rows=len(df)
st.markdown(f'# Meet our counselors')

for i in range(len(df)):
    with st.container():
        (col1,col2)=st.columns([7,3])
        row = df.iloc[i]
        p=row['Person']
        d=row['Degree']
        de=row['Description']
        ur=row['URL']
        desc=f'## {p} \n### {d}\n {de}'
        col2.image(ur,use_column_width=True)
        col1.markdown(desc)
        if col2.button("Send Conversation",key=f'button{i}'):
            st.write("Conversation sent")
        st.divider()
        print(row)



#df['C4'] = df['C4'].apply(lambda x: f'<img src="{x}" width="100"/>')

#styled_df = df.style.set_table_styles([
#    {"selector": "thead th", "props": [("font-size", "150%"), ("text-align", "center")]},
#    {"selector": "tbody td", "props": [("font-size", "120%"), ("text-align", "center")]}
#])

#html_output = df.to_html(index=False,escape=False)

# Display styled DataFrame in Streamlit
#st.write(html_output, unsafe_allow_html=True)

