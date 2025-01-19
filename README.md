# Never7 Eternal Edition (v0.6.1) for Android/Nintendo Switch
A patch to make the game playable on Android/Nintendo Switch  
* [Notes](#notes)
* [Saving](#saving)
* [FAQ](#faq)
* [Gameplay](#gameplay)
* [How to play](#how-to-play)

## Notes
### Switch
* The Switch support is considered to be "experimental" since I can't tell how well it's working because I don't have a Nintendo Switch myself (I had someone else to test it). You probably want to play this on handheld mode because the controller support is partial.
* You should use [love-nx](https://github.com/retronx-team/love-nx).
### Android
* ~~Audio keeps playing if you leave the game open in background.~~ (fixed in LÖVE v11.5)
* Plugging in a headset or headphones while the game is running doesn't switch the audio to the connected device. Instead, it stops all sound. Plug in whatever you want to plug first and then open the game. This seems to be a problem with the engine itself.
## Saving
By default, everything (save states, system save) is saved to `(internal storage)/Android/data/org.love2d.android/files/save/Never7Eternal`. If you can't access this directory, use MiXplorer.
## FAQ
**Q: Does it work on iOS?**  
A: I had compiled an IPA of the engine for someone else to test out the game while I was on hackintosh but they never got back to me so here's your answer: I don't know. But it should work.
## Gameplay
You can fast forward, instant skip and open the backlog with the GUI controls. Scrolling the menus using one of your fingers works just fine. 
* Tapping with two fingers goes back or opens the in-game menu
* Double tap the "Skip" text for instant skip, hold it for fast forwarding
## How to play
Download the already pre-patched game here: [link soon]  
If you're on Android, download the LÖVE APK on their [official website](https://love2d.org/) and then load the game through LÖVE Loader, which will appear in your app drawer once you install the APK.