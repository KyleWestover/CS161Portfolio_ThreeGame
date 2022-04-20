# Author: Kyle Westover
# Date: 02Dec21
# Description: Class that creates and plays a game in which a player wins by having 3 numbers sum to exactly 15
class TheThreeGame:
    """
    Represents a game with a list of numbers chosen by the first and second players, a turn tracker, and the current
    state of the game
    """
    def __init__(self):
        """
        Creates a game with empty lists for numbers chosen for each player, a turn tracker set to 'first_player' to
        start, and a tracker of the current state of the game set to 'GAME_UNFINISHED' to start
        """
        self._first_player_numbers = []
        self._second_player_numbers = []
        self._whose_turn = "first_player"
        self._current_state = "GAME_UNFINISHED"

    def get_winner(self):
        """
        Returns winner of the game
        """
        target = 15  # target number to win the game

        # check for first_player win
        if len(self._first_player_numbers) == 3:
            if (self._first_player_numbers[0] + self._first_player_numbers[1] + self._first_player_numbers[2]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
        elif len(self._first_player_numbers) == 4:
            if (self._first_player_numbers[0] + self._first_player_numbers[1] + self._first_player_numbers[3]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
            elif (self._first_player_numbers[0] + self._first_player_numbers[2] + self._first_player_numbers[3]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
            elif (self._first_player_numbers[1] + self._first_player_numbers[2] + self._first_player_numbers[3]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
        elif len(self._first_player_numbers) == 5:
            if (self._first_player_numbers[0] + self._first_player_numbers[1] + self._first_player_numbers[4]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
            elif (self._first_player_numbers[0] + self._first_player_numbers[2] + self._first_player_numbers[4]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
            elif (self._first_player_numbers[0] + self._first_player_numbers[3] + self._first_player_numbers[4]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
            elif (self._first_player_numbers[1] + self._first_player_numbers[2] + self._first_player_numbers[4]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
            elif (self._first_player_numbers[1] + self._first_player_numbers[3] + self._first_player_numbers[4]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
            elif (self._first_player_numbers[2] + self._first_player_numbers[3] + self._first_player_numbers[4]) == target:
                self._current_state = "FIRST_PLAYER_WON"
                return self._current_state
        elif len(self._first_player_numbers) < 3:
            return None

        # check for second_player win
        if len(self._second_player_numbers) == 3:
            if (self._second_player_numbers[0] + self._second_player_numbers[1] + self._second_player_numbers[2]) == target:
                self._current_state = "SECOND_PLAYER_WON"
                return self._current_state
            else:
                return None
        elif len(self._second_player_numbers) == 4:
            if (self._second_player_numbers[0] + self._second_player_numbers[1] + self._second_player_numbers[3]) == target:
                self._current_state = "SECOND_PLAYER_WON"
                return self._current_state
            elif (self._second_player_numbers[0] + self._second_player_numbers[2] + self._second_player_numbers[3]) == target:
                self._current_state = "SECOND_PLAYER_WON"
                return self._current_state
            elif (self._second_player_numbers[1] + self._second_player_numbers[2] + self._second_player_numbers[3]) == target:
                self._current_state = "SECOND_PLAYER_WON"
                return self._current_state
            else:
                return None
        elif len(self._second_player_numbers) < 3:
            return None

    def is_it_a_draw(self):
        """
        Returns game winner by calling get_winner method or returns "IT_IS_A_DRAW" or "GAME_UNFINISHED" as appropriate
        when there is no winner
        """
        # check for winner
        winner_status = self.get_winner()
        # if no winner, decide whether the game is a draw or unfinished
        if len(self._first_player_numbers) == 5 and len(self._second_player_numbers) == 4 and winner_status is None:
            self._current_state = "IT_IS_A_DRAW"
            return self._current_state
        elif (len(self._first_player_numbers) < 5 or len(self._second_player_numbers) < 4) and winner_status is None:
            self._current_state = "GAME_UNFINISHED"
            return self._current_state
        elif winner_status is not None:
            return winner_status

    def make_move(self, player, number):
        """
        Verifies that game is still ongoing, the correct player is playing, the number chosen is within range, and the
        number chosen has not been previously chosen in the current game. If all criteria are met, the number will be
        added to the list of the respective player and then the lists are checked for a winner, a draw, or an unfinished
        game.
        """
        # test for correct player taking turn
        if player == self._whose_turn:
            # check if number already chosen
            if number not in self._first_player_numbers and number not in self._second_player_numbers:
                # check to make sure game is still ongoing
                if self._current_state == "GAME_UNFINISHED":
                    # check to make sure integer is within range
                    if 1 <= number <= 9:
                        # record first_player's number, check for winner/draw, switch player turn
                        if player == "first_player":
                            self._first_player_numbers = self._first_player_numbers + [number]
                            self._whose_turn = "second_player"
                            self.is_it_a_draw()
                            return True

                        # record second_player's number, check for winner/draw, switch player turn
                        elif player == "second_player":
                            self._second_player_numbers = self._second_player_numbers + [number]
                            self._whose_turn = "first_player"
                            self.is_it_a_draw()
                            return True
                    else:
                        # Number out of range
                        return False
                else:
                    # Game is already over
                    return False
            else:
                # Number already used
                return False
        else:
            # Wrong player turn
            return False
