import zipfile
import pathlib


def make_archive(filepaths, destination_dir):
    dest_dir = pathlib.Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(dest_dir, 'w') as archive:
        for filepath in filepaths:
            # we use arcname and line 14 to just compress that file without their parent file
            # otherwise we compressed each file with their parents file for instance:
            # Users/Desktop/archive/a.pdf

            # filepath = "PosixPath(a.py)" -> filepath.name = a.py
            filepath = pathlib.Path(filepath)  # this code will convert the pure path into Posix path

            archive.write(filepath, arcname=filepath.name)
