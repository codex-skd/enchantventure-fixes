import json
import os
import shutil
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
MODS = r"C:\Users\llagu\curseforge\minecraft\Instances\EnchantVenture\mods"
SRC = os.path.join(ROOT, "datapack")
BUILD = os.path.join(ROOT, "build")
VERSION = open(os.path.join(ROOT, "version.txt"), encoding="utf-8").read().strip()
ZIP = os.path.join(BUILD, f"EnchantVenture_fixes-{VERSION}.zip")


def jar(mod):
    return os.path.join(MODS, mod)


def clean(d):
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)


def write(path, data):
    full = os.path.join(SRC, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def read_from_jar(mod, name):
    with zipfile.ZipFile(jar(mod)) as z:
        return json.loads(z.read(name).decode("utf-8"))


def fix_item_field(node):
    if isinstance(node, dict):
        for k, v in list(node.items()):
            if k == "items" and isinstance(v, str):
                item = v if ":" in v else "tntfoundry:" + v
                node[k] = [item]
            else:
                fix_item_field(v)
    elif isinstance(node, list):
        for v in node:
            fix_item_field(v)


def main():
    clean(SRC)

    write("pack.mcmeta", {
        "pack": {
            "description": "EnchantVenture data fixes: tntfoundry, formationsoverworld, fokus, nerospace, the_lost_city, berezka_api",
            "min_format": [107, 1],
            "max_format": 107,
        }
    })

    for name in ["hollow", "paperwork", "precision", "remote_work", "the_big_one", "full_catalogue"]:
        d = read_from_jar("tntfoundry-1.0.0.jar", f"data/tntfoundry/advancement/{name}.json")
        fix_item_field(d)
        write(f"data/tntfoundry/advancement/{name}.json", d)

    for name in ["stone_tower", "witch_tower"]:
        d = read_from_jar("formationsoverworld-1.0.5a-mc1.21+.jar",
                          f"data/formationsoverworld/loot_table/{name}/smithing.json")

        def swap_chain(node):
            if isinstance(node, dict):
                if node.get("name") == "minecraft:chain":
                    node["name"] = "minecraft:iron_ingot"
                for v in node.values():
                    swap_chain(v)
            elif isinstance(node, list):
                for v in node:
                    swap_chain(v)

        swap_chain(d)
        write(f"data/formationsoverworld/loot_table/{name}/smithing.json", d)

    write("data/fokus/predicate/is_night.json", {
        "condition": "minecraft:time_check",
        "clock": "minecraft:overworld",
        "period": 24000,
        "value": {"min": 12000, "max": 22500},
    })

    fokus_functions = {
        "kp4o6wh": [
            "schedule function fokus:nxf/kp4o6wh 1s",
            "scoreboard players add $fk.ttm fk.ttm 1",
        ],
        "11z33h0q4": [
            "scoreboard objectives add fk.ptm minecraft.custom:minecraft.play_time",
            "scoreboard players set $1Sux rl.basic 1",
        ],
        "_ignored_bffhan5h": [
            "item replace entity @s weapon.mainhand with air",
            "scoreboard players set $1xOQSeC7Zy 70w7 1",
        ],
    }
    for name, lines in fokus_functions.items():
        full = os.path.join(SRC, f"data/fokus/function/nxf/{name}.mcfunction")
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines) + "\n")

    write("data/nerospace/advancement/guide/new_life.json", {
        "parent": "nerospace:guide/living_world",
        "criteria": {
            "bred_ember_strutter": {"trigger": "minecraft:bred_animals"},
            "bred_meadow_loper": {"trigger": "minecraft:bred_animals"},
            "bred_woolly_drift": {"trigger": "minecraft:bred_animals"},
        },
        "display": {
            "description": "Breed a creature born of a terraformed world",
            "frame": "goal",
            "icon": {"id": "nerospace:meadow_loper_spawn_egg"},
            "title": "New Life",
        },
        "requirements": [["bred_meadow_loper", "bred_ember_strutter", "bred_woolly_drift"]],
        "sends_telemetry_event": True,
    })

    lost_city_pools = ["husk", "pillager", "vindicator", "zombie", "zombie_moss"]
    for spawner in lost_city_pools:
        pool = f"spawners_{spawner}"
        write(f"data/the_lost_city/worldgen/template_pool/{pool}.json", {
            "name": f"the_lost_city:{pool}",
            "fallback": "minecraft:empty",
            "elements": [
                {
                    "weight": 1,
                    "element": {
                        "element_type": "minecraft:single_pool_element",
                        "location": f"the_lost_city:spawner_{spawner}",
                        "processors": "minecraft:empty",
                        "projection": "rigid",
                    }
                }
            ],
        })

    # berezka_api's own built-in loot tables never register: openPrimary() throws a
    # NullPointerException while building the built-in pack's metadata (icon array is
    # null), so the pack "berezka_api_data" never gets added and every berezka_api:*
    # loot table resolves to "does not exist". Item lists below were recovered from
    # string constants in BuiltInResourcePack.class (berezka_api-1.2.9.5-beta.3);
    # exact rolls/weights/counts are not recoverable from bytecode, so quantities are
    # a reasonable approximation, not the mod's original values.
    write("data/berezka_api/loot_table/chests/car.json", {
        "type": "minecraft:chest",
        "pools": [
            {
                "rolls": {"min": 2, "max": 4},
                "entries": [
                    {"type": "minecraft:item", "name": "minecraft:cobweb", "weight": 4},
                    {"type": "minecraft:item", "name": "minecraft:fishing_rod", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:emerald", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:gunpowder", "weight": 1},
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:iron_ingot",
                        "weight": 1,
                        "functions": [
                            {"function": "minecraft:set_count", "count": {"min": 1, "max": 3}}
                        ],
                    },
                    {"type": "minecraft:item", "name": "minecraft:bread", "weight": 1},
                ],
            }
        ],
        "random_sequence": "berezka_api:chests/car",
    })

    write("data/berezka_api/loot_table/chests/berezkahousesmall_0.json", {
        "type": "minecraft:chest",
        "pools": [
            {
                "rolls": {"min": 1, "max": 3},
                "entries": [
                    {"type": "minecraft:item", "name": "minecraft:cobweb", "weight": 2},
                    {"type": "minecraft:item", "name": "minecraft:iron_ingot", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:bread", "weight": 1},
                    {
                        "type": "minecraft:group",
                        "children": [
                            {"type": "minecraft:item", "name": "minecraft:poisonous_potato"},
                            {"type": "minecraft:item", "name": "minecraft:potato"},
                            {"type": "minecraft:item", "name": "minecraft:baked_potato"},
                            {"type": "minecraft:item", "name": "minecraft:cobweb"},
                        ],
                    },
                ],
            }
        ],
        "random_sequence": "berezka_api:chests/berezkahousesmall_0",
    })

    write("data/berezka_api/loot_table/chests/diningroom.json", {
        "type": "minecraft:chest",
        "pools": [
            {
                "rolls": {"min": 2, "max": 4},
                "entries": [
                    {"type": "minecraft:item", "name": "minecraft:bread", "weight": 2},
                    {"type": "minecraft:item", "name": "minecraft:cobweb", "weight": 5},
                    {"type": "minecraft:item", "name": "minecraft:cake", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:baked_potato", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:poisonous_potato", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:cookie", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:mushroom_stew", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:suspicious_stew", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:pumpkin_pie", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:cooked_beef", "weight": 1},
                    {"type": "minecraft:empty", "weight": 3},
                ],
            }
        ],
        "random_sequence": "berezka_api:chests/diningroom",
    })

    write("data/berezka_api/loot_table/chests/farm.json", {
        "type": "minecraft:chest",
        "pools": [
            {
                "rolls": {"min": 1, "max": 3},
                "entries": [
                    {"type": "minecraft:item", "name": "minecraft:wheat_seeds", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:pumpkin_seeds", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:melon_seeds", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:beetroot_seeds", "weight": 1},
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:cobweb",
                        "weight": 1,
                        "functions": [
                            {"function": "minecraft:set_count", "count": {"min": 1, "max": 2}}
                        ],
                    },
                ],
            }
        ],
        "random_sequence": "berezka_api:chests/farm",
    })

    write("data/berezka_api/loot_table/chests/store.json", {
        "type": "minecraft:chest",
        "pools": [
            {
                "rolls": {"min": 3, "max": 6},
                "entries": [
                    {"type": "minecraft:item", "name": "minecraft:bread", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:apple", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:cooked_beef", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:rotten_flesh", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:cobweb", "weight": 4},
                    {"type": "minecraft:item", "name": "minecraft:iron_sword", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:crossbow", "weight": 1},
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:arrow",
                        "weight": 1,
                        "functions": [
                            {"function": "minecraft:set_count", "count": {"min": 4, "max": 12}}
                        ],
                    },
                    {"type": "minecraft:item", "name": "minecraft:bow", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:iron_axe", "weight": 1},
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:iron_ingot",
                        "weight": 1,
                        "functions": [
                            {"function": "minecraft:set_count", "count": {"min": 1, "max": 5}}
                        ],
                    },
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:gold_nugget",
                        "weight": 1,
                        "functions": [
                            {"function": "minecraft:set_count", "count": {"min": 1, "max": 4}}
                        ],
                    },
                    {"type": "minecraft:item", "name": "minecraft:emerald", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:book", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:paper", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:map", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:iron_helmet", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:iron_chestplate", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:iron_leggings", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:iron_boots", "weight": 1},
                ],
            }
        ],
        "random_sequence": "berezka_api:chests/store",
    })

    # This one was recovered verbatim (rolls/weights/counts are the mod's real
    # values, not an approximation) from a literal JSON string constant in the
    # class file, unlike the tables above which are reconstructed from separate
    # item-name string fragments.
    write("data/berezka_api/loot_table/chests/treasure.json", {
        "pools": [
            {
                "rolls": 1,
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:iron_ingot",
                        "weight": 100,
                        "functions": [
                            {"function": "minecraft:set_count", "count": {"min": 5, "max": 20}}
                        ],
                    },
                    {"type": "minecraft:item", "name": "minecraft:air", "weight": 10},
                ],
            },
            {
                "rolls": 1,
                "entries": [
                    {"type": "minecraft:item", "name": "minecraft:diamond", "weight": 1},
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:gold_ingot",
                        "functions": [
                            {
                                "function": "minecraft:set_count",
                                "count": {"type": "minecraft:uniform", "min": 1, "max": 5},
                            }
                        ],
                    },
                ],
            },
            {
                "rolls": 5,
                "entries": [
                    {"type": "minecraft:item", "name": "minecraft:cobweb", "weight": 1}
                ],
            },
        ],
        "random_sequence": "berezka_api:chests/treasure",
    })

    shutil.copy(os.path.join(ROOT, "pack.png"), os.path.join(SRC, "pack.png"))

    clean(BUILD)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _, files in os.walk(SRC):
            for f in files:
                full = os.path.join(dirpath, f)
                arc = os.path.relpath(full, SRC)
                z.write(full, arc)

    total = sum(len(fs) for _, _, fs in os.walk(SRC))
    print(f"OK. {total} archivos en {SRC}")
    print(f"ZIP: {ZIP}")


if __name__ == "__main__":
    main()
