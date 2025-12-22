# Never7 Eternal Edition (v0.6.1) for Android/Nintendo Switch
A patch to make the game playable on Android/Nintendo Switch  
* [Notes](#notes)
* [Saving](#saving)
* [FAQ](#faq)
* [Gameplay](#gameplay)
* [How to play](#how-to-play)

## Notes
### Switch
* The Switch support is considered to be "experimental" since I can't tell how well it's working because I don't have a Nintendo Switch myself (I had someone else to test it). You probably want to play this on handheld mode (at least to get past the title screen by touching on the screen).
### Android
* ~~Audio keeps playing if you leave the game open in background.~~ (fixed in LÖVE v11.5)
* Plugging in a headset or headphones while the game is running doesn't switch the audio to the connected device. Instead, it stops all sound. Plug in whatever you want to plug first and then open the game. This seems to be a problem with the engine itself.
## Saving
By default, everything (save states, system save) is saved to `(internal storage)/Android/data/org.love2d.android/files/save/Never7Eternal`. If you can't access this directory, use MiXplorer.
## Gameplay
### Touch
You can fast forward, instant skip and open the backlog with the GUI controls. Scrolling the menus using one of your fingers works just fine. 
* Tapping with two fingers goes back or opens the in-game menu
* Double tap the "Skip" text for instant skip, hold it for fast forwarding
### Controller
This mod has a limited support for controllers *(you can even use this mod just for this functionality if you're on PC)*.  
Below are the instructions for the Xbox layout, but it works for every controller that SDL supports *(you just have to follow the face button layout)*.  

**Xbox controller users:** A/B buttons are swapped by default if you're on a Nintendo Switch. They shouldn't be swapped if you're on anything else, but you can swap them in the in-game menu if you want to.

* B - hides the textbox (if it's visible) or goes back
* A - advances the text, confirms choices
* X - opens the in-game menu
* Y - opens the backlog
* L - fast forward
* R - enables auto mode

You can use the right stick to scroll the backlog and the left stick to scroll the menus. 
## How to play
Download the already pre-patched game [here](https://mega.nz/file/UpMQiJzA). 
The decryption key is in the [releases page](https://github.com/Nightdavisao/N7EternalMobile/releases).  
### Android
Download the LÖVE APK on their [official website](https://love2d.org/) and then load the game through LÖVE Loader, which will appear in your app drawer once you install the APK.
### iOS
#### Pre-built IPA
Download the pre-built IPA [here](https://mega.nz/file/vZ1BzJKS#CDYfPNZgZs08E5uNxc4DMLIiG-m8EpjY-jeerXTyo0Q) (v0.6.1) and sideload that using Sideloadly (or any other solution).  
#### Manually loading the game with LÖVE's compiled IPA
1. Sideload the [LÖVE IPA](/assets/love2d.ipa) with Sideloadly (or any other solution)  
2. Add the `.love` file to the documents for the LÖVE app through iTunes (See [this section](https://support.apple.com/en-gb/120403) on Apple's website).
3. Open the LÖVE app and load the game.

Thanks to [pichuis](https://github.com/lewismcyoutube) for helping to test this on iOS!
### Switch
Switch support has been tested with love-nx. From [love-nx](https://github.com/retronx-team/love-nx)'s README:
> Put a LÖVE archive named game.love in the same folder as the NRO file of the latest release. Additionally, you can directly drop the contents of the archive in the folder, as long as it contains a main.lua file.
Download love-nx's NRO [here](https://github.com/retronx-team/love-nx/releases).