# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.4.0] - 2022-01-28
### Changed
- Champion list has been updated to reflect the Neon Nights patch
- Augments have been modified in comps.py to reflect Neon Nights patch
- Team comp is now Yordles in comps.py

### Added
- More items in game_assets
- Auto queue messages

### Fixed
- CHANGELOG

## [2.3.0] - 2022-02-15
### Changed
- Auto queue method changed from WMIC get to lockfile method, this makes it compatible with servers that dont return the app port & auth token from WMIC get.

## [2.2.1] - 2022-01-28
### Fixed
- Potential bugfix for autoqueue crash

## [2.2.0] - 2022-01-28
### Added
- Forfeit functionality, change the time to forfeit in settings.py

## [2.1.1] - 2022-01-28
### Fixed
- Items not placing properly after the first game

## [2.1.0] - 2022-01-28
### Added
- Click location offset randomization

### Fixed
- Tacticians Crown check causing crashses when string is None

## [2.0.0] - 2022-01-27
### Added
- Transparent overlay window
- Change gold spending based on health
- Queue to communicate between the game process and GUI
- pywin32 to requirements.txt

### Changed
- Screen coordinates now have a naming convention, _pos for bbox & _loc for click locations

### Fixed
- Tacticians Crown check now checks against the proper string

### Removed
- Printing to the console from in game
- PyAutoGUI from requirements.txt

## [1.2.0] - 2022-01-26
### Added
- Health check

## [1.1.0] - 2022-01-19
### Changed
- README
- Screen coords now use (x, y, x+w, y+h) instead of (x, y, w, h)
- Moved bench occupied check to arena functions
- Reformatted imports 
- All screenshot functions now use ImageGrab.grab instead of pyautogui.screenshot
- Added function annotation to various functions

### Removed
- PyAutoGUI

## [1.0.0] - 2022-01-06
### Added
- Files
- README
- LICENSE

[2.3.0]: https://github.com/jfd02/TFT-OCR-BOT/tree/d6bdd20823d92cd84343eb007d5ef146d0abb2f9
[2.2.1]: https://github.com/jfd02/TFT-OCR-BOT/tree/b801ba52a9da65a3d954c7a486bc581901c7af9c
[2.2.0]: https://github.com/jfd02/TFT-OCR-BOT/tree/4eb5a19b976cd11dcbb05dd6af5a60207bfa7ed1
[2.1.1]: https://github.com/jfd02/TFT-OCR-BOT/tree/c4c08d692ac99cff3a3d6843a20fb10055743a46
[2.1.0]: https://github.com/jfd02/TFT-OCR-BOT/tree/d6311dfe21889ac3851d488af82b75a18393aafc
[2.0.0]: https://github.com/jfd02/TFT-OCR-BOT/tree/9fd022e47e029694e3dd816671181a09a26c5b5e
[1.2.0]: https://github.com/jfd02/TFT-OCR-BOT/tree/54eea1991fcbd338eb720a69fad3193e1b393824
[1.1.0]: https://github.com/jfd02/TFT-OCR-BOT/tree/af6258fb3aaa5e3807fce2375338c4af328472d1
[1.0.0]: https://github.com/jfd02/TFT-OCR-BOT/tree/6b7ce114ef35c45d4fc8328bed5520ed04a39592
