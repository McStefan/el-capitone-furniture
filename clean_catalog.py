import os
import glob

catalog_dir = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\images\catalog"
all_images = glob.glob(os.path.join(catalog_dir, "*.png"))

removed_count = 0
kept_count = 0

for img in all_images:
    basename = os.path.basename(img)
    try:
        # Expected format: page_2-img_1.png
        parts = basename.split('-')
        page_num = int(parts[0].replace('page_', ''))
        img_num = int(parts[1].split('.')[0].replace('img_', ''))
    except Exception as e:
        continue
        
    # PDF parsing extracts a lot of sub-layers. 
    # The main photo is ALWAYS img_1.png on the page.
    # Also, page 0 and 1 are title pages without furniture.
    if page_num < 2 or img_num != 1:
        os.remove(img)
        removed_count += 1
    else:
        # Additionally, remove anything smaller than 100KB to be absolutely sure we don't keep solid color blocks
        size = os.path.getsize(img)
        if size < 100 * 1024:
            os.remove(img)
            removed_count += 1
        else:
            kept_count += 1

print(f"Cleanup complete. Removed {removed_count} artifacts/backgrounds. Kept {kept_count} real furniture photos.")
