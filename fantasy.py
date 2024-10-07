# CHANGE FILE NAMES HERE
# ************************
text_file_1 = "espn-2024.txt"
text_file_2 = "fantasy_pros-2024.txt"
text_file_3 = "nhl_com-2024.txt"
# ************************

list_1 = []
list_2 = []
list_3 = []

def get_espn():
    with open(text_file_1, 'r') as f:
        print('Reading First Text File...')
        for line in f:
            list_1.append(line.strip())

def get_fantasy_pros():
    with open(text_file_2, 'r') as f:
        print('Reading Second Text File...')
        for line in f:
            list_2.append(line.strip())

def get_nhl_com():
    with open(text_file_3, 'r') as f:
        print('Reading Third Text File...')
        for line in f:
            list_3.append(line.strip())

def remove_player(player):
    global list_1, list_2, list_3  # Declare lists as global
    playerlower = player.lower()

    def remove_from_list(player_list, player_name):
        updated = []
        for p in player_list:
            if player_name not in p.lower():
                updated.append(p)

        return updated

    list_1 = remove_from_list(list_1, playerlower)
    list_2 = remove_from_list(list_2, playerlower)
    list_3 = remove_from_list(list_3, playerlower)

def print_lists_aligned():
    # Print the headers
    print(f"{'ESPN':<40}{'FANTASY PROS':<30}{'NHL.COM'}")

    # Print the players in each list, aligned
    for i in range(3):  # Limit to first 3 players
        player1 = list_1[i] if i < len(list_1) else ""
        player2 = list_2[i] if i < len(list_2) else ""
        player3 = list_3[i] if i < len(list_3) else ""

        print(f"{player1:<25}{player2:<25}{player3}")


def main_loop():
    while True:
        print_lists_aligned()

        to_remove = input("\n\n")
        if to_remove == "exit":
            break
        elif to_remove != " " and to_remove != "":
            remove_player(to_remove)

def main():
    get_espn()
    get_fantasy_pros()
    get_nhl_com()
    print('\n\nStarting main loop...')
    main_loop()

if __name__ == '__main__':
    main()