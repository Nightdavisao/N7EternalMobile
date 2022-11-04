# Never7 Eternal Edition for Android
A patch to make the game playable on Android (only for Android devices)
* [What's working](#whats-working)
* [Notes](#notes)
* [Saving](#saving)
* [TODO](#todo)
* [FAQ](#faq)
* [Gameplay](#gameplay)
* [How to install it](#how-to-use-this-patch-to-play-the-vn)
## What's working
* Opening the game (couldn't open before without removing some pixel shader that for some reason doesn't work)
* Playing the game (couldn't play before because scaling problems)
* Unlocked aspect ratio (the game will be draw in a safe area where it isn't obstructed by the phone's screen notch or the system UI)
* Opening the pause menu and backlog in-game
* Scrolling in backlog, playing log and the shortcut menu ("flow menu")
* Fast forwarding and instant skip
## Notes
* The game is automatically saved when it loses its focus (when it's running in background or when you open the system's notification panel) and there's no option to disable the auto saving for now.
* The sound won't pause if you leave the game open in background.
* Connecting a headset/headphone while the game is open won't route the sound to the connected device but instead it will stop playing any sound. Connect whatever you want to connect first and then open the game. This seems to be a problem with the engine itself.
## Saving
By default, everything (save states, system save) is saved to `/data/data/org.love2d.android/files/save/Never7Eternal`, however, if you're an unprivileged user of your own device (if your device isn't rooted), you can't access this directory.  
To change the save directory to an accessible one through common means, replace the `conf.lua` file with this [file](https://files.catbox.moe/eos49l.lua). Now this directory will be `/storage/emulated/0/Android/data/org.love2d.android/save/Never7Eternal`.
## TODO
* ~~GUI elements for instant skip and fast forwarding~~ (done in v0.2)
* maybe more...
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
## How to use this patch to play the VN
Below I explain how to transfer the game using Android's ADB in a Windows enviroment. If you're familiar with ADB and stuff already, I assume you just need to read this: Install the [LÖVE engine's APK](https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk), extract the game file (it's just a compressed zip file), [download](https://github.com/Nightdavisao/N7EternalMobile/releases/latest) and extract the patch over the extracted game, then transfer the files to `/sdcard/Android/data/org.love2d.android/files/games/lovegame` and now you're ready to play by opening the engine app.  
Of course, if you're not locked behind [Google's storage restrictions](https://developer.android.com/about/versions/11/privacy/storage#file-access) (this only applies in Android 11 and up), you can do all of this without relying on a computer, but will it take the double of the free space you need (about 10 GBs). 
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
