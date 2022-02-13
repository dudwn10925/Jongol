# players = list(input().split())
# num = players.count(players[0])
# player = []
# for p in players:
#     if players.count(p) <= num:
#         num = players.count(p)
#         if p not in player:
#             player.append(p)

# for p in player:
#     print(p)
# print(num)

players = input().split()
fouls = {}
for player in players:
    if player in fouls:
        fouls[player] += 1
    else:
        fouls[player] = 1
        
min_foul = min(fouls.values())
for player, foul in fouls.items():
    if foul == min_foul:
        print(player)
print(min_foul)