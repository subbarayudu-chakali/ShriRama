import time
import streamlit as st

st.set_page_config(
    page_title="శ్రీ రామచంద్ర పరబ్రహ్మణే నమః",
    page_icon="🚩",
    layout="centered",
    initial_sidebar_state="auto",
)

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 3rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #15d888;'>జై శ్రీ రామ్ 🚩</h1>", unsafe_allow_html=True)
ramakoti_tab, songs_tab, gallery_tab,= st.tabs(["శ్రీ రామకోటి [లక్ష నామల లిఖిత జపం]", "శ్రీ రామచంద్రుడి పాటలు", "అయోధ్య ఫోటోలు"])
# with video_tab:
#     st.subheader("Ram Mandir Live Video / "అయోధ్య రామమందిరం లైవ్ వీడియో"", divider="rainbow")
#     st.info("Log back on 22 January 2024 for the live video :) ")
with gallery_tab:
    st.info("We are collecting Photos for you :) ")
with songs_tab:
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
    with st.expander("పలికినంత పుణ్యమే శ్రీ రామ నామము"):
        st.write('''
        **సాకి...**
        
        దాశరథి కరుణాపయోనిధీ...... వినరా....మొరా..... రఘువంశ రాఘవా...


        **పల్లవి...** 

        పలికినంత పుణ్యమే శ్రీ రామ నామము 

        రాఘవ మమ్ము కావాలా.. రాఘవ మమ్ము బ్రోవరా


        **చరణం...** 

        కఠినమైన బోయవాన్ని పరమాత్మగ చేసిన 

        వాల్మికికి ప్రియమైనది శ్రీరామ నామము 

        దైవమే తన వెంగిలి ఫలములు తిన్నాడని 

        శబరికెంతొ ప్రయమైనది శ్రీరామ నామము

 

        ||పలికి||


        **చరణం....** 

        బందికాన జీవితాన బరువును నిలిపేవని 

        భక్త రామదాసుని నిక్కమైన నామము 

        అణువులోన తనువులోన నిలువెల్ల నీవేనని 

        గుండె చీల్చి చూపిన హనుమలోని నామం 
        
        ||పలికి||

        **చరణం...** 

        కలుశాత్ముడు రావణుని ఎదురొడ్డి నిలిచిన 

        జరాయువుకు ప్రయమైనది శ్రీరామ నామము 

        యజ్ఞ యాగాదులందు రాక్షసులు పగ బూనగ 

        మునివర్యులు పలికినది శ్రీరామ నామము
        ''')
    with st.expander("అయోధ్యలో వీరబూసేనే కదా ఆ నాటి రామ కథ"):
        st.write('''
        అయోధ్యలో వీరబూసేనే కదా ఆ నాటి రామ కథ నే మరువలేను కదా

        ఆ… ఆ… ఆ…  నే మరువలేను కదా

        దశరథ పుత్రుడవయ్యా అయోధ్య రామయ్యా
        
        తండ్రి ఆనతి కోరకు అడవులక్ వేగవయ్య

        **||అయోధ్యలో ||**

        నీ నామం వినరాగానే నీ గుడి కి చేరమయ్యా
        
        భక్తులను బ్రోవగా రావ భద్రాద్రి రామయ్యా

        **||అయోధ్యలో ||**

        ప్రతి గుడి కి నీవు తిరిగి ఏ గుడి నీసరి లేక
        
        భద్రాచలము నందు స్థిరముగా వెలసితివయ్యా

        **||అయోధ్యలో ||**
        
        అనుదినము నీదు భజన ఆనందముగా చేసె
        
        ఆప్తులను బ్రోవగా రావా అయోధ్య రామయ్యా

        **||అయోధ్యలో ||**
        ''')

    st.info("We are collecting more songs for you :) ")
with ramakoti_tab:
    st.info("Expected date to start this Japa is 25 December 2023.")