import os
from PIL import Image

# --- SETTINGS ---
input_folder = "input_images"        # Folder containing original images
output_folder = "output_images"      # Folder to save resized/converted images
new_size = (800, 800)                # Width, Height (change as needed)
output_format = "JPEG"               # Options: JPEG, PNG, WEBP, etc.
quality = 90                         # For JPEG/WebP quality (0–100)

# --- Ensure output folder exists ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- Process all images ---
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize with ANTIALIAS (smooth)
        img = img.resize(new_size, Image.LANCZOS)

        # Create output filename (change extension based on format)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, base_name + "." + output_format.lower())

        # Save in desired format
        img.save(output_path, output_format, quality=quality)

        print(f"Processed: {filename} → {output_path}")

print("\n✔️ Batch resizing complete!")
