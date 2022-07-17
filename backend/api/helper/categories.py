from flask import jsonify
import json

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
       if isinstance(obj, set):
          return list(obj)
       return json.JSONEncoder.default(self, obj)

category = {
    'men' : 
        [
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
    ,
    'women' : []
    ,
    'kids' : []
    
}


def get_categories():
    return json.dumps(category, indent=4)
