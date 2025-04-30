# SatellaText-Plus
Teletext service for the SatellaView+ project

## About this project
**SatellaText** is a free-to-access internet teletext service that is intended to serve as a companion to the Satellaview+ project.
This service ~~sucks~~ is a work-in-progress, with multiple contributors working to bring you a service that will, when finished,
feature roughly around 40+ pages of information, including:
- Broadcast schedules for Satellaview+ and its sister internet radio channel, SoundLink+;
- News about the service
- Info about your favourite SV+ titles
- And more... <sub>nah jk</sub>

## What is Satellaview+?
**Satellaview+** is a free-to-access closed-source project that aims to revive the Satellaview, a Japan-only SNES accessory, or more
specifically, BS-X, Nintendo's short-lived service for Satellaview, that allowed subscribers to download games, magazines, and more
via satellite broadcasts. BS-X was a collaboration between Nintendo and Japanese satellite radio broadcaster St.GIGA.
The BS-X service (among other Satellaview services) was ended on 30 June 2000.

## How to use SatellaText
- You will need to use [VBIT2](https://github.com/peterkvt80/vbit2) in order to get the teletext pages working. There are several
  ways to do this, but I recommend **loosely** following [this guide](https://zxnet.co.uk/teletext/emulators/) from ZXGuesser.
- Note that instead of Subversion, you will need git. Just do `git clone` on this repo into the same folder as VBIT.
- To update the pages, just run `git pull`. Maybe set a cron job or task schedule for this.
- You can use VBIT on a Raspberry Pi (excl. Models 5, Zero and Zero 2) to view the pages on a teletext TV if you can be asked.
- If using Windows, I would recommend BeebEm to view the pages. The guide above shows instructions for this. I would ideally
  set the packet server to Channel 4 so you can use the other channels for other services like NMS.
- If using Linux, Fuse would be ideal. Again, read the goddamn guide.

# Happy teletexting!
-- Kami-kun and everyone else at Satellaview+
