# Lethal Enhanced Moon Section Replacer

## What is this tool?

This is a tool that will replace specific moon sections of the main configuration file in Lethal Enhanced.

These specific sections are supported for this release:
 - Scrap - This will target the `loot_table` section of the moon configuration file and replace with contents from `scrap.json`.


 - Outside - This will target the `outside_enemies` section of the moon configuration file and replace with contents from `outside.json`.


 - Inside - This will target the `inside_enemies` section of the moon configuration file and replace with contents from `inside.json`.


 - Daytime - This will target the `daytime_enemies` section of the moon configuration file and replace with contents from `daytime.json`.

## How to use?

1. Download the latest release from the Master branch.
2. Place the tool in the same directory as the moon configuration file folder `Json Files`.
3. Run the tool using the command: `py moon_section_replacer.py` or use the next section's command arguments.

OR

1. Download and use the precompiled PyInstaller version from the releases, which is a standalone executable.

## Features
- Replace specific moon sections with data from the provided JSON files.
- Multiple moons are supported in a single run.

## Command used with PyInstaller
`pyinstaller --onefile --name Lethal_Enhanced_Text_Replacer --icon=.\PyInstaller/discord-avatar-512-1VMJP.ico --upx-dir="C:\Program Files\upx-4.2.4-win64" .\moon_section_replacer.py`

## Example Run

```text
No new moons detected. Moon extra info data in moon_extra_info.json is up to date!

List of available moon names (alphabetical):

Moon                      Risk Level

Acidir                    A    
Adamance                  B    
Aerona                    Unknown
Argent                    A+   
Artifice                  S++  
Assurance                 D    
Asteroid                  B    
Atlantica                 Wesley
AtlasAbyss                B+   
Auralis                   S++  
Azure                     C    
BlackMesa                 S+   
Bozoros                   A-   
Budapest                  A    
CaltPrime                 S    
Celest                    B    
Celestria                 S+   
Cosmocos                  Wesley
Crest                     S+   
Crystallum                D+   
Desolation                Wesley
Dine                      S    
Echelon                   B    
EchoReach                 C+   
Embrion                   S    
Etern                     Wesley
Experimentation           B    
FissionC                  Wesley
Fray                      A+   
Gloom                     Wesley
Gordion                   Wesley
Gratar                    Wesley
Harloth                   S+   
Infernis                  Wesley
Junic                     Wesley
March                     B    
Maritopia                 D    
Nimbus                    B    
Nyx                       D+   
Offense                   B    
Oldred                    Wesley
Polarus                   Wesley
PsychSanctum              A-   
Rend                      A    
Sanguine                  A    
Siabudabu                 S+   
Sierra                    A-   
Solace                    B    
Spectralis                A+   
Titan                     S+   
Triskelion                B+   
Vow                       C    
Zenit                     B    


Did you want to replace data for multiple moons? (y/n): 
```