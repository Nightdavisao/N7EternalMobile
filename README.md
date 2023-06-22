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
7. Now you're ready to play by opening the engine app.
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
8. Now you're ready to play by opening the engine app.
</details>
<details>
<summary markdown="span">ADB way (if you have a working computer)</summary>
### Transferring the whole game from a PC to your Android device
* First of all, [you should have the game already downloaded](https://www.mediafire.com/file/nshjldhr3zzm760/n7e.love/file).
* Also, you should make sure your device has enough free space (at least 5 GBs).  
* Download the [SDK platform-tools](https://developer.android.com/studio/releases/platform-tools) to be able to transfer the whole game to your device. 
* Download the LÖVE engine's APK [here](https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk) and install it in your device.
1. Create an folder somewhere in your computer called `games`, then create another folder named `lovegame` inside this folder.
2. Extract the game's .love file to the `lovegame` folder using some extract tool (such as WinRAR, 7zip), you can extract it through the `Open with...` option when you right click the file or opening the extract tool and navigating to the file's location, but notice that all the extracted files should be inside this folder.
3. Download the pre-patched game files [here](https://github.com/Nightdavisao/N7EternalMobile/releases/latest) and extract over the `lovegame` folder, overwriting the already existing files.
4. Now we just need to transfer the whole stuff. Extract the downloaded SDK platform-tools somewhere then open a command prompt (aka cmd) by using Windows+R and typing `cmd` then pressing enter.
6. Connect your device with a USB cable.
7. Enable [USB debugging](https://developer.android.com/studio/debug/dev-options).
8. When the command prompt window show up, type `cd` with a space right after `cd`, then drag the `platform-tools` folder to the cmd and then drop it. You should see a location pointing to this folder, just press enter.
9. Type `adb.exe devices`, press enter and check if your device is listed there, if it's not, perhaps you're having driver issues or a bad USB cable and you should google the problem if it's the former. The instant you enter this command a prompt will show up in your device (unlock the device if you don't see it) asking if you want to allow USB debugging, just allow it.
10. Type the following command: `adb.exe push (the location pointing to the 'games' folder) /sdcard/Android/data/org.love2d.android/files/`. You can just drag the `games` folder to the cmd and then drop it like you did before for the `cd` command. After all that, press enter and wait for the transfer get done.
11. Now you can just open the game by opening the game's engine app ("LÖVE for Android").
</details>