# Lethal Enhanced Moon Section Replacer

## What is this tool?

This tool will replace specific sections of the moon configuration file with data from the provided JSON files. The moon configuration file is located in the `Json Files` folder and contains all the moon data for the game.
The files contain their own list of risk from D to S++ to Unknown, and the associated enemies for each moon: `moon_extra_info.json`. The tool will replace the enemies for each moon based on the risk level provided in the JSON files.

These specific sections are supported for this release:
 - Scrap - This will target the `loot_table` section of the moon configuration file and replace with contents from `scrap.json`.


 - Outside - This will target the `outside_enemies` section of the moon configuration file and replace with contents from `outside.json`.


 - Inside - This will target the `inside_enemies` section of the moon configuration file and replace with contents from `inside.json`.


 - Daytime - This will target the `daytime_enemies` section of the moon configuration file and replace with contents from `daytime.json`.


 - Moon Travel Prices - This will target the `price` section of the moon configuration file and replace with contents from `options_by_risk.json`. More options will be supported here soon.

## How to use?

1. Download the latest release from the Master branch.
2. Place the tool in the same directory as the moon configuration file folder `Json Files`.
3. Run the tool using the command: `py moon_section_replacer.py` or use the next section's command arguments.

OR

1. Download and use the precompiled PyInstaller version from the releases(.zip), which is a standalone executable. This will come with the required `Json Files` folder and the executable.

- Note: Since I use the `--upx-dir` argument, you will need to change the path to the upx directory on your system. Additionally, this option is known to create false positives on anti-virus. Feel free to compile the executable yourself with the command above.
## Features
- Replace specific moon sections with data from the provided JSON files.
- All moons are supported in a single run.
- Detection of new moons in `main.json` and auto updating `moon_extra_info.json` if new moons are detected.
- Error resistance for missing moons, invalid JSON files, missing risk levels, and more.

## Command used with PyInstaller
`pyinstaller --onefile --name Lethal_Enhanced_Text_Replacer --icon=.\PyInstaller/discord-avatar-512-1VMJP.ico --upx-dir="C:\Program Files\upx-4.2.4-win64" .\moon_section_replacer.py`

## Example Run

```text
ConfigSyncer: : Loading Json Data...

ConfigSyncer: : File                 Loaded              
ConfigSyncer: : scrap.json           ✅                   
ConfigSyncer: : outside.json         ✅                   
ConfigSyncer: : inside.json          ✅                   
ConfigSyncer: : daytime.json         ✅                   
ConfigSyncer: : main.json            ✅                   
ConfigSyncer: : moon_extra_info.json ✅                   
ConfigSyncer: : Json Data Loaded ✅

ConfigSyncer: : Syncing moon data...

ConfigSyncer: : No missing moons in moon_extra_info.json. ✅

ConfigSyncer: : No outdated moons in moon_extra_info.json. ✅

ConfigSyncer: : Syncing main.json and scrap.json

ConfigSyncer: : Scrap data synced ✅

Select an action to perform:

1. Modify rarities for scraps or monsters in all moons.
2. Replace a section of moons by risk level
3. Exit script
Enter the number of the action you would like to perform: 2

Select which section of moons to replace by their associated risk: ['outside', 'inside', 'daytime', 'scrap', 'all']
outside
Moon                      Section                   Risk Level                               Moon Count Replaced/Total                    

111 PsychSanctum          OUTSIDE                   A-                                       1/63                                         
112 Aquatis               OUTSIDE                   D                                        2/63                                         
127 Eve-M                 OUTSIDE                   B                                        3/63                                         
129 Sierra                OUTSIDE                   A-                                       4/63                                         
130 Fray                  OUTSIDE                   A+                                       5/63                                         
134 Oldred                OUTSIDE                   S+                                       6/63                                         
147 Gratar                OUTSIDE                   A                                        7/63                                         
153 Maritopia             OUTSIDE                   D                                        8/63                                         
154 Etern                 OUTSIDE                   S+                                       9/63                                         
20 Adamance               OUTSIDE                   B                                        10/63                                        
21 Offense                OUTSIDE                   B                                        11/63                                        
220 Assurance             OUTSIDE                   D                                        12/63                                        
25 Fission-C              OUTSIDE                   A                                        13/63                                        
27 Triskelion             OUTSIDE                   B+                                       14/63                                        
28 Celest                 OUTSIDE                   B                                        15/63                                        
290 Summit                OUTSIDE                   S                                        16/63                                        
30 Echelon                OUTSIDE                   B                                        17/63                                        
32 Argent                 OUTSIDE                   A+                                       18/63                                        
33 EchoReach              OUTSIDE                   C+                                       19/63                                        
34 Nyx                    OUTSIDE                   D+                                       20/63                                        
35 CaltPrime              OUTSIDE                   S                                        21/63                                        
36 Gloom                  OUTSIDE                   B                                        22/63                                        
37 Zenit                  OUTSIDE                   B                                        23/63                                        
38 Crest                  OUTSIDE                   S+                                       24/63                                        
39 Azure                  OUTSIDE                   C                                        25/63                                        
41 Experimentation        OUTSIDE                   B                                        26/63                                        
42 Auralis                OUTSIDE                   S++                                      27/63                                        
42 Cosmocos               OUTSIDE                   Unknown                                  28/63                                        
42 Tranquillity           OUTSIDE                   A+                                       29/63                                        
43 Orion                  OUTSIDE                   S+                                       30/63                                        
44 Atlantica              OUTSIDE                   B                                        31/63                                        
46 Infernis               OUTSIDE                   B+                                       32/63                                        
48 Desolation             OUTSIDE                   A                                        33/63                                        
5 Embrion                 OUTSIDE                   S                                        34/63                                        
523 Ooblterra             OUTSIDE                   S++                                      35/63                                        
56 Vow                    OUTSIDE                   C                                        36/63                                        
57 Asteroid-13            OUTSIDE                   B                                        37/63                                        
59 Affliction             OUTSIDE                   C                                        38/63                                        
61 March                  OUTSIDE                   B                                        39/63                                        
618 Budapest              OUTSIDE                   A                                        40/63                                        
68 Artifice               OUTSIDE                   S++                                      41/63                                        
7 Dine                    OUTSIDE                   S                                        42/63                                        
71 Gordion                Company - Skipped ❌
71 Sector-0               OUTSIDE                   Unknown                                  43/63                                        
74 Solace                 OUTSIDE                   B                                        44/63                                        
76 Acidir                 OUTSIDE                   S                                        45/63                                        
8 Titan                   OUTSIDE                   S+                                       46/63                                        
813 Penumbra              OUTSIDE                   Unknown                                  47/63                                        
84 Junic                  OUTSIDE                   C                                        48/63                                        
85 Rend                   OUTSIDE                   A                                        49/63                                        
86 Synthesis              OUTSIDE                   S+                                       50/63                                        
9 Celestria               OUTSIDE                   S+                                       51/63                                        
93 Harloth                OUTSIDE                   S+                                       52/63                                        
94 Polarus                OUTSIDE                   A                                        53/63                                        
Atlas Abyss               OUTSIDE                   B+                                       54/63                                        
Black Mesa                OUTSIDE                   S+                                       55/63                                        
Bozoros                   OUTSIDE                   A-                                       56/63                                        
Crystallum                OUTSIDE                   D+                                       57/63                                        
Nimbus                    OUTSIDE                   B                                        58/63                                        
Sanguine                  OUTSIDE                   A                                        59/63                                        
Spectralis                OUTSIDE                   A+                                       60/63                                        
StarlancerZero            OUTSIDE                   Unknown                                  61/63                                        
Xen                       OUTSIDE                   S                                        62/63              
main.json updated successfully. ✅
Press enter to exit...
Process finished with exit code 0
```