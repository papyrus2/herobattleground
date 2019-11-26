import random

from characters.characters_attributes import characters_attributes
from protos.python import character_pb2


def generate_character(character_type):
    """Based on defined character attributes generate a new character."""
    character_dict = {}

    attributes = characters_attributes.get(character_type, {})
    base_stats = attributes.get('base_stats', {})
    additional_stats = attributes.get('additional_stats', {})
    skills = attributes.get('skills', [])

    for stats in base_stats:
        additional_value = random.randint(0, additional_stats[stats])
        character_dict[stats] = base_stats[stats] + additional_value

    if skills:
        character_dict['skills'] = skills

    character_dict['name'] = attributes['name']

    return character_pb2.Character(**character_dict)
