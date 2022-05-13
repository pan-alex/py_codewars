# Description
#
# You are Saitama (a.k.a One Punch Man), and you are fighting against the monsters! You are strong enough to kill them with one punch, but after you punch 3 times, one of the remaining monsters will hit you once.
#
# Your health is health; number of monsters is monsters, damage that monster can give you is damage.
# Task
#
# Write a function that will calculate:
#
# how many hits you received, how much damage you received and your remaining health.
#
# if your health is <= 0, you die and function should return "hero died".
# Examples
#
# killMonsters(100, 3, 33); // => "hits: 0, damage: 0, health: 100"
# killMonsters(50, 7, 10); // => "hits: 2, damage: 20, health: 30"
#
# Note
#
# All numbers are strictly positive. Your function should always return a string.
#
# Have fun :)

def kill_monsters(health, monsters, damage):
    hits = (monsters - 1) // 3

    health = health - (hits * damage)

    if health <= 0:
        return 'hero died'
    else:
        return f'hits: {hits}, damage: {hits * damage}, health: {health}'