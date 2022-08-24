# Never7 Eternal Edition for mobile devices
A patch to make the game playable in mobile devices (specifically Android).
## What's working
* Opening the game (couldn't open before without removing some pixel shader that for some reason doesn't work)
* Playing the game (couldn't play before because scaling problems)
* Unlocked aspect ratio (the game will be draw in a safe area where it isn't obstructed by the phone's screen notch or the system UI)
* Opening the pause menu and backlog in-game
* Scrolling in backlog, playing log and the shortcut menu ("flow menu")
* Fast-forwarding (but for now it's too uncomfortable to do so, though)
## Notes
* The game is automatically saved when it loses its focus (when it's running in background or when you open the system's notification panel) and there's no option to disable the auto saving for now
## TODO
* GUI elements for instant skip and fast forwarding
* maybe more... 
## Gameplay
Playing the game with this patch requires having more than one finger in your hands.  
* **Tapping with two fingers**: goes back or opens the in-game menu 
* **Tapping with three fingers**: opens the backlog  
* **Tapping with four fingers**: performs fast forward 
## How to use this patch to play the VN
### Playing it on Android
tldr: install the [LÖVE engine's APK](https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk), extract the game file, extract [the patch](https://github.com/Nightdavisao/N7EternalMobile/releases/download/v0.1/patch_foda.zip) over the extracted game, then manage to transfer it to /sdcard/Android/data/org.love2d.android/files/games/lovegame and now you're ready to play by opening the engine app
* First of all, [you should have the game already downloaded](https://www.mediafire.com/file/nshjldhr3zzm760/n7e.love/file).
* Also, you should make sure your device has enough free space (at least 5 GBs).  
* Download the [SDK platform-tools](https://developer.android.com/studio/releases/platform-tools) to be able to transfer the whole game to your device. 
* Download the LOVE engine's APK [here](https://github.com/love2d/love/releases/download/11.4/love-11.4-android.apk) and install it in your device.
1. Create an folder somewhere in your computer called "games", then create another folder called "lovegame" inside this folder.
2. Extract the game's .love file to the "lovegame" folder using some extract tool (such as WinRAR, 7zip), you can extract it through the "Open with..." option when you right click the file or opening the extract tool and navigating to the file's location, but notice that all the extracted files should be inside this folder.
3. Download the pre-patched game files [here](https://github.com/Nightdavisao/N7EternalMobile/releases/download/v0.1/patch_foda.zip) and extract over the "lovegame" folder, overwriting the already existing files.
4. Now we just need to transfer the whole stuff. Extract the downloaded SDK platform-tools somewhere then open a command prompt (aka cmd) by using Windows+R and typing "cmd" then pressing enter.
6. Connect your device with a USB cable.
7. When the command prompt window show up, type "cd" with a space right after "cd", then drag the "platform-tools" folder to the cmd and then drop it. You should see a location pointing to this folder, just press enter.
8. Type "adb.exe devices", press enter and check if your device is listed there, if it's not, perhaps you're having driver issues or a bad USB cable and you should google the problem if it's the former.
9. Type the following command: "adb.exe push (the location pointing to the 'games' folder) /sdcard/Android/data/org.love2d.android/files/", you can just drag'n'drop the "games" folder like you did before for the "cd" command, after all that, press enter and wait for the transfer get done.
10. Now you can just open the game by opening the game's engine app ("LÖVE for Android").
