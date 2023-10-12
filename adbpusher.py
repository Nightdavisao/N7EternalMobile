import subprocess, sys, argparse, os

from grabber import grab_files

# if you happen to have more than one device attached this script WILL fail
# todo: handle more than one device
def main(src_path, dst_path, serial, full_game_dir):
    devices_stdout = subprocess.run(args=["adb", "devices"], capture_output=True).stdout
    if serial == "all":
        print("pushing to all devices")
        devices = devices_stdout.decode("utf-8").split("\n")[1:-2]
        devices = [device.split("\t")[0] for device in devices]
    else:
        print(f"pushing to device {serial}")
        devices = [serial]

    files = None
    if full_game_dir:
        files = os.listdir(src_path)
        print("pushing all files first")
        for serial in devices:
            # create the directory if it doesn't exist
            subprocess.call(args=["adb", "-s", serial, "shell", "mkdir", "-p", dst_path])
            # push all files
            subprocess.call(args=["adb", "-s", serial, "push", full_game_dir + ".", dst_path])

    files = grab_files("diff.patch")
    print("pushing modified files")    
    push_files(src_path, dst_path, files, devices)

def push_files(src_path, dst_path, files, devices):
    for serial in devices:
        for file_path in files:
            print(f"sending file {file_path}")
            subprocess.call(args=["adb", "-s", serial, "push", file_path, dst_path], cwd=src_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pushes modified files to an Android device with adb")
    parser.add_argument("src_path", help="path to the source directory")
    parser.add_argument("--dst_path", help="path to the destination directory", default="/sdcard/Android/data/org.love2d.android/files/games/lovegame/")
    parser.add_argument("-s", "--serial", help="specify a device serial number", default="all")
    parser.add_argument("--fullgamedir", help="push all files (not only modified)", default=False)
    args = parser.parse_args()
    main(args.src_path, args.dst_path, args.serial, args.fullgamedir)