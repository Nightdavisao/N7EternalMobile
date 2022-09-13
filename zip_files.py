# script that zips the modified files

import sys, zipfile, os
from grabber import grab_files
# todo: use argparse
game_path = sys.argv[1]
zip_name = sys.argv[2]

def main():
    with zipfile.ZipFile(zip_name, "w") as archive:
        modified_files = grab_files()
        for file_path in modified_files:
            archive.write(os.path.join(game_path, file_path), arcname=file_path)
        archive.close()


if __name__ == "__main__":
    main()