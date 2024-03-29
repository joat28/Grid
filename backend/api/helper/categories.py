from flask import jsonify
import json

category = dict()

men = [
        "sportshoes",
        "casualshoes",
        "formalshoes",
        "sandals",
        "flip-flops",
        "loafers",
        "boots",
        "shoes",
        "sneakers",
        "deodrants",
        "perfume",
        "grooming",
        "beardcare",
        "shaving",
        "aftershave",
        "tshirt",
        "formalshirt",
        "casualshirt",
        "jeans",
        "casualtrouser",
        "formaltrouser",
        "trouser",
        "trackpant",
        "shorts",
        "cargos",
        "suits",
        "blazers",
        "waistcoats",
        "ties",
        "socks",
        "caps",
        "sweatshirts",
        "jackets",
        "sweaters",
        "tracksuit",
        "kurtas",
        "ethnicwear",
        "sherwani",
        "ethnicpyjama",
        "dhoti",
        "lungi",
        "vests",
        "boxers",
        "pyjamas",
        "thermals",
        "nightsuits",
        "raincoats",
        "fastrack",
        "watches",
        "casio",
        "titan",
        "fossil",
        "sonata",
        "wallets",
        "belts",
        "sunglass",
        "jewellery",
        "trimmers",
        "haircare",
        "beardo"
        ]
women = [
        "saree",
        "sandal",
        "kurtas & kurtis",
        "flats",
        "topwear",
        "hair care",
        "lehenga choli",
        "wedges",
        "jeans",
        "deodorants",
        "perfumes",
        "blouse",
        "shoes",
        "shorts",
        "kurta sets",
        "salwar",
        "jewellery",
        "skirt",
        "gowns",
        "jeggings",
        "tights",
        "trousers",
        "capris",
        "boots",
        "ballerina",
        "lingerie",
        "sleepwear",
        "legging",
        "churidar",
        "slipper",
        "flip-flop",
        "palazzo",
        "panties",
        "watch",
        "sharara",
        "handbag",
        "salwar",
        "patiala",
        "nightie",
        "tote",
        "camisole",
        "petticoat",
        "beachwear",
        "epilators",
        "designer saree",
        "sunglass",
        "wallet"
    ]
kids = [
            'boys tshirts',
            'boys ethnicwear',
            'boys shorts',
            'boys shirts',
            'boys innerwear',
            'boys sandals',
            'boys sport shoes',
            'boys sweatshirts',
            'boys jackets',
            'boys watches',
            'boys sunglasses',
            'boys baby-combo-sets',
            'boys baby-tshirts',
            'boys baby-innerwear',
            'boys sweatshirts',
            'boys jackets',
            'girls dresses & skirts',
            'girls ethnic wear',
            'girls t-shirts & tops',
            'girls innerwear',
            'girls baby-combo-sets',
            'girls baby-dresses & gowns',
            'girls baby-innerwear',
            'girls flats & bellies',
            'girls sportshoes',
            'girls sweatshirts',
            'girls jackets',
            'watches',
            'sunglasses',
            'infant innerwear',
            'thermals',
    ]


category['men'] = men
category['women'] = women
category['kids']  = kids

def get_categories():
    return category
