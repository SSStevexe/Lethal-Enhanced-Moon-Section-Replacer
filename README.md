# Lethal Enhanced Moon Section Replacer

## What is this tool?

This tool will replace specific sections of the moon configuration file with data from the provided JSON files. The moon configuration file is located in the `Json Files` folder and contains all the moon data for the game.
The files contain their own list of risk from D to S++ and the associated enemies for each moon. The tool will replace the enemies for each moon based on the risk level provided in the JSON files.

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
Loading Json Data...

Loaded data from ->scrap.json<- successfully! ✅

Loaded data from ->outside.json<- successfully! ✅

Loaded data from ->inside.json<- successfully! ✅

Loaded data from ->daytime.json<- successfully! ✅

Loaded data from ->main.json<- successfully! ✅

Loaded data from ->moon_extra_info.json<- successfully! ✅

No new moons detected in main.json. Moon extra info data in moon_extra_info.json is up to date! ✅

List of available moon names (alphabetical):

Moon                      Risk Level

Acidir                    S    
Adamance                  B    
Affliction                C    
Aquatis                   D    
Argent                    A+   
Artifice                  S++  
Assurance                 D    
Asteroid                  B    
Atlantica                 B    
AtlasAbyss                B+   
Auralis                   S++  
Azure                     C    
BlackMesa                 S+   
Bozoros                   A-   
Budapest                  A    
CaltPrime                 S    
CaltPrime                 S    
Celest                    B    
Celestria                 S+   
Cosmocos                  Unknown
Crest                     S+   
Crystallum                D+   
Desolation                A    
Dine                      S    
Echelon                   B    
Echelon                   B    
EchoReach                 C+   
Embrion                   S    
Etern                     S+   
EveM                      B    
Experimentation           B    
FissionC                  A    
Fray                      A+   
Gloom                     B    
Gordion                   Company
Gratar                    A    
Harloth                   S+   
Infernis                  B+   
Junic                     C    
March                     B    
Maritopia                 D    
Nimbus                    B    
Nyx                       D+   
Offense                   B    
Oldred                    S+   
Ooblterra                 S++  
Orion                     S+   
Penumbra                  Unknown
Polarus                   A    
PsychSanctum              A-   
Rend                      A    
Sanguine                  A    
Sector                    Unknown
Sierra                    A-   
Solace                    B    
Spectralis                A+   
StarlancerZero            Unknown
Summit                    S    
Synthesis                 S+   
Titan                     S+   
Tranquillity              A+   
Triskelion                B+   
Vow                       C    
Xen                       S    
Zenit                     B    



Select which section of moons to replace by their associated risk: ['outside', 'inside', 'daytime', 'all', 'skip']all
Moon                      Section                   Risk Level                               Moon Count Replaced/Total                    

134 Oldred                inside_enemies            S+                                       1/65                                         
134 Oldred                outside_enemies           S+                                       1/65                                         
134 Oldred                daytime_enemies           S+                                       1/65                                         
147 Gratar                inside_enemies            A                                        2/65                                         
147 Gratar                outside_enemies           A                                        2/65                                         
147 Gratar                daytime_enemies           A                                        2/65                                         
153 Maritopia             inside_enemies            D                                        3/65                                         
153 Maritopia             outside_enemies           D                                        3/65                                         
153 Maritopia             daytime_enemies           D                                        3/65                                         
154 Etern                 inside_enemies            S+                                       4/65                                         
154 Etern                 outside_enemies           S+                                       4/65                                         
154 Etern                 daytime_enemies           S+                                       4/65                                         
21 Offense                inside_enemies            B                                        5/65                                         
21 Offense                outside_enemies           B                                        5/65                                         
21 Offense                daytime_enemies           B                                        5/65                                         
220 Assurance             inside_enemies            D                                        6/65                                         
220 Assurance             outside_enemies           D                                        6/65                                         
220 Assurance             daytime_enemies           D                                        6/65                                         
25 Fission-C              inside_enemies            A                                        7/65                                         
25 Fission-C              outside_enemies           A                                        7/65                                         
25 Fission-C              daytime_enemies           A                                        7/65                                         
27 Triskelion             inside_enemies            B+                                       8/65                                         
27 Triskelion             outside_enemies           B+                                       8/65                                         
27 Triskelion             daytime_enemies           B+                                       8/65                                         
28 Celest                 inside_enemies            B                                        9/65                                         
28 Celest                 outside_enemies           B                                        9/65                                         
28 Celest                 daytime_enemies           B                                        9/65                                         
33 EchoReach              inside_enemies            C+                                       10/65                                        
33 EchoReach              outside_enemies           C+                                       10/65                                        
33 EchoReach              daytime_enemies           C+                                       10/65                                        
36 Gloom                  inside_enemies            B                                        11/65                                        
36 Gloom                  outside_enemies           B                                        11/65                                        
36 Gloom                  daytime_enemies           B                                        11/65                                        
37 Zenit                  inside_enemies            B                                        12/65                                        
37 Zenit                  outside_enemies           B                                        12/65                                        
37 Zenit                  daytime_enemies           B                                        12/65                                        
41 Experimentation        inside_enemies            B                                        13/65                                        
41 Experimentation        outside_enemies           B                                        13/65                                        
41 Experimentation        daytime_enemies           B                                        13/65                                        
42 Auralis                inside_enemies            S++                                      14/65                                        
42 Auralis                outside_enemies           S++                                      14/65                                        
42 Auralis                daytime_enemies           S++                                      14/65                                        
42 Cosmocos               inside_enemies            Unknown                                  15/65                                        
42 Cosmocos               outside_enemies           Unknown                                  15/65                                        
42 Cosmocos               daytime_enemies           Unknown                                  15/65                                        
44 Atlantica              inside_enemies            B                                        16/65                                        
44 Atlantica              outside_enemies           B                                        16/65                                        
44 Atlantica              daytime_enemies           B                                        16/65                                        
46 Infernis               inside_enemies            B+                                       17/65                                        
46 Infernis               outside_enemies           B+                                       17/65                                        
46 Infernis               daytime_enemies           B+                                       17/65                                        
48 Desolation             inside_enemies            A                                        18/65                                        
48 Desolation             outside_enemies           A                                        18/65                                        
48 Desolation             daytime_enemies           A                                        18/65                                        
56 Vow                    inside_enemies            C                                        19/65                                        
56 Vow                    outside_enemies           C                                        19/65                                        
56 Vow                    daytime_enemies           C                                        19/65                                        
57 Asteroid-13            inside_enemies            B                                        20/65                                        
57 Asteroid-13            outside_enemies           B                                        20/65                                        
57 Asteroid-13            daytime_enemies           B                                        20/65                                        
61 March                  inside_enemies            B                                        21/65                                        
61 March                  outside_enemies           B                                        21/65                                        
61 March                  daytime_enemies           B                                        21/65                                        
7 Dine                    inside_enemies            S                                        22/65                                        
7 Dine                    outside_enemies           S                                        22/65                                        
7 Dine                    daytime_enemies           S                                        22/65                                        
71 Gordion                Company - Skipped ❌
74 Solace                 inside_enemies            B                                        23/65                                        
74 Solace                 outside_enemies           B                                        23/65                                        
74 Solace                 daytime_enemies           B                                        23/65                                        
76 Acidir                 inside_enemies            S                                        24/65                                        
76 Acidir                 outside_enemies           S                                        24/65                                        
76 Acidir                 daytime_enemies           S                                        24/65                                        
8 Titan                   inside_enemies            S+                                       25/65                                        
8 Titan                   outside_enemies           S+                                       25/65                                        
8 Titan                   daytime_enemies           S+                                       25/65                                        
84 Junic                  inside_enemies            C                                        26/65                                        
84 Junic                  outside_enemies           C                                        26/65                                        
84 Junic                  daytime_enemies           C                                        26/65                                        
85 Rend                   inside_enemies            A                                        27/65                                        
85 Rend                   outside_enemies           A                                        27/65                                        
85 Rend                   daytime_enemies           A                                        27/65                                        
9 Celestria               inside_enemies            S+                                       28/65                                        
9 Celestria               outside_enemies           S+                                       28/65                                        
9 Celestria               daytime_enemies           S+                                       28/65                                        
93 Harloth                inside_enemies            S+                                       29/65                                        
93 Harloth                outside_enemies           S+                                       29/65                                        
93 Harloth                daytime_enemies           S+                                       29/65                                        
94 Polarus                inside_enemies            A                                        30/65                                        
94 Polarus                outside_enemies           A                                        30/65                                        
94 Polarus                daytime_enemies           A                                        30/65                                        
Atlas Abyss               inside_enemies            B+                                       31/65                                        
Atlas Abyss               outside_enemies           B+                                       31/65                                        
Atlas Abyss               daytime_enemies           B+                                       31/65                                        
111 PsychSanctum          inside_enemies            A-                                       32/65                                        
111 PsychSanctum          outside_enemies           A-                                       32/65                                        
111 PsychSanctum          daytime_enemies           A-                                       32/65                                        
20 Adamance               inside_enemies            B                                        33/65                                        
20 Adamance               outside_enemies           B                                        33/65                                        
20 Adamance               daytime_enemies           B                                        33/65                                        
5 Embrion                 inside_enemies            S                                        34/65                                        
5 Embrion                 outside_enemies           S                                        34/65                                        
5 Embrion                 daytime_enemies           S                                        34/65                                        
68 Artifice               inside_enemies            S++                                      35/65                                        
68 Artifice               outside_enemies           S++                                      35/65                                        
68 Artifice               daytime_enemies           S++                                      35/65                                        
Bozoros                   inside_enemies            A-                                       36/65                                        
Bozoros                   outside_enemies           A-                                       36/65                                        
Bozoros                   daytime_enemies           A-                                       36/65                                        
39 Azure                  inside_enemies            C                                        37/65                                        
39 Azure                  outside_enemies           C                                        37/65                                        
39 Azure                  daytime_enemies           C                                        37/65                                        
Crystallum                inside_enemies            D+                                       38/65                                        
Crystallum                outside_enemies           D+                                       38/65                                        
Crystallum                daytime_enemies           D+                                       38/65                                        
Echelon                   inside_enemies            B                                        39/65                                        
Echelon                   inside_enemies            B                                        39/65                                        
Echelon                   outside_enemies           B                                        39/65                                        
Echelon                   outside_enemies           B                                        39/65                                        
Echelon                   daytime_enemies           B                                        39/65                                        
Echelon                   daytime_enemies           B                                        39/65                                        
Nimbus                    inside_enemies            B                                        40/65                                        
Nimbus                    outside_enemies           B                                        40/65                                        
Nimbus                    daytime_enemies           B                                        40/65                                        
Spectralis                inside_enemies            A+                                       41/65                                        
Spectralis                outside_enemies           A+                                       41/65                                        
Spectralis                daytime_enemies           A+                                       41/65                                        
CaltPrime                 inside_enemies            S                                        42/65                                        
CaltPrime                 inside_enemies            S                                        42/65                                        
CaltPrime                 outside_enemies           S                                        42/65                                        
CaltPrime                 outside_enemies           S                                        42/65                                        
CaltPrime                 daytime_enemies           S                                        42/65                                        
CaltPrime                 daytime_enemies           S                                        42/65                                        
Black Mesa                inside_enemies            S+                                       43/65                                        
Black Mesa                outside_enemies           S+                                       43/65                                        
Black Mesa                daytime_enemies           S+                                       43/65                                        
129 Sierra                inside_enemies            A-                                       44/65                                        
129 Sierra                outside_enemies           A-                                       44/65                                        
129 Sierra                daytime_enemies           A-                                       44/65                                        
130 Fray                  inside_enemies            A+                                       45/65                                        
130 Fray                  outside_enemies           A+                                       45/65                                        
130 Fray                  daytime_enemies           A+                                       45/65                                        
32 Argent                 inside_enemies            A+                                       46/65                                        
32 Argent                 outside_enemies           A+                                       46/65                                        
32 Argent                 daytime_enemies           A+                                       46/65                                        
34 Nyx                    inside_enemies            D+                                       47/65                                        
34 Nyx                    outside_enemies           D+                                       47/65                                        
34 Nyx                    daytime_enemies           D+                                       47/65                                        
618 Budapest              inside_enemies            A                                        48/65                                        
618 Budapest              outside_enemies           A                                        48/65                                        
618 Budapest              daytime_enemies           A                                        48/65                                        
Sanguine                  inside_enemies            A                                        49/65                                        
Sanguine                  outside_enemies           A                                        49/65                                        
Sanguine                  daytime_enemies           A                                        49/65                                        
38 Crest                  inside_enemies            S+                                       50/65                                        
38 Crest                  outside_enemies           S+                                       50/65                                        
38 Crest                  daytime_enemies           S+                                       50/65                                        
StarlancerZero            inside_enemies            Unknown                                  51/65                                        
StarlancerZero            outside_enemies           Unknown                                  51/65                                        
StarlancerZero            daytime_enemies           Unknown                                  51/65                                        
30 Echelon                inside_enemies            B                                        52/65                                        
30 Echelon                outside_enemies           B                                        52/65                                        
30 Echelon                daytime_enemies           B                                        52/65                                        
35 CaltPrime              inside_enemies            S                                        53/65                                        
35 CaltPrime              outside_enemies           S                                        53/65                                        
35 CaltPrime              daytime_enemies           S                                        53/65                                        
Xen                       inside_enemies            S                                        54/65                                        
Xen                       outside_enemies           S                                        54/65                                        
Xen                       daytime_enemies           S                                        54/65                                        
86 Synthesis              inside_enemies            S+                                       55/65                                        
86 Synthesis              outside_enemies           S+                                       55/65                                        
86 Synthesis              daytime_enemies           S+                                       55/65                                        
127 Eve-M                 inside_enemies            B                                        56/65                                        
127 Eve-M                 outside_enemies           B                                        56/65                                        
127 Eve-M                 daytime_enemies           B                                        56/65                                        
290 Summit                inside_enemies            S                                        57/65                                        
290 Summit                outside_enemies           S                                        57/65                                        
290 Summit                daytime_enemies           S                                        57/65                                        
59 Affliction             inside_enemies            C                                        58/65                                        
59 Affliction             outside_enemies           C                                        58/65                                        
59 Affliction             daytime_enemies           C                                        58/65                                        
71 Sector-0               inside_enemies            Unknown                                  59/65                                        
71 Sector-0               outside_enemies           Unknown                                  59/65                                        
71 Sector-0               daytime_enemies           Unknown                                  59/65                                        
813 Penumbra              inside_enemies            Unknown                                  60/65                                        
813 Penumbra              outside_enemies           Unknown                                  60/65                                        
813 Penumbra              daytime_enemies           Unknown                                  60/65                                        
523 Ooblterra             inside_enemies            S++                                      61/65                                        
523 Ooblterra             outside_enemies           S++                                      61/65                                        
523 Ooblterra             daytime_enemies           S++                                      61/65                                        
112 Aquatis               inside_enemies            D                                        62/65                                        
112 Aquatis               outside_enemies           D                                        62/65                                        
112 Aquatis               daytime_enemies           D                                        62/65                                        
43 Orion                  inside_enemies            S+                                       63/65                                        
43 Orion                  outside_enemies           S+                                       63/65                                        
43 Orion                  daytime_enemies           S+                                       63/65                                        
42 Tranquillity           inside_enemies            A+                                       64/65                                        
42 Tranquillity           outside_enemies           A+                                       64/65                                        
42 Tranquillity           daytime_enemies           A+                                       64/65                                        
Would you like to update the scrap section for all moons? (y/n): y
Moon                      Section                   Risk Level                               Moon Count Replaced/Total                    

134 Oldred                loot_table                S+                                       1/65                                         
147 Gratar                loot_table                A                                        2/65                                         
153 Maritopia             loot_table                D                                        3/65                                         
154 Etern                 loot_table                S+                                       4/65                                         
21 Offense                loot_table                B                                        5/65                                         
220 Assurance             loot_table                D                                        6/65                                         
25 Fission-C              loot_table                A                                        7/65                                         
27 Triskelion             loot_table                B+                                       8/65                                         
28 Celest                 loot_table                B                                        9/65                                         
33 EchoReach              loot_table                C+                                       10/65                                        
36 Gloom                  loot_table                B                                        11/65                                        
37 Zenit                  loot_table                B                                        12/65                                        
41 Experimentation        loot_table                B                                        13/65                                        
42 Auralis                loot_table                S++                                      14/65                                        
42 Cosmocos               loot_table                Unknown                                  15/65                                        
44 Atlantica              loot_table                B                                        16/65                                        
46 Infernis               loot_table                B+                                       17/65                                        
48 Desolation             loot_table                A                                        18/65                                        
56 Vow                    loot_table                C                                        19/65                                        
57 Asteroid-13            loot_table                B                                        20/65                                        
61 March                  loot_table                B                                        21/65                                        
7 Dine                    loot_table                S                                        22/65                                        
71 Gordion                loot_table                Company                                  23/65                                        
74 Solace                 loot_table                B                                        24/65                                        
76 Acidir                 loot_table                S                                        25/65                                        
8 Titan                   loot_table                S+                                       26/65                                        
84 Junic                  loot_table                C                                        27/65                                        
85 Rend                   loot_table                A                                        28/65                                        
9 Celestria               loot_table                S+                                       29/65                                        
93 Harloth                loot_table                S+                                       30/65                                        
94 Polarus                loot_table                A                                        31/65                                        
Atlas Abyss               loot_table                B+                                       32/65                                        
111 PsychSanctum          loot_table                A-                                       33/65                                        
20 Adamance               loot_table                B                                        34/65                                        
5 Embrion                 loot_table                S                                        35/65                                        
68 Artifice               loot_table                S++                                      36/65                                        
Bozoros                   loot_table                A-                                       37/65                                        
39 Azure                  loot_table                C                                        38/65                                        
Crystallum                loot_table                D+                                       39/65                                        
Echelon                   loot_table                B                                        40/65                                        
Echelon                   loot_table                B                                        40/65                                        
Nimbus                    loot_table                B                                        41/65                                        
Spectralis                loot_table                A+                                       42/65                                        
CaltPrime                 loot_table                S                                        43/65                                        
CaltPrime                 loot_table                S                                        43/65                                        
Black Mesa                loot_table                S+                                       44/65                                        
129 Sierra                loot_table                A-                                       45/65                                        
130 Fray                  loot_table                A+                                       46/65                                        
32 Argent                 loot_table                A+                                       47/65                                        
34 Nyx                    loot_table                D+                                       48/65                                        
618 Budapest              loot_table                A                                        49/65                                        
Sanguine                  loot_table                A                                        50/65                                        
38 Crest                  loot_table                S+                                       51/65                                        
StarlancerZero            loot_table                Unknown                                  52/65                                        
30 Echelon                loot_table                B                                        53/65                                        
35 CaltPrime              loot_table                S                                        54/65                                        
Xen                       loot_table                S                                        55/65                                        
86 Synthesis              loot_table                S+                                       56/65                                        
127 Eve-M                 loot_table                B                                        57/65                                        
290 Summit                loot_table                S                                        58/65                                        
59 Affliction             loot_table                C                                        59/65                                        
71 Sector-0               loot_table                Unknown                                  60/65                                        
813 Penumbra              loot_table                Unknown                                  61/65                                        
523 Ooblterra             loot_table                S++                                      62/65                                        
112 Aquatis               loot_table                D                                        63/65                                        
43 Orion                  loot_table                S+                                       64/65                                        
42 Tranquillity           loot_table                A+                                       65/65                                        
Replacement process complete!

Press Enter to exit...
```