class Player:
    def __init__(self, name: str):
        self.name = name

    def guess_letter(self, letter: str):
        # if letter not in self.secret_word:
        #     self.lives -= 1
        ...


class Game:
    def __init__(self, player: Player, secret_word: str | None = None):
        self.player = player
        self.secret_word = secret_word
        self.lives = len(secret_word)
        self.tries = 0
        self.msg = ""
        self.final_msg = ""
        self.secret_word = secret_word or self._generate_random_word()

        self.blank_spaces = [""] * len(self.secret_word)

    def show_progress(self):
        ui = f"""Guess the word
        lives: {self.lives}
        tries: {self.tries}
        input letter: {self.letter}

        {self.msg}
        {self.blank_spaces}

        {self.final_msg}
        """

        print(ui)

    def _get_all_letter_indexes(self, letter: str, secret_word: str):
        indexes = []
        for index, value in enumerate(secret_word):
            if letter == value:
                indexes.append(index)
        return indexes


    def _lost_live(self):
        self.lives -= 1

    def _check_win(self):
        if self.lives > 0 and "".join(self.blank_spaces) == self.secret_word:
            self.final_msg = "You won!"

        if self.lives < 0:
            self.final_msg = f"Game Over! Secret word was: {self.secret_word}"


    def guess_word(self, letter: str):
        try:
            self.tries += 1
            self.letter = letter
            letter_indexes = self._get_all_letter_indexes(letter, self.secret_word)
            if not letter_indexes:
                self.msg = "You lost a live"
                self._lost_live()
                self._check_win()
                return
            self.msg = "Great, well guessed!"
            for index in letter_indexes:
                self.blank_spaces[index] = letter

            self._check_win()
        except Exception as err:
            print("error: ", err)



player1 = Player(name="Esteban")
game = Game(player=player1, secret_word="house")

game.guess_word(letter='h')
game.show_progress()
game.guess_word(letter='o')
game.show_progress()
game.guess_word(letter='u')
game.show_progress()
game.guess_word(letter='s')
game.show_progress()
game.guess_word(letter='1')
game.show_progress()
game.guess_word(letter='1')
game.show_progress()
game.guess_word(letter='1')
game.show_progress()
game.guess_word(letter='1')
game.show_progress()
game.guess_word(letter='1')
game.show_progress()
game.guess_word(letter='1')
game.show_progress()
game.guess_word(letter='1')
game.show_progress()

