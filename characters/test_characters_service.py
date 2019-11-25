import unittest
from mock import patch

from nose.plugins.attrib import attr
from characters.characters_attributes import characters_attributes
from characters.helpers import generate_character
from protos.python.character_pb2 import HUMAN, BEAST, Character


@attr('unit')
class TestCharactersService(unittest.TestCase):

    @patch("random.randint", autospec=True)
    def test_generate_character_human(self, mock_randint):
        """Check that generating a human character has all the expcted attributes. """
        mock_randint.return_value = 0
        result_character = generate_character(HUMAN)
        expecter_character_dict = characters_attributes[HUMAN]['base_stats']
        expecter_character_dict['skills'] = characters_attributes[HUMAN]['skills']

        self.assertEqual(result_character, Character(**expecter_character_dict), "Unexpected character was generated.")


if __name__ == '__main__':
    unittest.main()
