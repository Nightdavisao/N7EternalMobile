# script that pushes modified files to an android device with adb
import subprocess, sys

from grabber import grab_files
# todo: use argparse
game_path = sys.argv[1]
lovegame_path = "/sdcard/Android/data/org.love2d.android/files/games/lovegame/"

# if you happen to have more than one device attached this script WILL fail
# todo: handle more than one device
def main():
    # wake the adb process
    subprocess.call("adb devices")
    modified_files = grab_files()
    for file_path in modified_files:
        print("sending file {}".format(file_path))
        process = subprocess.Popen(args=["adb", "push", file_path, lovegame_path], 
        cwd=game_path, stdout=subprocess.PIPE, shell=True)
        output = process.communicate()[0].decode('utf-8')
        print(output)

if __name__ == "__main__":
    main()