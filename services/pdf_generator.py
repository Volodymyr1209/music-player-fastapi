from fpdf import FPDF


def generate_artist_report(
    filename: str,
    artists: list[str],
) -> str:
    pdf = FPDF()

    pdf.add_page()

    pdf.add_font(
        "DejaVu",
        "",
        "fonts/DejaVuSans.ttf",
    )

    pdf.set_font("DejaVu", size=16)

    pdf.cell(
        0,
        10,
        "Artists Report",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C",
    )

    pdf.ln(10)

    pdf.set_font("DejaVu", size=12)

    for artist in artists:
        pdf.cell(
            0,
            10,
            artist,
            new_x="LMARGIN",
            new_y="NEXT",
        )

    pdf.output(filename)

    return filename
