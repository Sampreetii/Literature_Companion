from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    pages = []


    for page in reader.pages:

        text = page.extract_text()


        if text:

            pages.append(
                text.strip()
            )


    final_text = "\n\n".join(
        pages
    )


    lines = final_text.splitlines()


    # remove PDF heading/title
    if len(lines) > 1:

        lines = lines[1:]


    return "\n".join(lines)