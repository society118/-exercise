import pytest
from rpg import Mage,Knight,Character

def test_health_and_mana():
    k =Knight("Арториас",100,40,50)
    k.health =-10
    k.mana = -5
    assert k.health == 0
    assert k.mana == 0

def test_eq_characters():
    k1 =Knight("Hero",100,30,50)
    m2 = Mage("Hero",100,80,20)
    assert  k1 == m2

def test_knight_test():
    k =Knight("Knight",100,50,60)
    m =Mage("Mage",100,90,30)
    k.attack(m)
    assert  m.health == 80

def test_mage_attack_with_mana():
    m =Mage("Mage",100,50,30)
    k =Knight("Knight",100,40,60)
    k.attack(k)
    assert k.health == 85
    assert m.health == 40

def test_mage_attack_with_no_mana():
    m =Mage("Mage",100,50,30)
    k=Knight("Knight",100,40,60)
    assert k.health == 100
    assert m.mana == 100

def test_static_description():
    assert Character.get_base_description() =="это персонаж в RPG мире "




