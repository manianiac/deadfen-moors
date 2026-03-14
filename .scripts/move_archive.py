import os
import shutil

archive_dir = "/Users/wbarron/Documents/LARPA TTRPG/Archive"
base_dir = "/Users/wbarron/Documents/LARPA TTRPG/The Deadfen Moors"

moves = {
    "Aenor.md": "Characters/Aenor.md",
    "Alaric.md": "Characters/Alaric.md",
    "Clovis.md": "Characters/Clovis.md",
    "Lothar.md": "Characters/Lothar.md",
    "Caelen.md": "Characters/Caelen.md",
    "Beric.md": "Characters/Beric.md",
    "Sir Galen.md": "Characters/Sir Galen.md",
    "Drust.md": "Characters/Drust.md",
    "Vortigern.md": "Characters/Vortigern.md",
    "Azag.md": "Characters/Azag.md",
    "Namtar.md": "Characters/Namtar.md",
    "Silas the Pallid.md": "Characters/Silas the Pallid.md",
    "The Flesh-Weaver.md": "Characters/The Flesh-Weaver.md",

    "The Silver Luminaries.md": "Lore/Religions/The Silver Luminaries.md",
    "The Withered Path.md": "Lore/Religions/The Withered Path.md",
    "The Hearth of the First Queen.md": "Lore/Religions/The Hearth of the First Queen.md",
    "The Ascendant Sky.md": "Lore/Religions/The Ascendant Sky.md",
    "The Twin Vanguard.md": "Lore/Religions/The Twin Vanguard.md",
    "The Anchorite Brotherhood.md": "Lore/Religions/The Anchorite Brotherhood.md",
    "The Cult of the Chimera.md": "Lore/Religions/The Cult of the Chimera.md",
    "The Children of Ash.md": "Lore/Religions/The Children of Ash.md",

    "Clan Zabar.md": "Lore/Dwarves/Clan Zabar.md",
    "Clan Kurgal.md": "Lore/Dwarves/Clan Kurgal.md",
    "Clan Gundinul.md": "Lore/Dwarves/Clan Gundinul.md",
    "Clan Lugal-Ur.md": "Lore/Dwarves/Clan Lugal-Ur.md",

    "The Elysian Dale.md": "Lore/Halflings/The Elysian Dale.md",
    "The Asphodel Thicket.md": "Lore/Halflings/The Asphodel Thicket.md",

    "Elves.md": "Lore/Elves/Elves.md",
    "City of the Ancient Heart.md": "Lore/Elves/City of the Ancient Heart.md",
    "The Ruin of Anu.md": "Lore/Elves/The Ruin of Anu.md",

    "The Iron-Dogs.md": "Lore/Factions/The Iron-Dogs.md",
    "The Copper-Grubbers.md": "Lore/Factions/The Copper-Grubbers.md",

    "Ash-Rats.md": "Lore/Abominations/Ash-Rats.md",  # Or creatures? Let's put in Abominations since it exists
    "Scrubbers.md": "Lore/Precursors/Scrubbers.md", # Precursors? Scrubbers are Precursor drones... Let's just put all in Lore/Creatures for now, actually let's use Lore/Factions and Lore/Creatures. Wait, Abominations.md is a file, not a directory.
    # Ah, I tried to list Lore/Abominations and it didn't exist. Let's create `Lore/Creatures` and `Lore/Factions`.
}

# Fix for Scrubbers and Ash-Rats
moves["Ash-Rats.md"] = "Lore/Creatures/Ash-Rats.md"
moves["Scrubbers.md"] = "Lore/Creatures/Scrubbers.md"
moves["Player Primer.md"] = "Player Primer.md"
moves["Rumors.md"] = "Rumors.md"

for src_name, dst_rel in moves.items():
    src_path = os.path.join(archive_dir, src_name)
    dst_path = os.path.join(base_dir, dst_rel)
    
    if os.path.exists(src_path):
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.move(src_path, dst_path)
        print(f"Moved {src_name} to {dst_rel}")
    else:
        print(f"Warning: {src_name} not found in {archive_dir}")

