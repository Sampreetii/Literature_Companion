import streamlit as st
import re
import html

from utils import process_text
from pdf_utils import extract_text_from_pdf


st.set_page_config(
    page_title="Literature Companion",
    page_icon="📚",
    layout="wide"
)



# ----------------------------
# Tooltip generator
# ----------------------------

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


    text = text.replace(
        "\n",
        "<br><br>"
    )


    return text




# ----------------------------
# Styling
# ----------------------------

st.markdown(
"""
<style>


.reader {

font-size:19px;

line-height:1.9;

letter-spacing:0.2px;

}



.note-text {

font-size:18px;

line-height:1.8;

}



.word-card {

font-size:17px;

padding:12px;

margin-bottom:10px;

border-radius:10px;

background-color:rgba(255,255,255,0.04);

}



.tooltip{

color:#FFD369;

font-weight:bold;

position:relative;

cursor:pointer;

}



.tooltip .tooltiptext{

visibility:hidden;

position:absolute;

background:#222;

color:white;

padding:10px;

border-radius:10px;

width:230px;

top:120%;

left:50%;

transform:translateX(-50%);

z-index:999;

font-size:14px;

}



.tooltip:hover .tooltiptext{

visibility:visible;

}


</style>
""",
unsafe_allow_html=True
)





# ----------------------------
# Header
# ----------------------------

st.title(
    "📚 Literature Companion"
)


st.write(
    "Experience classic books in modern English without losing their soul."
)




# ----------------------------
# Options
# ----------------------------


level = st.select_slider(

    "Reading Style",

    [
        "Simple",
        "Modern",
        "Literary"
    ],

    value="Modern"

)



show_notes = st.checkbox(

    "Show vocabulary and old expressions",

    value=True

)



show_meaning = st.checkbox(

    "Show deeper meaning",

    value=True

)




# ----------------------------
# Input
# ----------------------------


uploaded_file = st.file_uploader(

    "Upload a classic book PDF",

    type=["pdf"]

)



text = st.text_area(

    "Or paste a passage",

    height=250

)




if uploaded_file:


    text = extract_text_from_pdf(
        uploaded_file
    )


    st.success(
        "Book loaded successfully"
    )






# ----------------------------
# Processing
# ----------------------------


if st.button(
    "Transform Text"
):


    if not text.strip():


        st.warning(
            "Please enter text first"
        )



    else:


        with st.spinner(
            "Understanding the story..."
        ):


            result = process_text(
                text,
                level
            )




        modern = result[
            "modern_version"
        ]


        modern = modern.replace(
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





        original = add_tooltips(
            text,
            words
        )





        # ----------------------------
        # Reading View
        # ----------------------------


        col1, col2 = st.columns(2)




        with col1:


            st.subheader(
                "📖 Original"
            )


            st.markdown(

                f"""
                <div class='reader'>
                {original}
                </div>
                """,

                unsafe_allow_html=True
            )





        with col2:


            st.subheader(
                "✨ Modern Version"
            )


            st.markdown(

                f"""
                <div class='reader'>
                {modern}
                </div>
                """,

                unsafe_allow_html=True
            )





        # ----------------------------
        # Reader Notes
        # ----------------------------


        if show_notes:


            st.divider()


            st.header(
                "🧠 Reader Notes"
            )



            with st.container(
                border=True
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







        # ----------------------------
        # Meaning
        # ----------------------------


        if show_meaning and insight:


            st.divider()


            st.header(
                "💭 Understanding the Passage"
            )



            with st.container(
                border=True
            ):


                st.markdown(

                    f"""
                    <div class='note-text'>
                    {insight}
                    </div>
                    """,

                    unsafe_allow_html=True
                )