import streamlit as st
import re
import html


from utils import process_text
from pdf_utils import extract_text_from_pdf
from book_utils import split_book



# ---------------- CONFIG ----------------


st.set_page_config(
    page_title="Literature Companion",
    page_icon="📚",
    layout="wide"
)




# ---------------- SESSION ----------------


defaults = {

    "chunks": [],

    "page": 0,

    "cache": {}

}



for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value






# ---------------- HELPERS ----------------


def format_text(text):


    text = html.escape(
        text
    )


    paragraphs = text.split(
        "\n\n"
    )


    return "".join(

        f"<p>{p.strip()}</p>"

        for p in paragraphs

        if p.strip()

    )





def add_tooltips(text, words):


    text = html.escape(
        text
    )



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




    paragraphs = text.split(
        "\n\n"
    )



    return "".join(

        f"<p>{p}</p>"

        for p in paragraphs

        if p.strip()

    )








# ---------------- STYLE ----------------


st.markdown(
"""
<style>


.block-container {

max-width:1200px;

padding-top:2rem;

}



.reader {

font-size:20px;

line-height:1.75;

max-width:950px;

}



.reader p {

margin-bottom:18px;

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

font-size:14px;

z-index:10;

}



.tooltip:hover .tooltiptext {

visibility:visible;

}



.word-card {

padding:14px;

margin-bottom:12px;

border-radius:10px;

background:rgba(255,255,255,0.05);

}



</style>
""",

unsafe_allow_html=True
)








# ---------------- HEADER ----------------


st.title(
    "📚 Literature Companion"
)



st.write(
    "A modern reading experience for classic literature."
)








# ---------------- SETTINGS ----------------


level = st.select_slider(

    "Reading Style",

    [
        "Simple",

        "Modern",

        "Literary"
    ],

    value="Modern"

)




c1,c2,c3 = st.columns(3)




with c1:


    show_original = st.checkbox(

        "Show Original",

        False

    )





with c2:


    show_notes = st.checkbox(

        "Reader Notes",

        True

    )





with c3:


    show_meaning = st.checkbox(

        "Understanding",

        True

    )









# ---------------- INPUT ----------------


if not st.session_state.chunks:



    uploaded_file = st.file_uploader(

        "Upload PDF",

        type=["pdf"]

    )




    paste_text = st.text_area(

        "Or paste text",

        height=180

    )





    if st.button(
        "📖 Start Reading"
    ):



        text = ""



        if uploaded_file:



            text = extract_text_from_pdf(

                uploaded_file

            )




        elif paste_text.strip():



            text = paste_text






        if text:



            st.session_state.chunks = split_book(

                text

            )



            st.session_state.cache = {}



            st.session_state.page = 0



            st.rerun()






        else:


            st.warning(

                "Upload a PDF or paste text first."

            )









# ---------------- READER ----------------


if st.session_state.chunks:




    page = st.session_state.page



    total = len(

        st.session_state.chunks

    )




    st.caption(

        f"Page {page + 1} of {total}"

    )






    original_text = (

        st.session_state
        .chunks[page]

    )








    if page not in st.session_state.cache:




        with st.spinner(

            "Preparing your page..."

        ):



            st.session_state.cache[page] = process_text(

                original_text,

                level

            )









    result = st.session_state.cache[
        page
    ]






    modern = format_text(

        result["modern_version"]

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









    # ---------- TEXT DISPLAY ----------

    if show_original:

        left, right = st.columns(2)

        with left:

            st.header(
                "📖 Original"
            )

            st.markdown(

                f"""
                <div class="reader">
                {add_tooltips(original_text, words)}
                </div>
                """,

                unsafe_allow_html=True

            )

        with right:

            st.header(
                f"✨ {level} Version"
            )

            st.markdown(

                f"""
                <div class="reader">
                {modern}
                </div>
                """,

                unsafe_allow_html=True

            )

    else:

        st.header(
            f"✨ {level} Version"
        )

        st.markdown(

            f"""
            <div class="reader">
            {modern}
            </div>
            """,

            unsafe_allow_html=True

        )



    # ---------- NAVIGATION ----------

    back, regen, next_page, clear = st.columns(4)

    with back:

        if st.button(
            "⬅ Previous"
        ):

            if page > 0:

                st.session_state.page -= 1

                st.rerun()

    with regen:

        if st.button(
            "🔄 Regenerate"
        ):

            st.session_state.cache.pop(
                page,
                None
            )

            st.rerun()

    with next_page:

        if page < total - 1:

            if st.button(
                "Next ➡"
            ):

                st.session_state.page += 1

                st.rerun()

    with clear:

        if st.button(
            "🗑 Clear Book"
        ):

            st.session_state.chunks = []
            st.session_state.cache = {}
            st.session_state.page = 0

            st.rerun()



    # ---------- NOTES ----------

    if show_notes:

        with st.expander(
            "🧠 Reader Notes"
        ):

            if words:

                st.subheader(
                    "Vocabulary"
                )

                for word, meaning in words.items():

                    st.markdown(

                        f"""
                        <div class="word-card">

                        <b>{word}</b><br>

                        {meaning}

                        </div>
                        """,

                        unsafe_allow_html=True

                    )

            if phrases:

                st.subheader(
                    "Old Expressions"
                )

                for phrase, meaning in phrases.items():

                    st.markdown(

                        f"""
                        <div class="word-card">

                        <b>{phrase}</b><br>

                        {meaning}

                        </div>
                        """,

                        unsafe_allow_html=True

                    )



    # ---------- UNDERSTANDING ----------

    if show_meaning and insight:

        with st.expander(

            "💭 Understanding the Passage"

        ):

            st.write(
                insight
            )