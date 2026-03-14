import os

output_dir = "/Users/wbarron/Documents/LARPA TTRPG/Archive"
os.makedirs(output_dir, exist_ok=True)

files = {}

# God-Kings
files["Aenor.md"] = """---
aliases: [The Queen]
tags: [character, human, god-king]
---
# Aenor

One of the early, benevolent [[God-Kings|God-Queens]] whose divine bloodline served as a shield for early humanity. She is remembered as the Mother of the modern kingdoms.

- **Religion:** [[The Hearth of the First Queen]]
- **Associated Locations**:
  - [[D.6]] Tomb of Queen Aenor
"""

files["Alaric.md"] = """---
aliases: [The Withered King]
tags: [character, human, god-king]
---
# Alaric

A fallen [[God-Kings|God-King]] cursed to decay by divine mandate. He is remembered in the modern era as a tragic but necessary figure of the natural cycle.

- **Religion:** [[The Withered Path]]
- **Associated Locations**:
  - [[L.10]] King Alaric the Withered
"""

files["Clovis.md"] = """---
aliases: [The Lonely King]
tags: [character, human, god-king]
---
# Clovis

The last [[God-Kings|God-King]] of his specific bloodline, who viewed his isolation as a divine withdrawal from a collapsing world.

- **Religion:** [[The Anchorite Brotherhood]]
- **Associated Locations**:
  - [[G.13]] Den of King Clovis the Lonely
"""

files["Lothar.md"] = """---
aliases: [The Floating King]
tags: [character, human, god-king]
---
# Lothar

A tyrant [[God-Kings|God-King]] from the fading era who wielded the "Divine Levitation"—the ancient, magical right to rule from the sky.

- **Religion:** [[The Ascendant Sky]]
- **Associated Locations**:
  - [[O.5]] King Lothar the Floating
"""

files["Caelen.md"] = """---
aliases: [The Hero]
tags: [character, inhuman, god-king]
---
# Caelen

An Inhuman champion forged in a divine crucible specifically to hunt [[Abominations]]. Remembered as a noble, disciplined warrior whose strongholds still stand.

- **Religion:** [[The Twin Vanguard]]
- **Associated Locations**:
  - [[A.6]] Caelen’s Meadow
  - [[H.12]] Caelen’s Tangle
  - [[L.11]] Keep of Caelen
"""

files["Beric.md"] = """---
aliases: [The Thorny Hero]
tags: [character, inhuman, god-king]
---
# Beric

An Inhuman champion forged in a divine crucible to fight [[Abominations]]. Unlike Caelen, Beric was a heavily mutated, spiky brute who harnessed primal fury to fight fire with fire.

- **Religion:** [[The Twin Vanguard]]
- **Associated Locations**:
  - [[G.12]] Beric the Thorny
"""

files["Sir Galen.md"] = """---
aliases: [The Bright Knight, The Silver Knight]
tags: [character, human, god-king]
---
# Sir Galen

A [[God-Kings|God-King]] era paladin who wielded flawless, un-tarnished magical artifacts (often referred to as "Silver" or "Bright" by modern humans).

- **Religion:** [[The Silver Luminaries]]
- **Associated Locations**:
  - [[C.4]] Field of Sir Galen the Bright
  - [[K.10]] Sir Galen the Silver
"""

files["Drust.md"] = """---
aliases: [The Chimera, The Flesh-Shaper]
tags: [character, inhuman, god-king]
---
# Drust

An Inhuman [[God-Kings|God-King]] who believed humanity's static form was too weak to survive. He spliced the chaotic, magical essence of the [[Abominations]] into his own followers, viewing the human body as an unfinished canvas. 

- **Religion:** [[The Cult of the Chimera]]
- **Associated Locations**:
  - *(Add locations here)*
"""

files["Vortigern.md"] = """---
aliases: [The Scorched King]
tags: [character, inhuman, god-king]
---
# Vortigern

An immensely powerful [[God-Kings|God-King]] whose internal divine spark catastrophically ruptured. He became a walking cataclysm of holy fire and destructive energy, burning his own cities to the ground in his madness. 

- **Religion:** [[The Children of Ash]]
- **Associated Locations**:
  - *(Add locations here)*
"""

# Religions
files["The Silver Luminaries.md"] = """---
aliases: [Order of the Bright Knight, Order of Sir Galen]
tags: [faction, religion]
---
# The Silver Luminaries

Followers of [[Sir Galen]], this order believes that the flawless "silver" artifacts of the ancients are divine gifts of pure light meant to banish the darkness. 

- **Favored Weapon:** Mace (often polished to a mirror shine and flanged to resemble a sunburst).
- **Alignment:** Lawful.
- **Turn Undead:** A blinding, searing light—accompanied by a perfectly pitched humming sound—washes over the undead, burning the shadows from their rotting flesh.
- **Preferred Spells:** *Light*, *Continual Light*, *Protection from Evil*, *Striking*.
- **Esoteric Restriction (Vow of the Untarnished):** Adherents must never allow their weapons or armor to rust or soil. A speck of dirt on their holy implements is a spiritual failing, requiring fasting and polishing to atone.
"""

files["The Withered Path.md"] = """---
aliases: [Cult of Alaric]
tags: [faction, religion]
---
# The Withered Path

Followers of [[Alaric]], who preach that the world must rot to feed the new spring. They act as grim but necessary tenders of the natural cycle.

- **Favored Weapon:** Wooden Staff (carved from petrified wood or diseased roots).
- **Alignment:** Neutral.
- **Turn Undead:** The cleric reasserts the "true cycle." The undead weep dust, their bones turning to ash and blowing away, or collapsing into inert mulch.
- **Preferred Spells:** *Cure Light Wounds* (roleplayed as drawing out sickness), *Cure Disease*, *Speak with Plants*, *Hold Person*.
- **Esoteric Restriction:** Adherents refuse to eat fresh food. All food consumed must be fermented, aged, or slightly spoiled (hard cheese, fermented wine, cured meats) as a daily communion with the rot.
"""

files["The Hearth of the First Queen.md"] = """---
aliases: [Faith of Aenor]
tags: [faction, religion]
---
# The Hearth of the First Queen

Followers of [[Aenor]], these clerics are the premier protectors and healers of the common folk, embodying the maternal defense of early humanity.

- **Favored Weapon:** Sling (representing the humble defense of the commoners).
- **Alignment:** Lawful.
- **Turn Undead:** A warm presence fills the area. The unnatural animus leaves the undead peacefully as a voice echoes to "Rest now, child," causing them to lie down and cease moving.
- **Preferred Spells:** *Purify Food and Water*, *Bless*, *Remove Fear*, *Create Food*.
- **Esoteric Restriction (Rite of the Shared Cup):** When making camp, they must light the central fire, and are forbidden from taking their first drink of water without offering a portion to a stranger or companion first.
"""

files["The Ascendant Sky.md"] = """---
aliases: [Faith of Lothar, The Floating Tyrants]
tags: [faction, religion]
---
# The Ascendant Sky

Followers of [[Lothar]], who believe his mastery over gravity is the Divine Levitation—the magical right to rule from above. The church is ambitious, structured, and ruthless.

- **Favored Weapon:** Warhammer (bringing the crushing weight of gravity down upon the enemy).
- **Alignment:** Chaotic.
- **Turn Undead:** Air pressure drops suddenly, creating a localized vacuum. Undead are thrown backward by invisible kinetic force, tumbling as they lose purchase on the earth.
- **Preferred Spells:** *Resist Cold*, *Silence 15' radius*, *Dispel Evil*, *Continual Light*.
- **Esoteric Restriction:** They must sleep at least one foot off the ground. Touching the bare earth while resting is a sign of submission to the "lower world."
"""

files["The Twin Vanguard.md"] = """---
aliases: [Faith of Caelen and Beric, The Hunters]
tags: [faction, religion]
---
# The Twin Vanguard

A martial religion venerating [[Caelen]] and [[Beric]]. The church is split: the Vanguard uses disciplined, noble tactics, while the Thorns harness primal, mutated ferocity.

- **Favored Weapon:** Club. Perfectly balanced, iron-shod batons (Caelen), or jagged, studded cudgels of monster bone (Beric).
- **Alignment:** Lawful (Caelen sect) or Neutral (Beric sect).
- **Turn Undead:** A terrifying, predatory aura emanates from the cleric. The undead are turned by supernatural fear, sensing the apex predator of their kind has arrived.
- **Preferred Spells:** *Detect Evil*, *Resist Fire*, *Striking*, *Cure Serious Wounds*.
- **Esoteric Restriction (Tithe of the Hunt):** They must keep a physical trophy from the most dangerous creature they defeat each season. If a season passes without a worthy kill, they must undergo ritual scarification.
"""

files["The Anchorite Brotherhood.md"] = """---
aliases: [Followers of Clovis]
tags: [faction, religion]
---
# The Anchorite Brotherhood

Followers of [[Clovis]], these extreme survivalists view his isolation as a divine withdrawal. They are hidden protectors and hoarders of secret histories.

- **Favored Weapon:** Staff (doubling as a walking stick for traversing lonely places).
- **Alignment:** Neutral.
- **Turn Undead:** The cleric speaks a word of profound silence. The undead lose track of them entirely, blinded by a divine shroud of apathy, and wander away aimlessly.
- **Preferred Spells:** *Find Traps*, *Know Alignment*, *Locate Object*, *Silence 15' radius*.
- **Esoteric Restriction (Vow of the Hidden Face):** In the presence of a ruling monarch, noble, or when performing religious rites, they must veil their face or wear a blank mask.
"""

files["The Cult of the Chimera.md"] = """---
aliases: [Faith of Drust]
tags: [faction, religion]
---
# The Cult of the Chimera

Followers of [[Drust]], who worship mutation, forced evolution, and the breaking of natural laws. They view a static human body as an unfinished canvas.

- **Favored Weapon:** Flail (representing unpredictable, thrashing appendages).
- **Alignment:** Chaotic.
- **Turn Undead:** The cleric’s aura disrupts necrotic magic. The undead briefly and uncontrollably mutate—sprouting useless limbs or tumors—before collapsing under the strain of cancerous growth.
- **Preferred Spells:** *Cause Light Wounds*, *Resist Fire*, *Cause Disease*, *Neutralize Poison*.
- **Esoteric Restriction (The Flesh Tithe):** A clean body is spiritual stagnation. When surviving a brush with death or gaining a level, they must perform ritual scarification or accept a brand. They refuse magical healing for cosmetic damage.
"""

files["The Children of Ash.md"] = """---
aliases: [Faith of Vortigern]
tags: [faction, religion]
---
# The Children of Ash

Followers of [[Vortigern]], these doomsday zealots view civilization as a cage that must be reduced to ash so the world can start over.

- **Favored Weapon:** Morningstar (symbolizing a bursting star or explosive core).
- **Alignment:** Chaotic.
- **Turn Undead:** Undead are not repelled; they are melted. Their flesh cooks and bones turn to slag as a sudden, silent wave of divine radiation washes over them.
- **Preferred Spells:** *Darkness*, *Silence 15' radius*, *Striking*, *Cause Serious Wounds*.
- **Esoteric Restriction (Vow of Entropy):** To hoard wealth is an affront. Every morning at dawn, the cleric must cast a valuable or highly useful item into a fire and watch it burn to ash.
"""

# Dwarf Clans
files["Clan Zabar.md"] = """---
aliases: [The Zabar Collective]
tags: [faction, dwarves]
---
# Clan Zabar

An active clan of [[Dwarves]] operating out of a massive surface quarry. Originally a surface-extraction unit, they survived the ages by refusing to delve deep. They are paranoid hoarders who craft heavy, steam-powered approximations of [[Precursors|Precursor]] technology.

- **Status:** Active
- **Notable Figures:** [[Zabar]]
- **Associated Locations:** The Copper Cave 
"""

files["Clan Kurgal.md"] = """---
aliases: [The Kurgal Depths]
tags: [faction, dwarves]
---
# Clan Kurgal

A defunct clan of [[Dwarves]] wiped out after their deep-mining operations breached the hibernation cyst of an [[Abominations|Abomination]]. Their fortress is now a lethal ruin filled with hoarded wealth and eldritch spawn.

- **Status:** Defunct (Overrun)
- **Notable Figures:** [[Kurgal]]
- **Associated Locations:** Den of the Dead Kurgal
"""

files["Clan Gundinul.md"] = """---
aliases: [The Gundinul Quarantine]
tags: [faction, dwarves]
---
# Clan Gundinul

A defunct clan of [[Dwarves]] originally tasked with refining highly volatile, arcane isotopes for [[Precursors|Precursor]] energy cells. Left without oversight, their programming degraded until a catastrophic experiment with a "Reality Forge" tore a hole in spacetime, allowing a shifting, formless [[Abominations|Abomination]] into their hold. The automated doors permanently sealed the clan inside to contain the threat.

- **Status:** Defunct (Quarantined)
- **Notable Figures:** *(Add notable figures here)*
- **Associated Locations:** [[B.10]] The Ashen Cave (or The Dead Fort)
"""

files["Clan Lugal-Ur.md"] = """---
aliases: [The Lugal-Ur Garrison]
tags: [faction, dwarves]
---
# Clan Lugal-Ur

A defunct clan of [[Dwarves]] that originally operated as a logistics and transport hub. Following the departure of the [[Precursors]], the clan suffered a massive directive-cascade failure. Desperate to find their creators, they built a colossal subterranean boring machine, accidentally driving it into the lair of a massive [[Abominations|Abomination]]. The constructs intentionally collapsed the cavern to entomb the beast, sacrificing themselves in the process.

- **Status:** Defunct (Entombed)
- **Notable Figures:** *(Add notable figures here)*
- **Associated Locations:** [[J.3]] The Grim Stone (or The Stalwart Tomb)
"""

# Halfling Shires
files["The Elysian Dale.md"] = """---
aliases: [Elysium, The Active Shire]
tags: [faction, halflings, location]
---
# The Elysian Dale

An active, idyllic shire inhabited by [[Halflings]]. Originally an agricultural sector for the [[Precursors]], the halflings have maintained the hyper-resilient flora, viewing their farming duties as sacred, druidic rites passed down by the Ascended Ones. 

The community thrives around a buried terraforming artifact they call the "Well of Ceres," which keeps their valley lush and immune to blight.

- **Status:** Active
- **Notable Figures:** [[Castor]]
- **Associated Locations:** [[The Hidden Meadow]]
"""

files["The Asphodel Thicket.md"] = """---
aliases: [Asphodel, The Ruined Shire]
tags: [faction, halflings, location]
---
# The Asphodel Thicket

An abandoned shire that once served as a biological waste-filtration site for the [[Precursors]]. The [[Halflings]] here tended a specialized moss that eventually mutated due to volatile arcane runoff. The carnivorous moss overran the idyllic burrows, forcing the survivors to flee.

The ruins are now a highly dangerous thicket choked with toxic spores, carnivorous plants, and un-triggered mechanical defenses.

- **Status:** Defunct (Overrun by mutated flora)
- **Notable Figures:** [[Titus]] (scavenger of the ruins)
- **Associated Locations:** [[The Dark Grove]]
"""

# Elves & Havens
files["Elves.md"] = """---
aliases: [The Abandoned Caste, First of the Last, Greatest of the Least]
tags: [culture, faction]
---
# Elves

The closest mortal species to the [[Precursors]], but considered the least of them—painfully average and untalented compared to their ascended creators. They were left behind when the Precursors vanished, forcing them to help the Inhuman [[God-Kings]] fend off the [[Abominations]]. 

They are deeply isolationist. The faction is led by the "Greatest of the Least" (often called the First of the Last)—ancient elves who have been alive since before the departure. These elders are deeply bitter at being abandoned and watching their utopia degrade. However, a generational divide is forming: younger elves, lacking this eons-old hurt, are growing increasingly curious about the outside world.

- **Naming Convention**: Babylonian / Mesopotamian
- **Notable Figures**: [[Ereshki]], [[Enlil]]
"""

files["City of the Ancient Heart.md"] = """---
aliases: [The Last Sanctuary]
tags: [faction, elves, location, haven]
---
# City of the Ancient Heart

The last fully functioning enclave of the [[Elves]], ruled by the bitter elders known as the "Greatest of the Least." Originally a minor bureaucratic and artistic hub, it is now a heavily warded sanctuary. 

The elders strictly forbid contact with the outside world, harboring deep resentment over the loss of the [[Precursors]] and their ruined utopia. Despite this, younger elves frequently sneak past the magical barriers to explore the modern world. The elders here also dedicate significant magical resources to protecting the hidden stasis pods of [[Dumuzi]].

- **Status:** Active (Isolationist)
- **Associated Figures:** [[Dumuzi]] (Protected by their wards)
- **Associated Locations:** City of the Ancient Heart
"""

files["The Ruin of Anu.md"] = """---
aliases: [The Fallen Library]
tags: [faction, elves, location, ruin]
---
# The Ruin of Anu

Once a magnificent arcane library and sanctuary for the [[Elves]], named in honor of the Precursor [[Anu]]. 

During the great war, the Elven commander [[Enlil]] died defending its gates against the [[Abominations]], fracturing his spirit in the process. The sanctuary ultimately fell from within when [[Ereshki]], driven mad by bitterness, used forbidden eldritch magic in a failed attempt to force the elves into ascension. The resulting magical cataclysm twisted the survivors into horrific undead and warped the beautiful architecture. 

- **Status:** Defunct (Corrupted / Overrun)
- **Associated Figures:** [[Enlil]] (Haunting the gates), [[Ereshki]] (Responsible for its fall)
- **Associated Locations:** The Ruin of Anu
"""

# Lesser Abominations
files["Azag.md"] = """---
aliases: [The Ashen Dread, The First Dragon]
tags: [character, abomination, enemy, dragon]
---
# Azag

An [[Abominations|Abomination]] that adapted to the physical world by forming a hyper-dense biological shell of scale and flame. Azag is the progenitor of the world's dragons.

Aligned with Chaos, Azag hoards magical artifacts and wealth in an attempt to create a magical singularity to tear a hole in reality. It took the combined strength of several [[God-Kings]], including [[Beric]], to ground it. It is capable of spawning lesser dragons, wyverns, and hydras.

- **Associated Locations**:
  - [[The Doomed Mountain]]
  - [[Tower of the Shivering Ash]]
  - [[The Black Ash]]
"""

files["Namtar.md"] = """---
aliases: [The Shrouded King, The Death Knight]
tags: [character, abomination, enemy, undead]
---
# Namtar

A terrifying [[Abominations|Abomination]] corrupted not by the physical elements, but by the concept of Law. Having telepathically linked with humanity during the great war, Namtar became obsessed with perfect, deathly order. 

It views biological life as chaotic and agonizing, and seeks to impose eternal stasis (undeath) upon the world. It wears the rusted armor of an assimilated God-King and commands the intelligent undead (Liches, Wraiths, Spectres) as its lesser spawn.

- **Associated Locations**:
  - [[The Shrouded Wall]]
  - [[The Shrouded Crossing]]
  - [[The Shrouded Crystal]]
"""

# Local Threats
files["The Iron-Dogs.md"] = """---
aliases: [Kaelen's Bandits, The Breakers]
tags: [faction, enemy, bandits]
---
# The Iron-Dogs

A chaotic, highly organized company of rogue mercenaries led by Kaelen "The Breaker." Driven entirely by self-interest, greed, and a "might makes right" philosophy, they are a major threat to local trade. 

Kaelen (a 7 HD Fighter) wields a masterwork [[Precursors|Precursor]] halberd and commands a tactically sound force of crossbowmen and veterans. 

- **Alignment:** Chaotic
- **Associated Figures:** Kaelen The Breaker
- **Associated Locations:** [[The Thundering Ridge]] (Hex P.12)
"""

files["Silas the Pallid.md"] = """---
aliases: [The Shrouded Necromancer, Silas]
tags: [character, enemy, magic-user, lawful]
---
# Silas the Pallid

A powerful (9 HD) human Magic-User who was corrupted by the telepathic broadcast fragments of the [[Abominations|Abomination]] [[Namtar]]. Silas views biological life as a chaotic, agonizing fever. 

He acts out of a twisted sense of Lawful pity, seeking to "cure" the world by imposing the perfect, silent order of undeath. He exclusively utilizes mindless undead (Skeletons and Zombies) as a perfectly obedient, synchronized workforce.

- **Alignment:** Lawful (Twisted)
- **Associated Factions:** Cult of [[Namtar]] (Ideological)
- **Associated Locations:** [[The Shrouded Crystal]] (Hex K.11)
"""

files["The Flesh-Weaver.md"] = """---
aliases: [The Spawning Horror]
tags: [character, abomination, enemy]
---
# The Flesh-Weaver

An 8 HD "lesser" [[Abominations|Abomination]] hiding near the town at N.10. It is a bloated, physically degrading mass of eldritch biology that cannot easily move. 

To hunt and interact with the physical world, it constantly spawns and regurgitates semi-stable biological drones. These drones (mechanically functioning as B/X Goblins) are pale, hairless homunculi that dissolve into gray sludge when killed. They scour the countryside for biomass to drag back to their creator.

- **Alignment:** Chaotic
- **Associated Locations:** [[The Muck's Rock]] (Hex L.8)
"""

files["The Copper-Grubbers.md"] = """---
aliases: [The Grubbers, Scavengers]
tags: [faction, enemy, low-level]
---
# The Copper-Grubbers

A loose gang of exiled townsfolk, desperate addicts, and cowards who sift through the fens looking for broken [[Precursors|Precursor]] scrap. They are barely armed, wielding slings and clubs.

They are cowardly but dangerous to wounded travelers, relying on crude mud-traps, tripwires, and ambushes. They possess terrible morale and will scatter if faced with true magic or heavy resistance.

- **Alignment:** Neutral / Chaotic
- **Associated Factions:** Exiles of the main town
- **Associated Locations:** [[The Low Mud]] (Hex M.10)
"""

files["Ash-Rats.md"] = """---
aliases: [Mutated Rodents]
tags: [creature, enemy, low-level]
---
# Ash-Rats

Oversized, hairless rodents native to the Deadfen Moors. Their veins glow faintly due to a diet of arcane runoff and Eldritch moss. 

They are aggressive, amphibious pack hunters. Their bites are filthy, carrying a small chance of infecting the victim with a minor, feverish disease born from the lingering necrotic ash of the region.

- **Alignment:** Neutral (Animal)
- **Associated Locations:** [[The Red Hole]] (Hex N.9), and ubiquitous across the fens.
"""

files["Scrubbers.md"] = """---
aliases: [Maintenance Drones, Pipe-Cleaners]
tags: [creature, construct, enemy, low-level]
---
# Scrubbers

Ancient, segmented [[Precursors|Precursor]] maintenance drones originally designed to clean plumbing and ventilation shafts. They resemble metallic, multi-legged serpents.

Bereft of their original programming, they mindlessly attempt to "clean" biological lifeforms by injecting them with highly toxic chemical solvents. This solvent acts as a debilitating poison that leaves victims violently ill. As mindless constructs, they fight to the death and never retreat.

- **Alignment:** Neutral (Construct)
- **Associated Locations:** [[The Iron Circle]] (Hex O.10)
"""

# Player Primer & Rumors
files["Player Primer.md"] = """Welcome to the Deadfen Moors: Player Primer

The Mythic History (What Everyone Knows)

Long ago, the world was shaped by the Ascended Ones, a pantheon of flawless creators who built magnificent cities of gleaming metal and boundless magic. For unknown reasons, they abandoned the mortal realm. In their wake came the Abominations—terrifying, eldritch horrors that boiled up from the deep earth to unmake reality.

Humanity survived only because of the God-Kings, powerful, mythic champions whose very blood was a weapon against the dark. The God-Kings fought the horrors to a standstill, but their kingdoms eventually collapsed into infighting and ruin. Today, the world is a dangerous, wild place built upon the bones of these ancient, magical empires.

The Peoples of the World

Humans: The dominant species. The modern kingdoms are led by the un-powered descendants of the God-Kings, struggling to reclaim the glory of the past.

Dwarves: Believed to be ancient, living constructs forged by the Ascended Ones to harvest the earth's bounty. They are relentless, often paranoid, and many of their greatest clans have been lost to the horrors that slumber in the deep.

Halflings: Blessed caretakers of the natural world. They wield ancient, druidic miracles that keep their hidden shires immune to the world's blights, believing it is their sacred duty to maintain the Ascended Ones' gardens.

Elves: Known as the "First of the Last." They are an ancient, painfully isolationist people who were left behind when the Ascended Ones departed. Led by bitter, immortal elders who watched their utopia burn, they hide behind powerful magical wards. However, younger elves frequently wander into the human lands, seeking adventure.

Faiths and Divine Magic (For Clerics)

True divine magic is channeled through devotion to the lingering power of the ancient God-Kings. Clerics usually follow one of these dominant faiths:

The Silver Luminaries: Followers of the Bright Knight, Sir Galen. They worship flawless, untarnished light and seek to recover holy ancient artifacts.

The Hearth of the First Queen: Devotees of Queen Aenor. They are the ultimate protectors of the common folk, focusing on healing, community, and maternal warmth.

The Twin Vanguard: A martial faith worshiping the great hunters, Caelen and Beric. Followers embrace either strict, noble battlefield discipline or primal, mutated ferocity to destroy monsters.

The Withered Path: Followers of the fallen King Alaric. They are grim tenders of the natural cycle, believing that rot and decay are holy and necessary transitions.

The Ascendant Sky: A ruthless, ambitious church worshiping King Lothar. They believe in the "Divine Levitation"—the magical right to dictate the law from above.

The Anchorite Brotherhood: Followers of Clovis the Lonely. Extreme survivalists who preserve secret knowledge and hide their faces from a collapsing world.

(Warning: Darker, chaotic cults also exist in the wilds, worshipping terrifying concepts like forced flesh-mutations or apocalyptic holy fire.)

Available Quests & Bounties

You find yourselves in a frontier town situated on the edge of the Deadfen Moors. The local notice board, town guard, and desperate locals are offering coin for capable adventurers.

- The Captain's Bounty: Cull the "Pale Thieves" (pale, hairless goblins) dragging livestock northwest.
- The Antiquarian's Request: Recover antique scrap or "silver" from the metallic ruins of The Iron Circle (Hex O.10).
- The Missing Herbalist: Find the healer who vanished in the western bogs (Hex M.10).
- The Miller's Cellar: Clear the glowing "Ash-Rats" from a breached root cellar corridor.
- The Stolen Lockbox: Retrieve a merchant's iron lockbox from heavily armed bandits at The Thundering Ridge (Hex P.12).
"""

files["Rumors.md"] = """**2d6 Deadfen Moors Rumor Table**
(Rolling 2d6: First die is tens, second die is ones)

- **11 (T):** "Don't go near the water at The Red Hole (N.9). The giant rats there are completely bald, and their bite gives you a fever that rots you from the inside out."
- **12 (PT):** "The mud in the western bogs (M.10) is cursed! It'll swallow a man whole if he steps off the roots." (Grubbers dig pit-traps).
- **21 (T):** "Those desperate exiles who live in the western mud have banded together. They aren't just sifting for scrap anymore; they're ambushing lone travelers."
- **31 (T):** "There's a scholar in town paying triple the going rate for any un-tarnished 'silver' you can drag out of the ruins east of here."
- **34 (T):** "The 'metal snakes' in the ruins don't bite to eat you. They inject a blinding chemical solvent that makes you violently ill for days."
- **41 (T):** "A company of heavily armored mercenary rogues have set up a barricade on The Thundering Ridge (P.12) and are extorting merchants."
- **44 (T):** "A perfectly pale, hairless wizard has moved into the Shrouded Crystal ruins (K.11). The trees are dying in a perfect circle around his camp."
- **51 (T):** "There are pale, hairless goblins with too many joints stealing sheep and dragging them screaming toward The Muck's Rock (L.8)."
- **53 (T):** "If you need masterwork plate armor and have a cart full of raw copper ore, Clan Zabar at The Copper Cave (N.8) will trade with you."
- **61 (T):** "The Clerics of the Bright Knight are strict. If they let a single speck of rust touch their maces, they have to fast and pray to get their magic back."
- **64 (T):** "Don't mess with the Twin Vanguard clerics. Their religion forces them to hunt down the biggest monster they can find proof of."
"""

for filename, content in files.items():
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w") as f:
        f.write(content.strip())
        print(f"Created {filepath}")

print(f"Successfully created {len(files)} files in {output_dir}")
