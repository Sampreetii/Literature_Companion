import streamlit as st
import re
import html


from utils import process_text
from pdf_utils import extract_text_from_pdf
from book_utils import split_book



# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(

    page_title="Literature Companion",

    page_icon="📚",

    layout="wide"

)




# -----------------------------------
# SESSION STATE
# -----------------------------------


if "chunks" not in st.session_state:

    st.session_state.chunks = []



if "page" not in st.session_state:

    st.session_state.page = 0



if "cache" not in st.session_state:

    st.session_state.cache = {}





# -----------------------------------
# HELPERS
# -----------------------------------


def add_tooltips(text, words):


    text = html.escape(text)


    for word, meaning in words.items():


        tooltip = (

            f"<span class='tooltip'>{word}"

            f"<span class='tooltiptext'>{meaning}</span>"

            f"</span>"

        )


        text = re.sub(

            rf"\b{re.escape(word)}\b",

            tooltip,

            text,

            flags=re.IGNORECASE

        )


    return text.replace(
        "\n",
        "<br><br>"
    )





# -----------------------------------
# CSS
# -----------------------------------


st.markdown(
"""
<style>


.reader {

font-size:19px;

line-height:1.9;

}



.tooltip {

color:#FFD369;

font-weight:bold;

cursor:pointer;

position:relative;

}



.tooltip .tooltiptext {

visibility:hidden;

position:absolute;

background:#222;

color:white;

padding:10px;

border-radius:8px;

width:220px;

top:120%;

left:50%;

transform:translateX(-50%);

z-index:999;

font-size:14px;

}



.tooltip:hover .tooltiptext {

visibility:visible;

}



.word-card {

padding:12px;

margin-bottom:10px;

border-radius:10px;

background-color:rgba(255,255,255,0.05);

font-size:17px;

}



</style>
""",

unsafe_allow_html=True

)





# -----------------------------------
# HEADER
# -----------------------------------


st.title(
    "📚 Literature Companion"
)



st.write(

    "Read classic books in modern English without losing their soul."

)






# -----------------------------------
# SETTINGS
# -----------------------------------


level = st.select_slider(

    "Reading Style",

    [

        "Simple",

        "Modern",

        "Literary"

    ],

    value="Modern"

)



show_original = st.checkbox(

    "Show original text",

    value=False

)



show_notes = st.checkbox(

    "Show reader notes",

    value=True

)



show_meaning = st.checkbox(

    "Show deeper meaning",

    value=True

)





# -----------------------------------
# INPUT
# -----------------------------------


uploaded_file = st.file_uploader(

    "Upload a classic book PDF",

    type=["pdf"]

)




paste_text = st.text_area(

    "Or paste a passage",

    height=180

)






if st.button(
    "Load Text"
):


    text = ""


    if uploaded_file:


        text = extract_text_from_pdf(
            uploaded_file
        )



    elif paste_text.strip():


        text = paste_text



    else:


        st.warning(
            "Upload a PDF or paste text."
        )



    if text:


        st.session_state.chunks = split_book(
            text
        )


        st.session_state.page = 0


        st.session_state.cache = {}


        st.success(

            f"Loaded {len(st.session_state.chunks)} reading sections."

        )







# -----------------------------------
# READER
# -----------------------------------


if st.session_state.chunks:



    current_page = st.session_state.page



    current_text = (

        st.session_state
        .chunks[current_page]

    )



    st.caption(

        f"Page {current_page + 1} / {len(st.session_state.chunks)}"

    )





    # AI CACHE CHECK


    if current_page not in st.session_state.cache:



        with st.spinner(
            "Preparing your modern version..."
        ):


            st.session_state.cache[current_page] = process_text(

                current_text,

                level

            )






    result = st.session_state.cache[
        current_page
    ]





    modern = result[
        "modern_version"
    ].replace(
        "\n",
        "<br><br>"
    )



    words = result.get(
        "difficult_words",
        {}
    )



    phrases = result.get(
        "old_phrases",
        {}
    )



    insight = result.get(
        "reader_insight",
        ""
    )







    # --------------------------
    # TEXT DISPLAY
    # --------------------------


    if show_original:



        left,right = st.columns(2)



        with left:


            st.subheader(
                "📖 Original"
            )


            original = add_tooltips(

                current_text,

                words

            )


            st.markdown(

                f"<div class='reader'>{original}</div>",

                unsafe_allow_html=True

            )





        with right:


            st.subheader(
                "✨ Modern Version"
            )


            st.markdown(

                f"<div class='reader'>{modern}</div>",

                unsafe_allow_html=True

            )





    else:


        st.subheader(
            "✨ Modern Version"
        )


        st.markdown(

            f"<div class='reader'>{modern}</div>",

            unsafe_allow_html=True

        )







    # --------------------------
    # NAVIGATION
    # --------------------------


    prev,next = st.columns(2)



    with prev:


        if st.button(
            "⬅ Previous"
        ):


            if st.session_state.page > 0:


                st.session_state.page -= 1


                st.rerun()






    with next:


        if st.button(
            "Next ➡"
        ):


            if (

                st.session_state.page

                < len(st.session_state.chunks)-1

            ):


                st.session_state.page += 1


                st.rerun()








    # --------------------------
    # NOTES
    # --------------------------


    if show_notes:


        st.divider()


        st.header(
            "🧠 Reader Notes"
        )


        with st.container(
            border=True
        ):



            for word, meaning in words.items():


                st.markdown(

                    f"""

                    <div class='word-card'>

                    <b>{word}</b><br>

                    {meaning}

                    </div>

                    """,

                    unsafe_allow_html=True

                )




            for phrase, meaning in phrases.items():


                st.markdown(

                    f"""

                    <div class='word-card'>

                    <b>{phrase}</b><br>

                    {meaning}

                    </div>

                    """,

                    unsafe_allow_html=True

                )






    if show_meaning and insight:


        st.divider()


        st.header(
            "💭 Understanding"
        )


        with st.container(
            border=True
        ):


            st.markdown(
                insight
            )