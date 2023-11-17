# def numberOfMoveablePiecesHeuristic(board, move, player):
#     isStage1 = len(board['currentState']['humanStones']) + len(board['currentState']['computerStones']) <= 18

#     numPlayerOneTokens = numOfValue(board, 'human')
#     numPlayerTwoTokens = numOfValue(board, 'computer')

#     movablePiecesBlack = 0

#     if not isStage1:
#         movablePiecesBlack = len(find_available_position(board, 'computer'))

#     if not isStage1:
#         if numPlayerTwoTokens <= 2 or movablePiecesBlack == 0:
#             evaluation = float('inf')
#         elif numPlayerOneTokens <= 2:
#             evaluation = float('-inf')
#         else:
#             evaluation = 100 * (numPlayerOneTokens - numPlayerTwoTokens)
#             evaluation -= 50 * movablePiecesBlack
#     else:
#         evaluation = 100 * (numPlayerOneTokens - numPlayerTwoTokens)

#     return evaluation

# def numberOfPiecesHeuristic(board, player):
#     isStage1 = len(board['currentState']['humanStones']) + len(board['currentState']['computerStones']) < 18
#     numPlayerOneTokens = numOfValue(board, player)
#     numPlayerTwoTokens = numOfValue(board, player)

#     movablePiecesBlack = 0

#     if not isStage1:
#         movablePiecesBlack = len(find_available_position(board, player))

#     if not isStage1:
#         if numPlayerTwoTokens <= 2 or movablePiecesBlack == 0:
#             evaluation = float('inf')
#         elif numPlayerOneTokens <= 2:
#             evaluation = float('-inf')
#         else:
#             evaluation = 200 * (numPlayerOneTokens - numPlayerTwoTokens)
#     else:
#         evaluation = 100 * (numPlayerOneTokens - numPlayerTwoTokens)

#     return evaluation

# #TODO jedna koja ima sve  
# # def advancedHeuristic(board, player):
# #     isStage1 = len(board['currentState']['humanStones']) + len(board['currentState']['computerStones']) < 18
# #     numPlayerOneTokens = numOfValue(board, player)
# #     numPlayerTwoTokens = numOfValue(board, player)

# #     numPlayerOneMills = numOfMills(board, player)
# #     numPlayerTwoMills = numOfMills(board, player)

# #     numPlayerOneBlocked = numOfBlocked(board, player)
# #     numPlayerTwoBlocked = numOfBlocked(board, player)

# #     numPlayerOnePotentialMills = numOfPotentialMills(board, player)
# #     numPlayerTwoPotentialMills = numOfPotentialMills(board, player)

# #     if not isStage1:
# #         evaluation = 200 * (numPlayerOneTokens - numPlayerTwoTokens) + 50 * (numPlayerOneMills - numPlayerTwoMills) - 50 * (numPlayerOneBlocked - numPlayerTwoBlocked) + 100 * (numPlayerOnePotentialMills - numPlayerTwoPotentialMills)
# #     else:
# #         evaluation = 100 * (numPlayerOneTokens - numPlayerTwoTokens)

# #     return evaluation

# def can_form_mill(board, player):
#     player_color = 'black' if player == 'computer' else 'white'
#     player_stones = board['currentState']['humanStones'] if player == 'human' else board['currentState']['computerStones']

#     for mill in mills_positions:
#         if sum(any(stone['square'] == position['square'] and stone['index'] == position['index'] for stone in player_stones) for position in mill) == 2:
#             empty_positions = [position for position in mill if not any(stone['square'] == position['square'] and stone['index'] == position['index'] for stone in player_stones)]
#             if empty_positions:
#                 return True

#     return False

# # if opponent_can_form_mill(board, player): 
#     #     return 350
#     # if potentional_mills(board, move, player): 
#     #     return 300
#     # else: 
#     #     return 100
#     #     # return numberOfMoveablePiecesHeuristic(board, move, player)

# def heuristic(board, player):
#     # Weights for each factor
#     weights = {
#         'num_of_value': 10,
#         'num_of_mills': 40,
#         'blocked_mills': 30,
#         'potential_mills': 50,
#         'possible_moves': 10,
#         'blocked_pieces': 10
#     }

#     # Calculate the score for each factor
#     num_of_value_score = numOfValue(board, player) * weights['num_of_value']
#     num_of_mills_score = numOfMills(board, player) * weights['num_of_mills']
#     blocked_mills_score = count_blocked_mills(board, player) * weights['blocked_mills']
#     potential_mills_score = count_potential_mills(board, player) * weights['potential_mills']
#     possible_moves_score = count_possible_moves(board, player) * weights['possible_moves']
#     blocked_pieces_score = count_blocked_pieces(board, player) * weights['blocked_pieces']

#     # Sum up the scores to get the total score
#     total_score = num_of_value_score + num_of_mills_score + blocked_mills_score + potential_mills_score + possible_moves_score + blocked_pieces_score

#     return total_score

# def opponent_can_form_mill(board, player):
#     opponent_color = 'black' if player == 'human' else 'white'
#     opponent_stones = board['currentState']['computerStones'] if player == 'human' else board['currentState']['humanStones']

#     for mill in mills_positions:
#         if sum(any(stone['square'] == position['square'] and stone['index'] == position['index'] for stone in opponent_stones) for position in mill) == 2:
#             empty_positions = [position for position in mill if not any(stone['square'] == position['square'] and stone['index'] == position['index'] for stone in opponent_stones)]
#             if empty_positions:
#                 return True

#     return False

# #broj igraca
# def numOfValue(board, player):
#     if player == 'human':
#         return len(board['currentState']['humanStones'])
#     else:
#         return len(board['currentState']['computerStones'])

# #broj mlinova
# def numOfMills(board, player):
#     mills = 0

#     playerStones = board['currentState']['humanStones'] if player == 'human' else board['currentState']['computerStones']

#     for mill in mills_positions:
#         if all(position in playerStones for position in mill):
#             mills += 1

#     return mills

# #broj blokiranih mlinova
# def count_blocked_mills(board, player):
#     blocked_mills = 0

#     # Get the opponent's stones
#     opponent_stones = board['currentState']['computerStones'] if player == 'human' else board['currentState']['humanStones']

#     # Iterate over all possible mill positions
#     for mill in mills_positions:
#         # Check if the player has two pieces in this mill position
#         player_pieces_in_mill = [position for position in mill if position in board['currentState'][player + 'Stones']]
#         if len(player_pieces_in_mill) == 2:
#             # Check if the remaining position is occupied by the opponent
#             remaining_position = [position for position in mill if position not in player_pieces_in_mill][0]
#             if remaining_position in opponent_stones:
#                 blocked_mills += 1

#     return blocked_mills

# #broj potencijalnih mlinova
# def count_potential_mills(board, player):
#     potential_mills = 0

#     # Get the player's stones
#     player_stones = board['currentState']['humanStones'] if player == 'human' else board['currentState']['computerStones']

#     # Iterate over all possible mill positions
#     for mill in mills_positions:
#         # Check if the player has two pieces in this mill position and the third position is empty
#         player_pieces_in_mill = [position for position in mill if position in player_stones]
#         if len(player_pieces_in_mill) == 2:
#             # Check if the remaining position is empty
#             remaining_position = [position for position in mill if position not in player_pieces_in_mill][0]
#             if remaining_position not in board['currentState']['humanStones'] and remaining_position not in board['currentState']['computerStones']:
#                 potential_mills += 1

#     return potential_mills

# #broj mogucih pomeranja
# def count_possible_moves(board, player):
#     # Get the available positions for the player
#     available_positions = find_available_position(board, player)

#     # The number of possible moves is the number of available positions
#     return len(available_positions)

# def count_blocked_pieces(board, player):
#     blocked_pieces = 0

#     # Get the player's stones
#     player_stones = board['currentState']['humanStones'] if player == 'human' else board['currentState']['computerStones']

#     # Iterate over all player's stones
#     for stone in player_stones:
#         # Get the available moves for this stone
#         available_moves = find_available_moves(board['currentState']['humanStones'], board['currentState']['computerStones'], stone)
#         # If there are no available moves, the stone is blocked
#         if len(available_moves) == 0:
#             blocked_pieces += 1

#     return blocked_pieces

# def check_if_mill_blocked(board, move, player):

#     color = 'white' if player == 'human' else 'black'

#     # Izvlačimo kamenčiće protivnika
#     opponent_stones = board['currentState']['computerStones'] if color == 'white' else board['currentState']['humanStones']

#     # Proveravamo da li bi potez blokirao mlin
#     for mill in mills_positions:
#         # Proveravamo da li protivnik ima dva kamena u mlinu i da li je treća pozicija prazna
#         if sum(any(stone['square'] == position['square'] and stone['index'] == position['index'] for stone in opponent_stones) for position in mill) == 2 and any(position['square'] == move['square'] and position['index'] == move['index'] for position in mill):
#             return True

#     # Ako nije blokiran nijedan mlin, potez ne blokira mlin
#     return False

# def potentional_mills(board, move, player):
#     color = 'white' if player == 'human' else 'black'

#     # Izvlačimo kamenčiće trenutnog igrača
#     player_stones = board['currentState']['humanStones'] if color == 'white' else board['currentState']['computerStones']

#     # Dodajemo potez u listu kamenčića igrača da bismo proverili da li stvara mlin
#     player_stones.append(move)

#     # Proveravamo da li potez stvara mlin
#     for mill in mills_positions:
#         # Proveravamo da li igrač ima tri kamena u mlinu
#         if sum(any(stone['square'] == position['square'] and stone['index'] == position['index'] for stone in player_stones) for position in mill) == 3:
#             # Uklanjamo potez iz liste kamenčića igrača jer je ovo samo privremena provera
#             player_stones.remove(move)
#             return True

#     # Uklanjamo potez iz liste kamenčića igrača jer je ovo samo privremena provera
#     player_stones.remove(move)

#     # Ako potez ne stvara mlin, vraćamo False
#     return False



# def determine_winner(board):
#     if board['out']['totalHuman'] == 2:
#         return "AI is the winner"
#     elif board['out']['totalComputer'] == 2:
#         return "Human is the winner"
#     else:
#         return None
