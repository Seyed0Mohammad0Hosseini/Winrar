import zipfile


def archive_extractor(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)
