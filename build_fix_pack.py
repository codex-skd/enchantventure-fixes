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
            "description": "EnchantVenture data fixes: tntfoundry, formationsoverworld, fokus, nerospace, nerologistics",
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

    write("data/nerologistics/recipe/configurator.json", {
        "type": "minecraft:crafting_shaped",
        "key": {"I": {"item": "minecraft:iron_ingot"}},
        "pattern": ["I I", " I ", " I "],
        "result": {"id": "nerologistics:configurator"},
    })

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
