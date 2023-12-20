import streamlit as st

st.set_page_config(
    page_title="శ్రీ రామచంద్ర పరబ్రహ్మణే నమః",
    page_icon="🚩",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("జై శ్రీ రామ్ 🚩")

# create sidebar for the following options 1. Ram Mandir live video, 2. Ayodhya Gallery 3. శ్రీ రామచంద్రుడి పాటలు
sidebar_options = st.sidebar.selectbox(
    "Select an option", ("అయోధ్య రామమందిరం లైవ్ వీడియో", "అయోధ్య ఫోటోలు", "శ్రీ రామచంద్రుడి పాటలు"))
if sidebar_options == "అయోధ్య రామమందిరం లైవ్ వీడియో":
    st.subheader("Ram Mandir Live Video", divider="rainbow")

if sidebar_options == "అయోధ్య ఫోటోలు":
    st.subheader("Ayodhya Gallery", divider="rainbow")

if sidebar_options == "శ్రీ రామచంద్రుడి పాటలు":
    with st.expander("హరే కృష్ణ మంత్రం"):
        st.write("హరే కృష్ణ హరే కృష్ణ\n"
                 "\nకృష్ణ కృష్ణ హరే హరే ||\n"
                 "\nహరే రామ హరే రామ\n"
                 "\nరామ రామ హరే హరే ||")
    with st.expander("హరే కృష్ణ మంత్రం English"):
        st.write("Hare Krishna Hare Krishna, Krishna Krishna Hare Hare\n"
                 "\nHare Rama Hare Rama , Rama Rama Hare Hare")
    with st.expander("హరే కృష్ణ మంత్రం हिंदी"):
        st.write("हरे कृष्ण हरे कृष्ण\n"
                 "\nकृष्ण कृष्ण हरे हरे ||\n"
                 "\nहरे राम हरे राम\n"
                 "\nराम राम हरे हरे ||")
