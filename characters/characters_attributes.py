from protos.python import character_pb2

# A list ok defined skills of characters in battleground.
skills = {
    'Rapid strike': {
        'name': 'Rapid strike',
        'chance': 10,
        'skill_type': character_pb2.ATTACK,
        'power': 2
    },
    'Magic shield': {
        'name': 'Magic shield',
        'chance': 20,
        'skill_type': character_pb2.DEFENCE,
        'power': 2
    },
}

# Character attrbiutes describes the character attributes.
# Each type of battleground characters will have a 'base_stats' dictionary,
# an additional_stats and a list of skills.
characters_attributes = {
    character_pb2.HUMAN: {
        'base_stats': {
            'health': 70,
            'strength': 70,
            'defence': 45,
            'speed': 40,
            'chance': 10
        },
        'additional_stats': {
            'health': 30,
            'strength': 10,
            'defence': 5,
            'speed': 10,
            'chance': 20
        },
        'skills': [skills['Rapid strike'], skills['Magic shield']]
    },
    character_pb2.BEAST: {
        'base_stats': {
            'health': 60,
            'strength': 60,
            'defence': 40,
            'speed': 40,
            'chance': 25
        },
        'additional_stats': {
            'health': 30,
            'strength': 30,
            'defence': 20,
            'speed': 20,
            'chance': 15
        }
    }
}
