# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#=====Part 1===================================================================
player_scored_0 = 'Ruud Gullit'
goal_0 = 32
player_scored_1 = 'Marco van Basten'
goal_1 = 54
scorers = player_scored_0 + " " + str(goal_0) + ", " + player_scored_1 + " " + str(goal_1)
print(scorers)
report = scorers_single_line = f"{player_scored_0} scored in the {goal_0}nd minute \n{player_scored_1} scored in the {goal_1}th minute"
print(report)

#=====Part 2===================================================================

player = "Ruud Gullit"
first_name = player[:player.find(" ")]
print(first_name)
last_name = player[player.find(" ")+1:]
print(last_name)
last_name_len = len(player[player.find(" ")+1:])
print(last_name_len)

name_short = f'{player[:1]}.{player[player.find(" "):]}'
print(name_short)

chant = (' '.join(len(player[:player.find(" ")]) * [f'{first_name}!']))
print(chant)

good_chant = print(chant[-1] != " ")