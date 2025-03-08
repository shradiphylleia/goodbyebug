from data import dataframe
import streamlit as st

st.logo("bug.png")
st.header("goodbyebug 🐛")
st.subheader("search based on the type of pest")

pest=st.text_input(label="enter the name of the pest to search",help="enter the name of the pest, to get recommendation.")



if st.button(label='search'):
    if pest:
        pest_lower=pest.lower()
        filtered_df=dataframe[dataframe["Pest Name"].str.lower()==pest_lower]
        
        if not filtered_df.empty:
            filtered_df.set_index('Most Commonly Used Pesticides',inplace=True)
            st.write(filtered_df)        
        else:
                st.write("A recommendation is not available at the moment.")

    