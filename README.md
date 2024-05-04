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

## Features
- Replace specific moon sections with data from the provided JSON files.
- Mutliple moons are supported in a single run.

## Command arguments ( not yet implemented )

- `--main_file` - The main moon configuration file. Default is `main.json`.
- `--moon` - Which moon to target. These moons are found by looking at the `moon` section of the main configuration file. Ex: `March`, `Experimentation`, etc...
- `--replace` - The section to replace. Options are `scrap`, `outside`, `inside`, and `daytime`.

Example ( args - NOT YET IMPLEMENTED): `py moon_section_replacer.py --main_file main.json --moon march --replace scrap`


Example (no args): `py moon_section_replacer.py`
## Example Run

```text
List of available moon names (alphabetical):

     Acidir
     Adamance
     Argent
     Artifice
     Assurance
     Asteroid
     Atlantica
     AtlasAbyss
     Auralis
     Azure
     BlackMesa
     Bozoros
     CaltPrime
     Celest
     Celestria
     Cosmocos
     Crystallum
     Desolation
     Dine
     Echelon
     EchoReach
     Embrion
     Etern
     Experimentation
     FissionC
     Fray
     Gloom
     Gordion
     Gratar
     Harloth
     Infernis
     Junic
     March
     Maritopia
     Nimbus
     Offense
     Oldred
     Polarus
     PsychSanctum
     Rend
     Sierra
     Solace
     Spectralis
     Titan
     Triskelion
     Vow
     Zenit


Did you want to replace data for multiple moons? (y/n): yes
Enter the names of the moons you want to replace data for one at a time. Type "all" to affect ALL moons!

Moon to include in replacement (type "done!" to end): vow
Moon to include in replacement (type "done!" to end): assurance
Moon to include in replacement (type "done!" to end): march
Moon to include in replacement (type "done!" to end): zenit
Moon to include in replacement (type "done!" to end): all
Moons you have requested to replace data for: ['Acidir', 'Adamance', 'Argent', 'Artifice', 'Assurance', 'Asteroid', 'Atlantica', 'AtlasAbyss', 'Auralis', 'Azure', 'BlackMesa', 'Bozoros', 'CaltPrime', 'Celest', 'Celestria', 'Cosmocos', 'Crystallum', 'Desolation', 'Dine', 'Echelon', 'EchoReach', 'Embrion', 'Etern', 'Experimentation', 'FissionC', 'Fray', 'Gloom', 'Gordion', 'Gratar', 'Harloth', 'Infernis', 'Junic', 'March', 'Maritopia', 'Nimbus', 'Offense', 'Oldred', 'Polarus', 'PsychSanctum', 'Rend', 'Sierra', 'Solace', 'Spectralis', 'Titan', 'Triskelion', 'Vow', 'Zenit']

Enter the name of the section you want to replace data for (scrap, outside, inside, daytime): scrap
Section ->loot_table<- for moon ->Acidir<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Adamance<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Argent<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Artifice<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Assurance<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Asteroid<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Atlantica<- has been replaced successfully with data from ->scrap.json<-


Section ->loot_table<- for moon ->Auralis<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Azure<- has been replaced successfully with data from ->scrap.json<-


Section ->loot_table<- for moon ->Bozoros<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->CaltPrime<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Celest<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Celestria<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Cosmocos<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Crystallum<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Desolation<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Dine<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Echelon<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->EchoReach<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Embrion<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Etern<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Experimentation<- has been replaced successfully with data from ->scrap.json<-


Section ->loot_table<- for moon ->Fray<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Gloom<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Gordion<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Gratar<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Harloth<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Infernis<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Junic<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->March<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Maritopia<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Nimbus<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Offense<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Oldred<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Polarus<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->PsychSanctum<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Rend<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Sierra<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Solace<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Spectralis<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Titan<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Triskelion<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Vow<- has been replaced successfully with data from ->scrap.json<-

Section ->loot_table<- for moon ->Zenit<- has been replaced successfully with data from ->scrap.json<-

Replacement process complete!

Press Enter to exit...
```