import fitz
import os
import json

pdf_path = "sample.pdf"
output_folder = "static/output_images"
os.makedirs(output_folder, exist_ok=True)
doc = fitz.open(pdf_path)
extracted_data = []
for page_num, page in enumerate(doc, start=1):
    text = page.get_text().strip()
    image_list = page.get_images(full=True)
    image_paths = []

    for img_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_filename = f"page{page_num}_image{img_index}.{image_ext}"

        image_path = os.path.join(output_folder, image_filename)
        with open(image_path, "wb") as f:
            f.write(image_bytes)

        web_path = os.path.join("static", "output_images", image_filename).replace("\\", "/")
        image_paths.append(web_path)

    extracted_data.append({
        "page": page_num,
        "text": text,
        "images": image_paths
    })

doc.close()

structured_output = []

for entry in extracted_data:
    page_number = entry["page"]
    text = entry["text"]
    images = entry["images"]

    if not images:
        continue

    i = 0
    while i < len(images):
        q_block = {
            "question": f"From page {page_number}: {text[:100]}...",
            "images": images[i] if i < len(images) else None,
            "option_images": []
        }
        for j in range(1, 4):
            if i + j < len(images):
                q_block["option_images"].append(images[i + j])
        structured_output.append(q_block)
        i += 4

with open("structured_output.json", "w") as f:
    json.dump(structured_output, f, indent=2)

print("JSON and images generated successfully.")
