from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShoot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator():
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if (isinstance(ent, Enemy)):
            if ent.rect.right < 0:
                ent.health = 0

        if (isinstance(ent, PlayerShot)):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

        if (isinstance(ent, EnemyShoot)):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        vallid_collision = False
        if (isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot)):
            vallid_collision = True

        elif (isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy)):
            vallid_collision = True

        elif (isinstance(ent1, Player) and isinstance(ent2, EnemyShoot)):
            vallid_collision = True

        elif (isinstance(ent1, EnemyShoot) and isinstance(ent2, PlayerShot)):
            vallid_collision = True

        if vallid_collision:
            if (ent1.rect.right >= ent2.rect.left
                    and ent1.rect.left <= ent2.rect.right
                    and ent1.rect.bottom >= ent2.rect.top
                    and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for entity in entity_list:
                if entity.name == 'Player1':
                    entity.score += enemy.score

        elif enemy.last_dmg == 'Player2Shot':
            for entity in entity_list:
                if entity.name == 'Player2':
                    entity.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)

            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
