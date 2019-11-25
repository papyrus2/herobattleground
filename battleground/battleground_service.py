from concurrent import futures
import random

import grpc
from protos.python.battleground_pb2_grpc import (BattlegroundServiceServicer, add_BattlegroundServiceServicer_to_server)
from protos.python import character_pb2, battleground_pb2
from characters.helpers import generate_character


class BattlegroundService(BattlegroundServiceServicer):
    """ Battleground Service will handle all the fighting mechanism. """

    def decide_playing_order(self, first_player, second_player):
        """ Decide the what player will be first to attack. 
        The player order will be decided based on the speed and chance
        """
        if first_player.speed > second_player.speed:
            return first_player, second_player
        elif first_player.speed == second_player.speed:
            if first_player.chance > second_player.chance:
                return first_player, second_player
        return second_player, first_player

    def compute_damage(self, attacker, defender):
        """ Compute the damage done by the attacker. """
        return attacker.strength - defender.defence

    def roll_chance(self, chance):
        """ See if the player lucky strike. """
        roll = random.randint(0, 100)
        return roll <= chance

    def round(self, attacker, defender):
        """ Play a round in the battleground, attack and defence try their lucks 
        and skills. """
        log = battleground_pb2.BattleLog(attacker=attacker, defender=defender, skills=[])

        damage = self.compute_damage(attacker, defender)
        defence_chance = self.roll_chance(defender.chance)

        if defence_chance:
            # no damage done
            log.damage = 0
            log.defence_health = defender.health
            return log

        skill = self.use_skill(defender.skills, character_pb2.DEFENCE)
        if skill:
            # append skill to the log
            log.skills.append(skill)
            damage = int(damage / skill.power)

        skill = self.use_skill(attacker.skills, character_pb2.ATTACK)
        if skill:
            # append skill to the log
            log.skills.append(skill)
            damage += int(damage * (skill.power - 1))

        # Damage done
        defender.health -= damage
        log.damage += damage
        log.defence_health = defender.health

        return log

    def use_skill(self, skills, skill_type):
        """ Get skill of the skill_type from the available skills. """
        for skill in skills:
            if skill.skill_type == skill_type:
                if self.roll_chance(skill.chance):
                    return skill
        return None

        # chance to defance

    def Fighting(self, request, context):
        """ The battleground winner will be decided in a legendery fight.

        The defense and attack will be computed here and the battle will 
        be done over a duration of 20 rounds or until one of the players is dead.
        """
        attacker = request.first_player
        defender = request.second_player

        attacker, defender = self.decide_playing_order(attacker, defender)

        winner = attacker
        battle_log = []
        for _ in range(20):
            log = self.round(attacker, defender)
            battle_log.append(log)
            if defender.health < 0:
                winner = attacker
                break

            attacker, defender = defender, attacker

        return battleground_pb2.BattlegroundResponse(winner=winner, battle_log=battle_log)


def serve():
    """ Starting the service and listen on a specific port for incoming 
    requests. """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BattlegroundServiceServicer_to_server(BattlegroundService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
