import re


def clean_text(text):

    """
    Cleans extracted PDF text.
    """

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )


    text = re.sub(
        r"[ ]+",
        " ",
        text
    )


    return text.strip()





def split_book(text, chunk_size=2200):

    """
    Splits books into comfortable reading pages.
    """

    text = clean_text(
        text
    )


    paragraphs = text.split(
        "\n\n"
    )


    chunks = []


    current = ""



    for paragraph in paragraphs:


        if len(current) + len(paragraph) <= chunk_size:


            current += paragraph + "\n\n"



        else:


            if current.strip():

                chunks.append(
                    current.strip()
                )


            current = paragraph + "\n\n"





    if current.strip():


        chunks.append(
            current.strip()
        )




    return chunks