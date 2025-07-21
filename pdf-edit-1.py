import fitz  # PyMuPDF
from datetime import datetime

# File paths
pdf_path = "bobs-fruit.pdf"  # Replace with your actual PDF file
font_path = "Lucida Calligraphy Bold.otf" # Replace with your actual font file

# Generate a unique output file name with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f"bobs_fruit_{timestamp}.pdf"

# Open the PDF
doc = fitz.open(pdf_path)

# Register the custom font
custom_font = fitz.Font(fontfile=font_path)
custom_font_name = "LucidaCalligraphyBold"

# Loop through each page
for page_num in range(doc.page_count):
    page = doc[page_num]
    instances_apples = page.search_for("apples")
    instances_oranges = page.search_for("oranges")

    # Combine and sort instances by vertical position
    instances = sorted(instances_apples + instances_oranges, key=lambda inst: inst.y0)

    for inst in instances:
        # Extract the full line containing the word
        text_dict = page.get_text("dict", clip=fitz.Rect(0, inst.y0, page.rect.width, inst.y1))
        try:
            line = text_dict["blocks"][0]["lines"][0]
            full_line_text = "".join([span["text"] for span in line["spans"]])
            font_size = line["spans"][0]["size"]
            y_position = line["spans"][0]["origin"][1]
        except (IndexError, KeyError):
            continue

        # Skip lines containing "apples, red delicious"
        if "apples, red delicious" in full_line_text:
            continue

        # Remove the entire line
        page.add_redact_annot(fitz.Rect(0, inst.y0, page.rect.width, inst.y1), fill=(1, 1, 1))
        page.apply_redactions()

        # Center the line using the custom font
        line_width = custom_font.text_length(full_line_text, fontsize=font_size)
        x_position = (page.rect.width - line_width) / 2

        # Reinsert the full line in the custom font
        page.insert_text(
            (x_position, y_position),
            full_line_text,
            fontname=custom_font_name,
            fontfile=font_path,
            fontsize=font_size,
            color=(0, 0, 0),
        )

# Save the updated PDF
doc.save(output_path)
print(f"✅ Updated PDF saved as: {output_path}")
