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
     
     
Enter the name of the moon you want to replace data for: >? vow
Valid moon name entered. Now targeting moon: vow

Enter the name of the section you want to replace data for (scrap, outside, inside, daytime): >? outside
Section ->outside_enemies<- for moon ->vow<- has been replaced successfully with data from ->outside.json<-

Press Enter to exit...
```