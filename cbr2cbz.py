import os
import patoolib


def process_cbr2zip(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.cbr'):
                rar_filename = os.path.join(root, file)
                zip_filename = rar_filename.replace('.cbr','.cbz')

                # Extract files from RAR archive
                patoolib.repack_archive(rar_filename, zip_filename)

                os.remove (rar_filename)


# Example usage:
input_dir = "F:/Comics/"
process_cbr2zip (input_dir)

print(f"Program complete")
