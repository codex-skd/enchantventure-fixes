execute if entity @s[nbt=!{weapon: {components: {"minecraft:enchantments": {"levels": {"minecraft:infinity": 1}}}}}] run tag @s add no_infinity
execute if entity @s[nbt=!{weapon: {components: {"minecraft:enchantments": {"levels": {"minecraft:multishot": 1}}}}}] run tag @s add no_multishot
tag @s add enchant_checked
