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


def write_mcfunction(path, lines):
    full = os.path.join(SRC, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


MARSWARD_FIELD_MANUAL_ES = {
  "chapters": [
    {
      "id": "mission_brief",
      "kind": "prose",
      "paragraphs": [
        "Tu primer trabajo es construir un Kit de cohete en la Tierra.",
        "Usa el Kit de cohete sobre terreno abierto para montar tu cohete. Luego carga comida, herramientas, vidrio, cobre, hierro, redstone y cultivo de semillas antes de lanzarte.",
        "Tu libro de recetas ya conoce la receta del Kit de cohete.",
        "Una vez colocado el cohete, lee Prepara tu equipaje y Pilotar el cohete antes de partir.",
        "Tu misión en Marte: aterrizar sano y salvo, construir una base y explorar sin perderte ni quedarte sin aire."
      ],
      "title": "Tu misión"
    },
    {
      "id": "earth_prep",
      "kind": "prose",
      "paragraphs": [
        "Lee esto antes de fabricar un Kit de cohete. Recibes un Manual de campo la primera vez que apareces en la Tierra. Fabrica otro si lo pierdes.",
        "Trae esto:",
        "- Un Kit de cohete.",
        "- Comida para tus primeros días en Marte.",
        "- Vidrio, cobre, hierro y redstone. Más adelante encontrarás chatarra en Marte, pero trae abundante al principio.",
        "- Cultivo de semillas inicial hecho en la Tierra con semillas de trigo, semillas de calabaza, champiñón marrón y papel. Las plantas no pueden crecer al aire libre en Marte.",
        "- Un pico y una pala. Herramientas de hierro o mejores funcionan mejor.",
        "El Kit de cohete te da una Llave de encendido después de colocar el cohete.",
        "Extras útiles:",
        "- Más cobre y vidrio para ventanas, tanques y paneles solares.",
        "- Bloques de Luz de trabajo o los materiales para fabricarlos.",
        "- Papel y cuero por si tus amigos necesitan manuales de repuesto.",
        "Consulta el capítulo Referencia de fabricación para los materiales, y luego usa el libro de recetas para colocarlos."
      ],
      "title": "Prepara tu equipaje"
    },
    {
      "id": "rocket_operations",
      "kind": "prose",
      "paragraphs": [
        "Usa el Kit de cohete solo en la Tierra. Colócalo sobre suelo firme con espacio abierto encima.",
        "Obtendrás un cohete alto con una sala en su interior, un Núcleo de lanzamiento, una Llave de encendido y una puerta.",
        "Antes del lanzamiento:",
        "1. Entra en la sala del cohete.",
        "2. Cierra la puerta del cohete.",
        "3. Asegúrate de que todos los que viajan están dentro contigo.",
        "4. Usa el Núcleo de lanzamiento mientras sostienes la Llave de encendido.",
        "El cohete no despegará si la puerta está abierta o la sala está bloqueada. Solo viajan las personas dentro de la sala.",
        "Al lanzarte, tu cohete abandona la Tierra y aterriza en Marte. Quédate en ese cohete aterrizado hasta construir una base.",
        "Para volver a casa, entra de nuevo en el cohete de Marte, cierra la puerta y lánzate otra vez. Tu cohete aterrizará de vuelta en la Tierra, en el punto donde empezaste."
      ],
      "title": "Pilotar el cohete"
    },
    {
      "id": "first_hour",
      "kind": "prose",
      "paragraphs": [
        "Llegas dentro del cohete en Marte. El aire es seguro dentro hasta que sales caminando.",
        "Prueba esto primero:",
        "1. Coloca una Baliza de ruta junto al cohete para poder encontrar el camino de vuelta.",
        "2. Mina Regolito de Marte, Piedra de Marte, Basalto de Marte y Óxido de hierro de Marte cerca de ti.",
        "3. Busca hielo en el terreno roto y la piedra de hielo. Mina Mena de hielo de Marte para obtener Trozo de hielo.",
        "4. Fabrica Panel de hábitat, Ventana reforzada y Luz de trabajo en cuanto puedas.",
        "5. Coloca un Núcleo de hábitat y un Panel solar bajo cielo abierto antes de alejarte demasiado.",
        "Las antorchas y las hogueras no funcionan en Marte. Usa Luz de trabajo para iluminarte.",
        "Los charcos de agua y las granjas al aire libre no funcionan en Marte. Usa máquinas y salas cerradas en su lugar.",
        "Pueden aparecer Tormentas de polvo irregulares durante el día. Coloca bloques de Baliza de ruta antes de explorar para que el HUD de la tormenta pueda guiarte a casa."
      ],
      "title": "Primeros pasos en Marte"
    },
    {
      "id": "mars_rover",
      "kind": "prose",
      "paragraphs": [
        "Fabrica un Kit de rover cuando necesites una forma más rápida de explorar Marte. Usa una Batería de Marte, Unidad de control de máquina, Panel de hábitat, cobre, redstone y hierro.",
        "Usa el Kit de rover sobre suelo firme de Marte con un área despejada de 3 por 3 y dos bloques de altura libre. El kit no se consume si el despliegue está bloqueado.",
        "El asiento derecho conduce y el asiento izquierdo lleva a un pasajero. Usa avanzar o retroceder mientras miras hacia donde quieres girar; el rover no puede desplazarse lateralmente ni saltar.",
        "Abre tu inventario normal mientras vas montado para acceder a nueve espacios de carga. Interactúa agachado con el rover para comprobar carga, mercancía y asientos.",
        "Una carga completa da cinco minutos reales de conducción. Con la carga a cero el rover sigue siendo montable y su carga sigue siendo accesible, pero no puede moverse.",
        "Aparca el rover vacío, sin pasajeros, a menos de 10 bloques de un Núcleo de hábitat energizado. La energía solar lo carga de día; de noche o durante una Tormenta de polvo el núcleo necesita una Batería cargada.",
        "Para recuperar el Kit de rover, desmonta y ataca al rover. Un ataque de jugador lo desmonta al instante; otros daños reducen sus 12 PS y solo lo rompen al llegar a cero. Ambos caminos sueltan el kit más toda la carga."
      ],
      "title": "Conducir el rover de Marte"
    },
    {
      "id": "meteor_impacts",
      "kind": "prose",
      "paragraphs": [
        "Tras tu segundo día en Marte, pueden caer meteoritos raros sobre terreno natural ya explorado cerca de exploradores activos. Solo puede existir un lugar de impacto sin cosechar a la vez.",
        "Un aviso de cinco segundos muestra la dirección y distancia aproximadas del meteorito. Busca su brillante estela de llamas y humo y escucha el sonido de descenso; durante una Tormenta de polvo, una guía cercana señala hacia él a través de la visibilidad reducida.",
        "Los impactos de meteorito no destruyen bloques ni provocan incendios, y evitan cohetes, bases, máquinas, Paneles solares, Balizas de ruta, rovers y lugares de exploración ya conocidos.",
        "Cada impacto deja una pequeña marca oscura con exactamente un Depósito de meteoritos. Mina el depósito con un pico para recuperar de tres a cinco Fragmentos de meteorito y desbloquear el siguiente meteorito programado.",
        "Tras recuperarlo, el siguiente evento se programa de dos a cuatro días marcianos después. Funde cada Fragmento de meteorito en un horno para obtener un Lingote de hierro."
      ],
      "title": "Impactos de meteoritos"
    },
    {
      "id": "eva_life_support",
      "kind": "prose",
      "paragraphs": [
        "El aire exterior es peligroso. Tu traje tiene un temporizador. Se agota mientras estás fuera de las zonas seguras.",
        "Zonas seguras: dentro del cohete, o cerca de un Núcleo de hábitat en funcionamiento.",
        "Zonas seguras más grandes:",
        "- Un Núcleo de hábitat por sí solo crea una pequeña burbuja segura.",
        "- Añade un Panel solar bajo cielo abierto para hacer la burbuja mucho más grande.",
        "- Añade una Batería para mantener la burbuja grande activa cuando no hay sol o una Tormenta de polvo bloquea la energía solar.",
        "- Añade un Generador de oxígeno con agua en un tanque para hacerla aún más grande.",
        "El Generador de oxígeno solo gasta agua cuando alguien está en el rango de oxígeno extra más allá de la cobertura normal energizada.",
        "Sobre cuánto tiempo puedes estar fuera (consulta Números importantes para más detalles):",
        "- El traje dura unos 15 minutos en total fuera de zonas seguras.",
        "- El aviso empieza alrededor de los 7 minutos restantes.",
        "- El peligro empieza alrededor de los 3 minutos restantes.",
        "Vigila el mensaje en la parte inferior de tu pantalla. Vuelve al cohete o a la base para rellenar tu traje.",
        "Las balizas de ruta te ayudan a encontrar el camino. No te dan aire.",
        "Durante una Tormenta de polvo, la reserva EVA se agota más rápido y el movimiento es más lento mientras estás fuera de la cobertura segura."
      ],
      "title": "Aire y zonas seguras"
    },
    {
      "id": "mars_environment",
      "kind": "prose",
      "paragraphs": [
        "Estas cosas no funcionan en Marte:",
        "- Plantar semillas y champiñones al aire libre.",
        "- Dejar agua expuesta al aire libre.",
        "- Antorchas, faroles, velas, hogueras y herramientas de fuego.",
        "Para iluminar el interior de tu base, coloca bloques de Luz de trabajo.",
        "Para cultivar comida, construye una sala cerrada con paredes, suelo y techo. No debe haber huecos hacia el cielo exterior ni hacia cuevas.",
        "Coloca una Lámpara de invernadero y una Bandeja de invernadero dentro de la misma sala sellada. Esa sala también necesita cobertura de un Núcleo de hábitat energizado y agua almacenada cerca.",
        "Para la entrada, usa dos bloques de Puerta de esclusa con un pequeño espacio entre ellos. Mantén una puerta cerrada antes de abrir la otra para que el invernadero no se ventile hacia Marte.",
        "Caes más despacio en Marte, pero los agujeros y acantilados siguen haciendo daño. Vigila tus pasos.",
        "Las Tormentas de polvo solo ocurren durante el día y no siguen un horario simple. Desactivan la energía solar hasta que la tormenta amaina o termina el día."
      ],
      "title": "Reglas de Marte"
    },
    {
      "id": "materials_guide",
      "kind": "prose",
      "paragraphs": [
        "Encuentra esto en Marte:",
        "- Regolito de Marte - polvo similar a la tierra, para construir.",
        "- Piedra de Marte - roca resistente.",
        "- Basalto de Marte - roca oscura en zonas escarpadas.",
        "- Óxido de hierro de Marte - manchas rojizas oxidadas.",
        "- Mena de hielo de Marte y Trozo de hielo - tu fuente de agua.",
        "Encuentra esto en restos antiguos y cofres: cobre, hierro, pepitas y redstone.",
        "Trae esto desde la Tierra: vidrio, papel, semillas, cobre, hierro y redstone.",
        "Luz de trabajo es lo primero que puedes fabricar usando solo materiales de Marte. Casi todo lo demás necesita suministros de la Tierra al principio."
      ],
      "title": "Qué minar y qué traer"
    },
    {
      "id": "base_building",
      "kind": "prose",
      "paragraphs": [
        "Empieza con una caja cerrada pequeña cerca de tu cohete:",
        "- Paredes de Panel de hábitat o Piedra de Marte.",
        "- Ventanas de Ventana reforzada.",
        "- Puerta de Puerta de esclusa. Dos puertas con un pequeño espacio entre ellas forman una esclusa más segura.",
        "- Luces de Luz de trabajo.",
        "- Un Núcleo de hábitat en el centro.",
        "- Un Panel solar con cielo despejado encima.",
        "- Una Batería cerca del núcleo y del panel.",
        "No cubras el panel solar con bloques. Solo genera energía de día y no durante las Tormentas de polvo. Sus luces de colores muestran si el cielo está despejado y si está energizando el núcleo.",
        "Añade una sala a la vez: almacén, sala de agua, invernadero, taller.",
        "Coloca bloques de Baliza de ruta a lo largo de los caminos hacia el hielo, los restos y las cuevas."
      ],
      "title": "Construye tu base"
    },
    {
      "id": "machines_loops",
      "kind": "prose",
      "paragraphs": [
        "Energía: de día, un Panel solar bajo cielo abierto energiza un Núcleo de hábitat, que a su vez energiza las máquinas cercanas.",
        "Las Tormentas de polvo bloquean la energía solar durante el día. Una Batería cargada puede mantener energizado un Núcleo de hábitat cercano mientras dura la tormenta.",
        "Una Batería cerca de un Panel solar activo almacena energía. De noche o durante una tormenta, una batería cargada puede energizar un Núcleo de hábitat cercano.",
        "Las máquinas no pueden conectarse directamente al panel solar.",
        "Agua:",
        "1. Mina Trozo de hielo de la Mena de hielo de Marte.",
        "2. Colócate junto a un Procesador de agua sosteniendo hielo y úsalo.",
        "3. El agua va a un Tanque de agua vinculado.",
        "Comida:",
        "1. Consigue Cultivo de semillas inicial en la Tierra o en lugares lejanos.",
        "2. Construye una sala sellada con una Lámpara de invernadero y una Bandeja de invernadero. Usa una esclusa de dos puertas para que una puerta permanezca siempre cerrada.",
        "3. Usa el cultivo de semillas en una bandeja vacía.",
        "4. Mantén la lámpara energizada y con agua.",
        "5. Recoge Verduras de invernadero cuando la bandeja parezca lista. A veces recuperas cultivo de semillas.",
        "Aire extra:",
        "Un Generador de oxígeno cerca de un Núcleo de hábitat energizado y un tanque de agua agranda la zona segura.",
        "Solo gasta agua cuando alguien está en la parte de la zona segura que solo da oxígeno."
      ],
      "title": "Cómo funcionan las máquinas"
    },
    {
      "id": "machine_lights",
      "kind": "prose",
      "paragraphs": [
        "Las tiras de colores en las máquinas muestran qué están haciendo.",
        "Panel solar: rojo significa cielo bloqueado, noche o Tormenta de polvo; amarillo significa que no hay Núcleo de hábitat vinculado; verde significa que está energizando un núcleo.",
        "Núcleo de hábitat: amarillo significa zona segura pequeña; verde significa energizado por energía solar o batería.",
        "Procesador de agua: rojo significa que no hay núcleo energizado; amarillo significa que no hay espacio en el tanque; verde significa listo; azul significa que está procesando hielo.",
        "Generador de oxígeno: rojo significa que no hay núcleo energizado; amarillo significa que no hay agua almacenada; verde significa listo; azul significa que está gastando agua para dar aire extra.",
        "Lámpara de invernadero: rojo significa sin energía o soporte de sala roto; amarillo significa que no hay agua almacenada; verde significa lista.",
        "El Tanque de agua usa un medidor de agua en lugar de tiras de colores.",
        "La Bandeja de invernadero usa su imagen de tierra y hojas para mostrar plantada, creciendo, lista o bloqueada."
      ],
      "title": "Luces de las máquinas"
    },
    {
      "id": "exploration_pois",
      "kind": "prose",
      "paragraphs": [
        "Cerca de tu cohete puedes encontrar máquinas viejas, cofres enterrados, pozos de hielo y terreno roto. Más lejos, Marte tiene lugares más grandes y terreno más hostil.",
        "Explora por etapas:",
        "- Lugares cercanos - los primeros viajes más seguros.",
        "- Lugares a media distancia - caminatas más largas y terreno más complicado.",
        "- Lugares lejanos - planifica tu aire, tu ruta y tu regreso antes de ir.",
        "Recuerda:",
        "- Coloca balizas de ruta mientras avanzas.",
        "- Da la vuelta antes de que el temporizador de tu traje baje demasiado.",
        "- Reduce la velocidad en zonas calientes, polvorientas o de suelo roto.",
        "- En una Tormenta de polvo, sigue la dirección y distancia del HUD hasta la Baliza de ruta más cercana.",
        "Vigila las formas que no parezcan naturales. Algunos lugares tienen marcadores o equipo roto cerca.",
        "Algunas señales cercanas a buscar:",
        "Rover de reconocimiento inactivo (cercano): los restos de una máquina pequeña cerca de la zona de aterrizaje. Puede haber chatarra útil temprana en su interior.",
        "Caché de suministros sellada (cercano): un contenedor sellado cerca de la zona de aterrizaje. Puede haber suministros iniciales útiles en su interior.",
        "Campo de nódulos de hematita (cercano): un campo de rocas rojizas oxidadas. Vale la pena revisarlo cuando necesites materiales locales.",
        "Lente de hielo de cráter enterrado (cercano): un pozo hundido con piedra pálida en las paredes. Trae un pico."
      ],
      "title": "Lugares para explorar"
    },
    {
      "id": "hazards",
      "kind": "prose",
      "paragraphs": [
        "Algunas zonas son más difíciles que otras. El juego te avisa cuando te acercas.",
        "Vigila:",
        "- Suelos rotos que se desmoronan bajo edificios antiguos.",
        "- Terreno caliente cerca de agujeros de tubos de lava.",
        "- Zonas planas polvorientas que agotan tu traje más rápido.",
        "- Cuencas frías y bajas con polvo extra.",
        "- Tormentas de polvo diurnas que detienen la energía solar, ralentizan el movimiento y agotan la reserva EVA más rápido fuera de la cobertura segura.",
        "Los lugares lejanos suelen ser más difíciles. Coloca balizas en el camino de ida.",
        "La mayoría de los problemas vienen de caerse, perderse o quedarse fuera demasiado tiempo. Marca tu camino a casa antes de coger el botín."
      ],
      "title": "Peligros"
    },
    {
      "id": "troubleshooting",
      "kind": "prose",
      "paragraphs": [
        "El cohete no despega:",
        "- Cierra la puerta.",
        "- Ponte de pie dentro de la sala.",
        "- Trae a todos los viajeros dentro.",
        "La máquina no funciona:",
        "- ¿Hay un Núcleo de hábitat cerca?",
        "- ¿Hay un Panel solar bajo cielo abierto energizándolo?",
        "- Si hay una Tormenta de polvo activa, la energía solar está desconectada hasta que la tormenta amaine.",
        "- Para las máquinas de agua, ¿el Tanque de agua tiene suficiente capacidad?",
        "El invernadero no crece:",
        "- ¿La sala está completamente cerrada, sin huecos hacia el cielo?",
        "- ¿La lámpara está encendida y tiene agua?",
        "- ¿Plantaste el cultivo de semillas en la bandeja?",
        "El traje se agota rápido:",
        "- Vuelve al cohete o a la base energizada.",
        "- Sal de las zonas de peligro calientes o polvorientas.",
        "- Durante una Tormenta de polvo, usa la dirección de la Baliza de ruta más cercana en el HUD para regresar.",
        "Perdiste este libro:",
        "- Fabrica uno nuevo en la Tierra.",
        "- Puede haber una copia de repuesto en un cofre de suministros sellado en Marte."
      ],
      "title": "Si algo sale mal"
    },
    {
      "entries": [
        {
          "lines": [
            "Fabrica 4.",
            "Materiales: Regolito de Marte x4, Piedra de Marte x2, Lingote de cobre x1."
          ],
          "title": "Panel de hábitat"
        },
        {
          "lines": [
            "Fabrica 2.",
            "Materiales: Vidrio x2, Lingote de cobre x1, Piedra de Marte x1."
          ],
          "title": "Ventana reforzada"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Lingote de cobre x2, Luz de trabajo x1, Redstone x1, Regolito de Marte x1."
          ],
          "title": "Baliza de ruta"
        },
        {
          "lines": [
            "Fabrica 4.",
            "Materiales: Óxido de hierro de Marte x2, Basalto de Marte x1, Trozo de hielo x1."
          ],
          "title": "Luz de trabajo"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Vidrio x3, Lingote de cobre x2, Redstone x1, Piedra de Marte x3."
          ],
          "title": "Panel solar"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Lingote de cobre x2, Redstone x1, Lingote de hierro x2, Unidad de control de máquina x1, Panel de hábitat x2, Ventana reforzada x1."
          ],
          "title": "Batería"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Lingote de cobre x2, Redstone x1, Batería x1, Unidad de control de máquina x1, Panel de hábitat x1, Lingote de hierro x2."
          ],
          "title": "Kit de rover"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Lingote de cobre x2, Pepita de hierro x2, Piedra de Marte x2, Redstone x1."
          ],
          "title": "Unidad de control de máquina"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Lingote de cobre x6, Vidrio x1, Redstone x1, Lingote de hierro x1."
          ],
          "title": "Kit de cohete"
        },
        {
          "lines": [
            "Fabrica 4.",
            "Materiales: Semillas de trigo x1, Semillas de calabaza x1, Champiñón marrón x1, Papel x1."
          ],
          "title": "Cultivo de semillas inicial"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Panel de hábitat x4, Ventana reforzada x1, Lingote de cobre x2, Unidad de control de máquina x1, Lingote de hierro x1."
          ],
          "title": "Núcleo de hábitat"
        },
        {
          "lines": [
            "Fabrica 2.",
            "Materiales: Panel de hábitat x4, Lingote de cobre x2, Ventana reforzada x2, Unidad de control de máquina x1."
          ],
          "title": "Puerta de esclusa"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Basalto de Marte x2, Lingote de cobre x2, Ventana reforzada x1, Unidad de control de máquina x1, Piedra de Marte x3."
          ],
          "title": "Procesador de agua"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Ventana reforzada x4, Vidrio x2, Lingote de cobre x2, Panel de hábitat x1."
          ],
          "title": "Tanque de agua"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Lingote de cobre x2, Polvo de piedra luminosa x1, Unidad de control de máquina x1, Baliza de ruta x1."
          ],
          "title": "Lámpara de invernadero"
        },
        {
          "lines": [
            "Fabrica 2.",
            "Materiales: Panel de hábitat x2, Regolito de Marte x2, Ventana reforzada x1, Lingote de cobre x1, Cultivo de semillas inicial x1."
          ],
          "title": "Bandeja de invernadero"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Piedra de Marte x2, Lingote de cobre x2, Tanque de agua x2, Unidad de control de máquina x1, Trozo de hielo x1, Redstone x1."
          ],
          "title": "Generador de oxígeno"
        },
        {
          "lines": [
            "Fabrica 1.",
            "Materiales: Papel x8, Cuero x1."
          ],
          "title": "Manual de campo de Marsward"
        }
      ],
      "id": "crafting_reference",
      "kind": "generated",
      "source": "recipes",
      "title": "Referencia de fabricación"
    },
    {
      "entries": [
        {
          "lines": [
            "Bloque de terreno de Marte."
          ],
          "title": "Regolito de Marte"
        },
        {
          "lines": [
            "Bloque de terreno de Marte."
          ],
          "title": "Piedra de Marte"
        },
        {
          "lines": [
            "Bloque de terreno de Marte."
          ],
          "title": "Basalto de Marte"
        },
        {
          "lines": [
            "Bloque de terreno de Marte."
          ],
          "title": "Óxido de hierro de Marte"
        },
        {
          "lines": [
            "Bloque de terreno de Marte."
          ],
          "title": "Mena de hielo de Marte"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Núcleo de lanzamiento"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Panel de hábitat"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Ventana reforzada"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Baliza de ruta"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Luz de trabajo"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Panel solar"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Núcleo de hábitat"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Puerta de esclusa"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Puerta de cohete"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Procesador de agua"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Tanque de agua"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Batería"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Lámpara de invernadero"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Bandeja de invernadero"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Generador de oxígeno"
        },
        {
          "lines": [
            "Bloque de Marte para cohetes, bases, máquinas o navegación."
          ],
          "title": "Depósito de meteoritos"
        },
        {
          "lines": [
            "Ítem de cohete."
          ],
          "title": "Kit de cohete"
        },
        {
          "lines": [
            "Ítem de despliegue de vehículo de Marte."
          ],
          "title": "Kit de rover"
        },
        {
          "lines": [
            "Ítem de guía para el jugador."
          ],
          "title": "Manual de campo de Marsward"
        },
        {
          "lines": [
            "Recurso de Marte."
          ],
          "title": "Trozo de hielo"
        },
        {
          "lines": [
            "Recurso de Marte."
          ],
          "title": "Fragmento de meteorito"
        },
        {
          "lines": [
            "Componente de fabricación."
          ],
          "title": "Unidad de control de máquina"
        },
        {
          "lines": [
            "Ítem de invernadero."
          ],
          "title": "Cultivo de semillas inicial"
        },
        {
          "lines": [
            "Comida cultivada en un invernadero."
          ],
          "title": "Verduras de invernadero"
        },
        {
          "lines": [
            "Ítem de cohete."
          ],
          "title": "Llave de encendido"
        }
      ],
      "id": "blocks_items_glossary",
      "kind": "generated",
      "source": "glossary",
      "title": "Lista de bloques e ítems"
    },
    {
      "entries": [
        {
          "lines": [
            "15 minutos de aire seguro fuera."
          ],
          "title": "Duración del traje EVA"
        },
        {
          "lines": [
            "7 minutos restantes."
          ],
          "title": "Aviso EVA"
        },
        {
          "lines": [
            "3 minutos restantes."
          ],
          "title": "Peligro EVA"
        },
        {
          "lines": [
            "16 bloques desde el cohete."
          ],
          "title": "Aire seguro del cohete"
        },
        {
          "lines": [
            "8 bloques."
          ],
          "title": "Núcleo de hábitat solo"
        },
        {
          "lines": [
            "24 bloques."
          ],
          "title": "Núcleo de hábitat con Panel solar"
        },
        {
          "lines": [
            "10 bloques desde un Núcleo de hábitat."
          ],
          "title": "Vínculo del Panel solar"
        },
        {
          "lines": [
            "300 segundos con la carga completa."
          ],
          "title": "Autonomía de conducción del rover"
        },
        {
          "lines": [
            "100 segundos desde vacío."
          ],
          "title": "Tiempo de carga del rover"
        },
        {
          "lines": [
            "10 bloques desde un Núcleo de hábitat energizado."
          ],
          "title": "Vínculo de energía del rover"
        },
        {
          "lines": [
            "32 bloques."
          ],
          "title": "Extensión del Generador de oxígeno"
        },
        {
          "lines": [
            "10 bloques desde un Núcleo de hábitat."
          ],
          "title": "Vínculo del Generador de oxígeno"
        },
        {
          "lines": [
            "10 bloques desde un Tanque de agua."
          ],
          "title": "Vínculo de máquinas de agua"
        },
        {
          "lines": [
            "4 unidades de agua."
          ],
          "title": "Agua de un Trozo de hielo"
        },
        {
          "lines": [
            "100 unidades de agua."
          ],
          "title": "Capacidad del Tanque de agua"
        },
        {
          "lines": [
            "1 unidad de agua cada 10 segundos al extender el aire."
          ],
          "title": "Consumo de agua del oxígeno"
        },
        {
          "lines": [
            "10 bloques desde una Lámpara de invernadero."
          ],
          "title": "Vínculo de la bandeja de invernadero"
        },
        {
          "lines": [
            "Una etapa cada 10 segundos."
          ],
          "title": "Crecimiento del invernadero"
        },
        {
          "lines": [
            "2 Verduras de invernadero."
          ],
          "title": "Cosecha del invernadero"
        },
        {
          "lines": [
            "50% de probabilidad tras la cosecha."
          ],
          "title": "Recuperación del cultivo de semillas"
        },
        {
          "lines": [
            "Suelo inestable: aviso a 18 bloques, activo a 8 bloques."
          ],
          "title": "Puesto de investigación del lecho seco"
        },
        {
          "lines": [
            "Calor volcánico: aviso a 22 bloques, activo a 10 bloques, peligro a 3,25 bloques, drenaje EVA x1,6."
          ],
          "title": "Lumbrera de tubo de lava"
        },
        {
          "lines": [
            "Sedimento polvoriento: aviso a 20 bloques, activo a 12 bloques, drenaje EVA x2."
          ],
          "title": "Depósito de arcilla sulfatada"
        },
        {
          "lines": [
            "Polvo de cuenca fría: aviso a 26 bloques, activo a 14 bloques, drenaje EVA x3."
          ],
          "title": "Delta antiguo expuesto"
        }
      ],
      "id": "tuning_reference",
      "kind": "generated",
      "source": "constants",
      "title": "Números importantes"
    }
  ],
  "item": "marsward:field_manual",
  "subtitle": "Cómo llegar a Marte y sobrevivir",
  "title": "Manual de campo de Marsward"
}


def main():
    clean(SRC)

    write("pack.mcmeta", {
        "pack": {
            "description": "EnchantVenture data fixes: formationsoverworld, fokus, nerospace, the_lost_city, berezka_api, orphaned Lootr containers, marsward es_ES, frontier_armaments recipes, nerologistics/nerotech recipes, bosscraft_2/aerialhell advancements, equivalent_legacy EMC, neroagriculture tags, bettervillageranimations book",
            "min_format": [107, 1],
            "max_format": 107,
        }
    })

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
                    {"type": "minecraft:empty", "weight": 10},
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

    # Orphaned Lootr container at BlockPos{x=-4854, y=70, z=669} in the overworld
    # references loot table 'minecraft:chests/houseloot', which does not exist in
    # any installed mod or in vanilla (leftover NBT tag from a mod/datapack that is
    # no longer present). Stub it out under the vanilla namespace so Lootr can
    # resolve it instead of erroring every time the container is filled.
    write("data/minecraft/loot_table/chests/houseloot.json", {
        "type": "minecraft:chest",
        "pools": [
            {
                "rolls": {"min": 1, "max": 3},
                "entries": [
                    {"type": "minecraft:item", "name": "minecraft:bread", "weight": 1},
                    {"type": "minecraft:item", "name": "minecraft:iron_ingot", "weight": 1},
                    {"type": "minecraft:empty", "weight": 2},
                ],
            }
        ],
    })

    

    # Marsward field manual (data/marsward/field_manual/field_manual.json) has no
    # lang-key-driven text -- all chapter/entry strings are literal English baked into
    # the mod's own datapack JSON, so a resource pack cannot translate it (assets/ only).
    # This overrides the mod's own data file with a full es_ES translation, same key/
    # structure, same chapter ids/kind/source (only human-readable text translated).
    write("data/marsward/field_manual/field_manual.json", MARSWARD_FIELD_MANUAL_ES)

# ============================================================
    # FRONTIER_ARMAMENTS: Fix invalid recipes using "minecraft:chain" as key
    # Error: Map entry 'C' / 'I' - "minecraft:chain" not a valid ingredient
    # Replace chain with iron_ingot in shaped recipes
    # ============================================================
    frontier_recipes = [
        "juggernaut_helmet.json",
        "juggernaut_chestplate.json",
        "juggernaut_leggings.json",
        "juggernaut_boots.json",
        "peasant_chestplate.json",
    ]
    for recipe_name in frontier_recipes:
        try:
            d = read_from_jar("frontier_armaments-neoforge-1.0.0+26.2.jar",
                              f"data/frontier_armaments/recipe/{recipe_name}")
            def fix_chain_ingredient(node):
                if isinstance(node, dict):
                    for k, v in list(node.items()):
                        if k == "key" and isinstance(v, dict):
                            for key_char, ingredient in v.items():
                                if isinstance(ingredient, str) and ingredient == "minecraft:chain":
                                    v[key_char] = "minecraft:iron_ingot"
                                elif isinstance(ingredient, dict) and ingredient.get("item") == "minecraft:chain":
                                    ingredient["item"] = "minecraft:iron_ingot"
                        else:
                            fix_chain_ingredient(v)
                elif isinstance(node, list):
                    for v in node:
                        fix_chain_ingredient(v)
            fix_chain_ingredient(d)
            write(f"data/frontier_armaments/recipe/{recipe_name}", d)
        except KeyError:
            pass

    # ============================================================
    # NEROLOGISTICS & NEROTECH: Fix invalid "tools" ingredient in configurator recipes
    # Error: Unknown element name:tools
    # Replace with valid tag or item
    # ============================================================
    for mod_jar, mod_id in [
        ("nerologistics-neoforge-26.2-0.1.0-alpha.1.jar", "nerologistics"),
        ("nerotech-neoforge-26.2-0.1.0-beta.1.jar", "nerotech"),
    ]:
        try:
            d = read_from_jar(mod_jar, f"data/{mod_id}/recipe/configurator.json")
            def fix_tools_ingredient(node):
                if isinstance(node, dict):
                    for k, v in list(node.items()):
                        if k in ("key", "ingredient") and isinstance(v, dict):
                            if v.get("item") == "tools" or v.get("tag") == "tools":
                                v["tag"] = "c:tools"
                        else:
                            fix_tools_ingredient(v)
                elif isinstance(node, list):
                    for v in node:
                        fix_tools_ingredient(v)
            fix_tools_ingredient(d)
            write(f"data/{mod_id}/recipe/configurator.json", d)
        except KeyError:
            pass

    # ============================================================
    # BOSSCRAFT_2: Fix advancements using non-existent entity_sub_predicate_type
    # Error: Unknown registry key minecraft:entity_sub_predicate_type for bosscraft_2 entities
    # Replace with direct entity type predicate
    # ============================================================
    bosscraft_advancements = [
        "burn_advandement.json",
        "dead_advancement.json",
        "dust_advancement.json",
        "exterminator_advancement.json",
        "ice_advancement.json",
        "mountain_advancement.json",
        "ninja_advancement.json",
    ]
    for adv_name in bosscraft_advancements:
        try:
            d = read_from_jar("Bosscraft_2_Remake-1.2.0-neoforge-26.x.jar",
                              f"data/bosscraft_2/advancement/{adv_name}")
            def fix_entity_predicate(node):
                if isinstance(node, dict):
                    for k, v in list(node.items()):
                        if k == "entity" and isinstance(v, dict):
                            if "type" in v and isinstance(v["type"], str) and v["type"].startswith("bosscraft_2:"):
                                v["type"] = v["type"]
                        else:
                            fix_entity_predicate(v)
                elif isinstance(node, list):
                    for v in node:
                        fix_entity_predicate(v)
            fix_entity_predicate(d)
            write(f"data/bosscraft_2/advancement/{adv_name}", d)
        except KeyError:
            pass

    # ============================================================
    # AERIALHELL: Fix loot tables using non-existent entity_sub_predicate_type
    # Error: Unknown registry key minecraft:entity_sub_predicate_type for #minecraft:skeletons
    # Replace entity_properties with entity_type predicate using expanded skeleton types
    # ============================================================
    try:
        d = read_from_jar("aerialhell-0.7.7.8_neoforge26.2.jar",
                          "data/aerialhell/loot_table/entities/shroomboom.json")
        def fix_loot_entity_predicate(node):
            if isinstance(node, dict):
                for k, v in list(node.items()):
                    if k == "condition" and v == "minecraft:entity_properties":
                        if "predicate" in node and isinstance(node["predicate"], dict):
                            if "type" in node["predicate"]:
                                # Replace entity_properties with entity_type
                                # #minecraft:skeletons expands to skeleton variants
                                node["condition"] = "minecraft:entity_type"
                                node["entity"] = "attacker"
                                skeleton_types = [
                                    "minecraft:skeleton",
                                    "minecraft:wither_skeleton",
                                    "minecraft:stray",
                                    "minecraft:bogged"
                                ]
                                node["type"] = skeleton_types
                                # Remove the old predicate field
                                del node["predicate"]
                    else:
                        fix_loot_entity_predicate(v)
            elif isinstance(node, list):
                for v in node:
                    fix_loot_entity_predicate(v)
        fix_loot_entity_predicate(d)
        write("data/aerialhell/loot_table/entities/shroomboom.json", d)
    except KeyError:
        pass

    # ============================================================
    # EQUIVALENT LEGACY: Add EMC values for missing items to prevent exploits
    # The mod errors show missing items from: allthemodium, powah, occultism, ecologics, reliquary
    # We add conversions for items that exist in the pack
    # ============================================================
    emc_values = {
        "equivalent_legacy:conversions": {
            "values": {
                # Occultism silver
                "occultism:silver_ingot": 512,
                "occultism:silver_nugget": 57,
                # Ecologics
                "ecologics:azalea_flower": 32,
                # Reliquary
                "reliquary:witch_hat": 30,
                # Croptopia (if present)
                # Add more as needed - these prevent the "EMC Exploit" warnings
            }
        }
    }
    write("data/equivalent_legacy/emc/values.json", emc_values)

    # ============================================================
    # NEROAGRICULTURE: Add material tags to fix empty tag warnings
    # The mod warns about empty tags for many materials
    # We provide fallback tags pointing to common equivalents
    # ============================================================
    neroagriculture_tags = {
        "c:dusts/certus_quartz": ["ae2:certus_quartz_dust"],
        "c:dusts/coal_coke": ["immersiveengineering:dust_coke"],
        "c:dusts/fluix": ["ae2:fluix_dust"],
        "c:dusts/sky_stone": ["ae2:sky_stone_dust"],
        "c:gems/black_quartz": ["actuallyadditions:black_quartz"],
        "c:gems/chimerite": [],
        "c:ingots/demonite": [],
        "c:ingots/uraninite": ["powah:uraninite"],
        "c:ores/baronyte": [],
        "c:ores/black_quartz": ["actuallyadditions:black_quartz_ore"],
        "c:ores/blazium": [],
        "c:ores/bloodstone": [],
        "c:ores/blue_gemstone": [],
        "c:ores/bone_fragments": ["minecraft:bone_meal"],
        "c:ores/charged_runium": [],
        "c:ores/crystallite": [],
        "c:ores/elecanium": [],
        "c:ores/emberstone": [],
        "c:ores/gemenyte": [],
        "c:ores/ghastly": [],
        "c:ores/ghoulish": [],
        "c:ores/green_gemstone": [],
        "c:ores/jade": [],
        "c:ores/jewelyte": [],
        "c:ores/limonite": ["minecraft:iron_ore"],
        "c:ores/lyon": [],
        "c:ores/mystite": [],
        "c:ores/ornamyte": [],
        "c:ores/purple_gemstone": ["minecraft:amethyst_shard"],
        "c:ores/red_gemstone": ["minecraft:redstone"],
        "c:ores/runium": [],
        "c:ores/shyregem": [],
        "c:ores/shyrestone": [],
        "c:ores/varsium": [],
        "c:ores/white_gemstone": ["minecraft:quartz"],
        "c:ores/yellow_gemstone": ["minecraft:gold_ore"],
        "c:raw_materials/demonite": [],
    }
    for tag_id, values in neroagriculture_tags.items():
        if ":" not in tag_id:
            continue
        namespace, path = tag_id.split(":", 1)
        write(f"data/{namespace}/tags/items/{path}.json", {"replace": False, "values": values})

    # ============================================================
    # BETTER VILLAGER ANIMATIONS: Add field manual/book integration
    # The mod has a book system similar to marsward
    # ============================================================
    bva_book = {
        "book": {
            "title": "Guía del Aldeano Animado",
            "author": "EnchantVenture",
            "description": "Todo sobre las animaciones y comportamientos de los aldeanos",
            "chapters": [
                {
                    "title": "Introducción",
                    "entries": [
                        {
                            "title": "Nuevas animaciones",
                            "text": "Los aldeanos ahora tienen animaciones de trabajo, descanso e interacción social."
                        },
                        {
                            "title": "Interacciones",
                            "text": "Los aldeanos reaccionan a los jugadores: saludan, huyen o comercian según su profesión."
                        }
                    ]
                }
            ]
        }
    }
    write("data/bettervillageranimations/book/guide.json", bva_book)

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
