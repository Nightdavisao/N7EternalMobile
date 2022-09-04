# Never7 Eternal Edition for mobile devices
A patch to make the game playable in mobile devices (specifically for Android devices).
* [Notes](#notes)
* [What's working](#whats-working)
* [TODO](#todo)
* [Gameplay](#gameplay)
* [FAQ](#faq)
* [How to install it](#how-to-use-this-patch-to-play-the-vn)
## What's working
* Opening the game (couldn't open before without removing some pixel shader that for some reason doesn't work)
* Playing the game (couldn't play before because scaling problems)
* Unlocked aspect ratio (the game will be draw in a safe area where it isn't obstructed by the phone's screen notch or the system UI)
* Opening the pause menu and backlog in-game
* Scrolling in backlog, playing log and the shortcut menu ("flow menu")
* Fast-forwarding (but for now it's too uncomfortable to do so, though)
## Notes
* The game is automatically saved when it loses its focus (when it's running in background or when you open the system's notification panel) and there's no option to disable the auto saving for now.
* The sound won't pause if you leave the game open in background.
* Connecting a headset/headphone while the game is open won't route the sound to the connected device but instead it will stop playing any sound. Connect whatever you want to connect first and then open the game. This seems to be a problem with the engine itself.
* Don't try to change the game's display resolution. 
## TODO
* GUI elements for instant skip and fast forwarding (almost done)
* maybe more... 
## FAQ
*No one really asked me anything below so call it a QA*  
**Q: Does it work in iOS?**  
A: I don't know. I could ~~steal~~ borrow an iThing from my family and tell you if it works, but instead [you can tell me](https://www.reddit.com/message/compose/?to=nightdavisao) and I will gladly edit this answer. In theory it should work if the LÖVE's version in the App Store is updated to 11.4.  
**Q: Does it work with the LÖVE's Play Store version?**  
A: No. Don't even try it. You will miserably fail to make it work, this version is just too outdated.  
**Q: Does transferring the files by the usual way (through the Windows Explorer) works?**  
A: Yes if you believe you can do it. But keep in mind that this is the most slower way to transfer files and it tends to fail.
## Gameplay
You may need working fingers to play the VN. Scrolling the menus using one of your fingers works just fine. 
* **Tapping with two fingers**: goes back or opens the in-game menu 
* **Tapping with three fingers**: opens the backlog  
* **Pressing with four fingers**: performs fast forward  
## How to use this patch to play the VN
### Playing it on Android
tldr: install the [LÖVE engine's APK](https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk), extract the game file, extract [the patch](https://github.com/Nightdavisao/N7EternalMobile/releases/download/v0.1/patch_foda.zip) over the extracted game, then manage to transfer it to /sdcard/Android/data/org.love2d.android/files/games/lovegame and now you're ready to play by opening the engine app.
* First of all, [you should have the game already downloaded](https://www.mediafire.com/file/nshjldhr3zzm760/n7e.love/file).
* Also, you should make sure your device has enough free space (at least 5 GBs).  
* Download the [SDK platform-tools](https://developer.android.com/studio/releases/platform-tools) to be able to transfer the whole game to your device. 
* Download the LÖVE engine's APK [here](https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk) and install it in your device.
1. Create an folder somewhere in your computer called `games`, then create another folder named `lovegame` inside this folder.
2. Extract the game's .love file to the "lovegame" folder using some extract tool (such as WinRAR, 7zip), you can extract it through the "Open with..." option when you right click the file or opening the extract tool and navigating to the file's location, but notice that all the extracted files should be inside this folder.
3. Download the pre-patched game files [here](https://github.com/Nightdavisao/N7EternalMobile/releases/download/v0.1/patch_foda.zip) and extract over the "lovegame" folder, overwriting the already existing files.
4. Now we just need to transfer the whole stuff. Extract the downloaded SDK platform-tools somewhere then open a command prompt (aka cmd) by using Windows+R and typing `cmd` then pressing enter.
6. Connect your device with a USB cable.
7. Enable [USB debugging](https://developer.android.com/studio/debug/dev-options).
8. When the command prompt window show up, type `cd` with a space right after `cd`, then drag the `platform-tools` folder to the cmd and then drop it. You should see a location pointing to this folder, just press enter.
9. Type `adb.exe devices`, press enter and check if your device is listed there, if it's not, perhaps you're having driver issues or a bad USB cable and you should google the problem if it's the former. The instant you enter this command a prompt will show up in your device (unlock the device if you don't see it) asking if you want to allow USB debugging, just allow it.
10. Type the following command: `adb.exe push (the location pointing to the 'games' folder) /sdcard/Android/data/org.love2d.android/files/`, you can just drag'n'drop the `games` folder like you did before for the `cd` command, after all that, press enter and wait for the transfer get done.
11. Now you can just open the game by opening the game's engine app ("LÖVE for Android").
