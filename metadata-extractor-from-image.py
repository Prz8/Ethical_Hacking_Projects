import piexif

image_name = '<path_to_image>.jpg'
exif_dict = piexif.load(image_name)

# Extract thumbnail and save it, if exists
thumbnail = exif_dict.pop('thumbnail')
if thumbnail is not None:
    with open('thumbnail.jpg', 'wb') as f:
        f.write(thumbnail)

# Iterate through all the other ifd names and print them
print(f'Metadata for {image_name}:')
for ifd in exif_dict:
    print(f'{ifd}:')
    for tag in exif_dict[ifd]:
        tag_name = piexif.TAGS[ifd][tag]["name"]
        tag_value = exif_dict[ifd][tag]
        # Avoid print a large value, just to be pretty
        if isinstance(tag_value, bytes):
            tag_value = tag_value[:10]
        print(f'\t{tag_name:25}: {tag_value}')
print()