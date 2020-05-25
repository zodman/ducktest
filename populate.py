import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
import django
from django.conf import settings

django.setup()
from django_seed import Seed
from ducks.models import DuckType, FoodType
from django.contrib.auth.models import User


def initial_ducks():
    duck_types = [
        "mallard",
        "canvasback",
        "marble",
        "black-belled whisting ",
        "domestic",
        "spotted whistling",
        "West Indian whistling",
        "Plumed whistling",
        "african ",
        "alabio ",
        "allier ",
        "american pekinancona ",
        "antigua and barbuda ",
        "australian callaustralian spottedaylesbury ",
        "bac kinh ",
        "bali ",
        "barbary ",
        "bashkir ",
        "bau ",
        "black east indian ",
        "blekinge ",
        "blue swedishbourbourg ",
        "buff ",
        "call ",
        "campbell ",
        "cayuga ",
        "challans ",
        "chara chamble ",
        "crested ",
        "danish ",
        "dendermond ",
        "deshi blackdeshi whiteduclair ",
        "dutch hookbilleast indies ",
        "elizabeth ",
        "estaires ",
        "faroese ",
        "forest ",
        "german pekingermanata venetagimbsheimer ",
        "golden cascadegressingham ",
        "grimao erma&#xf4;shaut-volant ",
        "havanna ",
        "herve ",
        "hook billhungarian ",
        "huttegem ",
        "idegem ",
        "indian runner ",
        "japanice criollojendingkaiya ",
        "khaki campbelllaplaignemagpie ",
        "merchtem ",
        "mulardmuscovy ",
        "orpington ",
        "overberg ",
        "pomeranian ",
        "rouen ",
        "saxony ",
        "semois ",
        "shetland ",
        "silver appleyard ",
        "silver appleyard miniaturesilver bantamswedish blueswedish yellow ",
        "tea ankamtea kapatermonde ",
        "tsaiya ",
        "ukrainian clay ",
        "ukrainian grey ",
        "ukrainian white ",
        "svenetian ",
        "vouill&#xe9; ",
        "watervale ",
        "welsh harlequin ",
        "west indian ",
        "white-breasted black ",
        "others",
    ]
    for i in set(duck_types):
        DuckType.objects.get_or_create(name=f"{i.capitalize()} Duck")

    duck_eats = [
        "Small fish",
        "fish eggs",
        "Snails",
        "worms",
        "slugs",
        "mollusks",
        "Small crustaceans",
        "crayfish",
        "Grass",
        "leaves",
        "weeds",
        "aquatic plants",
        "roots",
        "Frogs",
        "tadpoles",
        "salamanders" "insects",
        "Seeds",
        "grain",
        "bread",
        "Cracked Corn",
        "bugs",
        "Fruits",
        "Vegetables",
        "Mix",
        "others",
    ]
    for i in set(duck_eats):
        FoodType.objects.get_or_create(name=i.capitalize())


def initial_users():
    User.objects.create_superuser("admin", "admin@example.com", "admin")


def main():
    initial_ducks()
    initial_users()


if __name__ == "__main__":
    main()
