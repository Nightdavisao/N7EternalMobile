# Never7 Eternal Edition for Android
A patch to make the game playable on Android (only for Android devices)
* [What's working](#whats-working)
* [Notes](#notes)
* [Saving](#saving)
* [FAQ](#faq)
* [Gameplay](#gameplay)
* [How to install it](#how-to-install)
## Notes
* The game is automatically saved when it loses its focus (when it's running in background or when you open the system's notification panel) and there's no option to disable the auto saving for now.
* The sound won't pause if you leave the game open in background.
* Connecting a headset/headphone while the game is open won't route the sound to the connected device but instead it will stop playing any sound. Connect whatever you want to connect first and then open the game. This seems to be a problem with the engine itself.
## Saving
By default, everything (save states, system save) is saved to `/data/data/org.love2d.android/files/save/Never7Eternal`, however, if you're an unprivileged user of your own device (if your device isn't rooted), you can't access this directory.  
To change the save directory to an accessible one through common means, replace the `conf.lua` file with this [file](https://files.catbox.moe/eos49l.lua). Now this directory will be `/storage/emulated/0/Android/data/org.love2d.android/save/Never7Eternal`.
## FAQ
*No one really asked me anything below so call it a QA*  
**Q: Does it work on iOS?**  
A: I don't know. [You can tell me](https://www.reddit.com/message/compose/?to=nightdavisao) and I will gladly edit this answer.  
**Q: Does it work with the LÖVE's Play Store version?**  
A: No. Don't even try it. You will miserably fail to make it work, this version is just too outdated.  
**Q: Does transferring the files by the usual way (through the Windows Explorer) works?**  
A: Yes if you believe you can do it. But keep in mind that this is the most slower way to transfer files and it tends to fail.
## Gameplay
You can fast forward, instant skip and open the backlog with the GUI controls. Scrolling the menus using one of your fingers works just fine. 
* Tapping with two fingers goes back or opens the in-game menu
* Double tap the "Skip" text for instant skip, hold it for fast forwarding
## How to install
<details>
<summary markdown="span">Common way (not avaliable for Android 11 and up)</summary>
**BE SURE TO HAVE AT LEAST 8 GIGS OF FREE SPACE IN YOUR DEVICE. (THAT'S PROBABLY THE DOUBLE OF THE GAME'S SIZE)**

1. Download the VN if you haven't already, it's free (KID is defunct and MAGES doesn't care bruh) and you can get it [here](https://www.mediafire.com/file/nshjldhr3zzm760/n7e.love/file).
2. [Download a proper file manager](https://github.com/zhanghai/MaterialFiles/releases/latest), we will need it to transfer the game files to the right directory.  
3. Download the [LÖVE engine's APK](https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk)
4. Install everything you downloaded (I'm talking about the APKs, not the VN)
5. Extract the game's .love file to `(Internal storage)/Android/data/org.love2d.android/files/games/lovegame` using the file manager you downloaded. (You can extract it through the `Open with...` option when you long press the file and click the three dots on the top right corner. Rename the file to `n7e.zip` if you can't find the option.)
6. Download the pre-patched game files [here](https://github.com/Nightdavisao/N7EternalMobile/releases/latest) and extract it to the same folder you extracted the game's .love file. Overwrite everything when asked.
7. Now you're ready to play by launching the game's engine app.
</details>
<details>
<summary markdown="span">Android 11 and up way</summary>
**BE SURE TO HAVE AT LEAST 8 GIGS OF FREE SPACE IN YOUR DEVICE. (THAT'S PROBABLY THE DOUBLE OF THE GAME'S SIZE)**

1. Download the VN if you haven't already, it's free (KID is defunct and MAGES doesn't care bruh) and you can get it [here](https://www.mediafire.com/file/nshjldhr3zzm760/n7e.love/file).
2. Download the [LÖVE engine's APK](https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk)
3. Install everything you downloaded. (I'm talking about the APKs, not the VN)
4. Extract the game's .love file to somewhere in your device with a file manager or an archive manager. (You can extract it through the `Open with...` option when you long press the file and click the three dots on the top right corner. Rename the file to `n7e.zip` if you can't find the option.)
5. Download the pre-patched game files [here](https://github.com/Nightdavisao/N7EternalMobile/releases/latest)
6. Extract the patch to the same folder you extracted the game's .love file. Overwrite everything when asked.
7. Transfer the files using your native file manager to `/sdcard/Android/data/org.love2d.android/files/games/lovegame` (Your native file manager is the one that comes with your device, probably it is called "Files" or "My Files")
8. Now you're ready to play by launching the game's engine app.
</details>
<details>
<summary markdown="span">ADB way (if you have a working computer)</summary>
1. Ensure your device has at least 5 GB of free space.
2. Download the game from [here](https://www.mediafire.com/file/nshjldhr3zzm760/n7e.love/file).
3. Download the [SDK platform-tools](https://developer.android.com/studio/releases/platform-tools) for transferring the game.
4. Download and install the LÖVE engine's APK from [here](https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk).
5. On your computer, create a folder named `games`, and inside it, create another folder called `lovegame`.
6. Extract the game's .love file to the `lovegame` folder using an extraction tool like WinRAR or 7zip. Ensure that all the extracted files are within this folder.
7. Download the pre-patched game files from [here](https://github.com/Nightdavisao/N7EternalMobile/releases/latest).
8. Extract the downloaded files and overwrite the existing files in the `lovegame` folder.
9. Extract the downloaded SDK platform-tools to a location on your computer.
10. Connect your device to your computer using a USB cable.
11. Enable USB debugging on your device. You can find instructions [here](https://developer.android.com/studio/debug/dev-options).
12. Open a command prompt (cmd) on your computer by pressing Windows+R, typing `cmd`, and pressing Enter.
13. In the command prompt, navigate to the location of the extracted platform-tools folder by using the `cd` command.
14. Type `adb.exe devices` in the command prompt and press Enter to verify that your device is listed.
15. If your device is listed, type the following command: `adb.exe push (location path to the 'games' folder) /sdcard/Android/data/org.love2d.android/files/`. Replace `(location path to the 'games' folder)` with the actual path to the `games` folder on your computer.
16. Press Enter and wait for the transfer to complete.
17. Launch the LÖVE engine app on your Android device to open and play the game.
</details>