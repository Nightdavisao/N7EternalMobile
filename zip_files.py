import sys, zipfile, os
game_path = sys.argv[1]


with open('diff.patch', 'r') as f:
    lines = f.readlines()
    with zipfile.ZipFile("patch_foda.zip", "w") as archive:
        for line in lines:
            # this grabs the modified files
            if line.startswith("+++"):
                stripped = line[4:line.find('\t')]
                stripped = stripped[stripped.find('/')+1:]
                archive.write(os.path.join(game_path, stripped), arcname=stripped)
        archive.close()

    f.close()