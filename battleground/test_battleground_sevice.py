import unittest
from copy import deepcopy

from mock import patch
from nose.plugins.attrib import attr

from battleground.battleground_service import BattlegroundService
from characters.helpers import generate_character
from protos.python.character_pb2 import HUMAN, BEAST


@attr('unit')
class TestBattlegroundService(unittest.TestCase):

    @patch("battleground.battleground_service.BattlegroundService.roll_chance", autospec=True)
    def test_round_attack_success(self, mock_roll_chance):
        """ Test that an attack is ended with success and the defender lose health. """
        mock_roll_chance.return_value = False

        attacker = generate_character(HUMAN)
        defencer = generate_character(BEAST)

        original_defencer = deepcopy(defencer)
        original_defencer.health = original_defencer.health - (attacker.strength - defencer.defence)

        bs = BattlegroundService()
        bs.round(attacker, defencer)

        self.assertEqual(original_defencer, defencer, "Defender health should have changed.")

    @patch("battleground.battleground_service.BattlegroundService.roll_chance", autospec=True)
    def test_round_defence_success(self, mock_roll_chance):
        """ Test that an attack is ended with success and the defender lose health. """
        mock_roll_chance.return_value = True

        attacker = generate_character(HUMAN)
        defencer = generate_character(BEAST)

        original_defencer = deepcopy(defencer)

        bs = BattlegroundService()
        bs.round(attacker, defencer)

        self.assertEqual(original_defencer, defencer, "Defenders health shouldn't have changed.")

    @patch("battleground.battleground_service.BattlegroundService.roll_chance", autospec=True)
    def test_round_defence_skill_success(self, mock_roll_chance):
        """ Test that less damage is takes when defence skill is activated. """
        mock_roll_chance.side_effect = [False, True]

        attacker = generate_character(BEAST)
        defencer = generate_character(HUMAN)

        original_defencer = deepcopy(defencer)
        original_defencer.health = original_defencer.health - int((attacker.strength - defencer.defence) / 2)

        bs = BattlegroundService()
        bs.round(attacker, defencer)

        self.assertEqual(original_defencer, defencer, "Defender health should have changed.")


if __name__ == '__main__':
    unittest.main()
