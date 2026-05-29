def split_book(text, chunk_size=3500):

    """
    Splits long books into readable chunks.
    Keeps paragraphs together.
    """

    paragraphs = text.split("\n\n")


    chunks = []


    current = ""



    for paragraph in paragraphs:


        if len(current) + len(paragraph) <= chunk_size:


            current += paragraph + "\n\n"


        else:


            chunks.append(
                current.strip()
            )


            current = paragraph + "\n\n"




    if current.strip():


        chunks.append(
            current.strip()
        )



    return chunks