from copy import deepcopy

import unittest
from mock import patch

from nose.plugins.attrib import attr
from characters.characters_attributes import characters_attributes
from characters.helpers import generate_character
from protos.python.character_pb2 import HUMAN, BEAST, Character, CharacterRequest, CharacterResponse
from characters.characters_service import CharacterService


@attr('unit')
class TestCharactersService(unittest.TestCase):

    @patch("random.randint", autospec=True)
    def test_generate_character_human(self, mock_randint):
        """ Check that generating a human character has all the expcted attributes. """
        mock_randint.return_value = 0
        result_character = generate_character(HUMAN)

        # create expected character
        human_attribute = deepcopy(characters_attributes[HUMAN])
        expecter_character_dict = human_attribute['base_stats']
        expecter_character_dict['skills'] = human_attribute['skills']
        expecter_character_dict['name'] = human_attribute['name']

        self.assertEqual(result_character, Character(**expecter_character_dict), "Unexpected character was generated.")

    @patch("random.randint", autospec=True)
    def test_generate_character_beast(self, mock_randint):
        """ Check that generating a beast character has all the expcted attributes. """
        mock_randint.return_value = 0
        result_character = generate_character(BEAST)

        beast_attribute = deepcopy(characters_attributes[BEAST])
        expecter_character_dict = beast_attribute['base_stats']
        expecter_character_dict['name'] = beast_attribute['name']

        self.assertEqual(result_character, Character(**expecter_character_dict), "Unexpected character was generated.")

    @patch("random.randint", autospec=True)
    def test_get_character_service(self, mock_randint):
        """ Test that get method works as expected. """
        mock_randint.return_value = 0
        service = CharacterService()
        result = service.Get(CharacterRequest(character_type=BEAST), None)

        beast_attribute = deepcopy(characters_attributes[BEAST])
        expecter_character_dict = beast_attribute['base_stats']
        expecter_character_dict['name'] = beast_attribute['name']
        expecter_result = CharacterResponse(character=Character(**expecter_character_dict))
        self.assertEqual(result, expecter_result, "Get method retuned a different result.")


if __name__ == '__main__':
    unittest.main()
