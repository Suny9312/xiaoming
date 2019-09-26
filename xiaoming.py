class character:

    def __init__(self, hp, atk, speed, shield, name):
        if(speed <= 0):
            speed = 65536;
        self.m_hp = hp;
        self.m_atk = atk;
        self.m_speed = speed;
        self.m_shield = shield;
        self.m_name = name;

    def attack(self, character):
        character.m_hp = character.m_hp - (max(0, self.m_atk - character.m_shield));
        print(self.m_name + ' attack ' + character.m_name + '!\n');
        print(character.m_name + ' hp = ' + (str)(character.m_hp) + '\n');
        if(character.death()):
            print(character.m_name + ' dead!\n');
            
    def alive(self):
        return self.m_hp > 0

    def death(self):
        return self.m_hp <= 0;

if __name__ == "__main__":

    player = character(500, 10, 0.8, 0, 'xiaoming');
    monster1 = character(110, 5, 2, 0, 'monster1');
    monster2 = character(110, 5, 2, 0, 'monster2');
    monster3 = character(110, 5, 2, 0, 'monster3');
    monster4 = character(110, 5, 2, 0, 'monster4');
    monster5 = character(110, 5, 2, 0, 'monster5');
    monster6 = character(110, 5, 2, 0, 'monster6');
    monsters = [monster1, monster2, monster3, monster4, monster5, monster6];
    a = 0;
    while(player.alive()):
        if len(monsters) > 0:
            if(a % (player.m_speed * 10) == 0):
                player.attack(monsters[0]);
        else:
            break;
        for monster in monsters:
            if(a % (monster.m_speed * 10) == 0):
                monster.attack(player);
                if(player.death()):
                    break;
        for monster in monsters:
            if(monster.death()):
                monsters.remove(monster);
                print(monster.m_name + ' out!\n');
        a += 1;
    if(player.alive()):
        print(player.m_name + ' win');

