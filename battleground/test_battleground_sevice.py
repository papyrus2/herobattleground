import unittest
from copy import deepcopy

from mock import patch
from nose.plugins.attrib import attr

from battleground.battleground_service import BattlegroundService
from protos.python.battleground_pb2 import BattlegroundResponse, BattlegroundRequest, BattleLog
from protos.python.character_pb2 import HUMAN, BEAST, DEFENCE, ATTACK, Character


@attr('unit')
class TestBattlegroundService(unittest.TestCase):

    @patch("battleground.battleground_service.BattlegroundService.roll_chance", autospec=True)
    def test_round_attack_success(self, mock_roll_chance):
        """ Test that an attack is ended with success and the defender lose health. """
        mock_roll_chance.return_value = False

        attacker = self.generate_character(HUMAN)
        defender = self.generate_character(BEAST)

        original_defender = deepcopy(defender)
        damage = attacker.strength - defender.defence
        original_defender.health = original_defender.health - damage
        expected_log = BattleLog(
            attacker=attacker, defender=defender, damage=damage, defence_health=original_defender.health
        )

        bs = BattlegroundService()
        log = bs.round(attacker, defender)

        self.assertEqual(original_defender, defender, "Defender health should have changed.")
        self.assertEqual(log, expected_log, "Different BattleLogs received")

    @patch("battleground.battleground_service.BattlegroundService.roll_chance", autospec=True)
    def test_round_defence_success(self, mock_roll_chance):
        """ Test that an attack is ended with success and the defender lose health. """
        mock_roll_chance.return_value = True

        attacker = self.generate_character(HUMAN)
        defender = self.generate_character(BEAST)

        original_defender = deepcopy(defender)

        bs = BattlegroundService()
        bs.round(attacker, defender)

        self.assertEqual(original_defender, defender, "Defenders health shouldn't have changed.")

    @patch("battleground.battleground_service.BattlegroundService.roll_chance", autospec=True)
    def test_round_attack_skill_success(self, mock_roll_chance):
        """ Test that an attack is ended with success and the defender lose health. """
        mock_roll_chance.side_effect = [False, True]

        attacker = self.generate_character(HUMAN)
        defender = self.generate_character(BEAST)

        original_defender = deepcopy(defender)
        damage = attacker.strength - defender.defence
        original_defender.health -= damage * 2

        bs = BattlegroundService()
        bs.round(attacker, defender)

        self.assertEqual(original_defender, defender, "Defender health should have changed.")

    @patch("battleground.battleground_service.BattlegroundService.roll_chance", autospec=True)
    def test_round_defence_skill_success(self, mock_roll_chance):
        """ Test that less damage is takes when defence skill is activated. """
        mock_roll_chance.side_effect = [False, True, False]

        attacker = self.generate_character(BEAST)
        defender = self.generate_character(HUMAN)

        original_defender = deepcopy(defender)
        original_defender.health = original_defender.health - int((attacker.strength - defender.defence) / 2)

        bs = BattlegroundService()
        bs.round(attacker, defender)

        self.assertEqual(original_defender, defender, "Defender health should have changed.")

    @patch("battleground.battleground_service.BattlegroundService.roll_chance", autospec=True)
    def test_fighting_no_luck(self, mock_roll_chance):
        """ Test fighting method with no luck. """
        mock_roll_chance.return_value = False

        attacker = self.generate_character(HUMAN)
        defender = self.generate_character(BEAST)

        expected_winner = deepcopy(attacker)
        expected_winner.health = 25
        bs = BattlegroundService()

        result = bs.Fighting(BattlegroundRequest(first_player=attacker, second_player=defender), None)

        # when there is no luck the HUMAN always wins with Health left at 25
        self.assertEqual(expected_winner, result.winner, "Unexpected winner of the fight")

    def generate_character(self, character_type):
        """ Generate a fix type of characters. """
        character_dict = {
            HUMAN: {
                'health': 70,
                'strength': 70,
                'defence': 45,
                'speed': 40,
                'chance': 10,
                'skills': [
                    {
                        'name': 'Rapid strike',
                        'chance': 10,
                        'skill_type': ATTACK,
                        'power': 2
                    }, {
                        'name': 'Magic shield',
                        'chance': 20,
                        'skill_type': DEFENCE,
                        'power': 2
                    }
                ]
            },
            BEAST: {
                'health': 60,
                'strength': 60,
                'defence': 40,
                'speed': 40,
                'chance': 25
            }
        }
        return Character(**character_dict[character_type])


if __name__ == '__main__':
    unittest.main()
