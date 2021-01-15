# Access Key Extractor

* ![Auto Release](https://github.com/Lord-Giganticus/access-key-extractor/workflows/Auto%20Release/badge.svg)
* ![Python application](https://github.com/Lord-Giganticus/access-key-extractor/workflows/Python%20application/badge.svg)
* ![CodeQL](https://github.com/Lord-Giganticus/access-key-extractor/workflows/CodeQL/badge.svg)

Extracts server access keys from 3DS and WiiU ROM dumps

## Requirements
- Node 12.x or higher
- Python 3.x
- curl for windows

## Usage

`python extractor.py` (*Note that extractor.py is the only file from releases that must be downloaded. extractor.py checks for the other 3 files and downloads them if they're missing*)

## Extractor.js Arguments

- `node extractor [path]` The path to the game dump (WiiU ROM decompressed ELF or 3DS ROM bin) [Required]
- `node extractor [path] [packet]` A PRUDP packet to test found access keys against. For simplicity, the packet is expected to be of type SYN [Optional]

## Notes

- Encoding defaults to utf16le, which seems to work for all titles. Has not been tested on every title
- Access keys are always 8 lowercase characters a-f0-9, except for the Friends server access key. Because of this, this may return multiple possible keys. You may provide a test packet to attempt to find the exact access key, or try all returned possible keys one by one
- To get the access key for a WiiU title you must first decompress the RPX file in the `code/` folder of the decrypted title into an ELF, then run the extractor on the ELF. See [wiiurpxtool.](https://github.com/0CBH0/wiiurpxtool) I also provided the latest exe in the repo :)
