import streamlit as st
pages={
    "Pest control":[
        st.Page("app.py",title="find the pest using image"),
        st.Page("suggestion.py",title="techniques to curb pests"),
        st.Page("pesticides.py",title="pesticide suggestion")
    ],
    "General":[
        st.Page("about.py",title="about")
    ]
}

pg=st.navigation(pages)
pg.run()