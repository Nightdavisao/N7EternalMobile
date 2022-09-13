# grabs modified files from the unified diff

def grab_files(diff_path="diff.patch", strip_slashes = 1):
    grabbed = []
    with open(diff_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("+++"):
                stripped = line[4:line.find('\t')]
                idx = 0
                while idx < strip_slashes:
                    stripped = stripped[stripped.find('/')+1:]
                    idx += 1
                grabbed.append(stripped)
        f.close()
        return grabbed