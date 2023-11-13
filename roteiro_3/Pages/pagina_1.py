
import streamlit as st 
import numpy as np 
tab1,tab2 = st.tabs(['tab 1 ','tab 2'])

with tab1: 
    with st.expander("expander teste"): 
        st.write("aqui é um expander")

with tab2: 
    with st.container():
        col1,col2,col3 = st.columns([1,2,3])
        with col1: 
            st.write("aqui é um expander")
        with col2: 
                    st.write("aqui é um expander")
        with col3: 
            st.write("aqui é um expander")
    with st.container():
        st.write('Outro container aq ')
    with st.container():
        st.write("This is inside the container")

        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

    st.write("This is outside the container")