from typing import Optional
import random


class Player:
    def __init__(self, name: str):
        self.name = name
        self.guessed_letters: set[str] = set()  # Track what player has guessed

    def add_guess(self, letter: str) -> bool:
        """
        Add a letter to guessed letters.
        Returns False if already guessed, True otherwise.
        """
        if letter in self.guessed_letters:
            return False
        self.guessed_letters.add(letter)
        return True


class Game:
    def __init__(self, player: Player, secret_word: Optional[str] = None):
        self.player = player
        self.secret_word = (secret_word or self._generate_random_word()).lower()
        self.max_lives = 6  # Standard hangman lives
        self.lives = self.max_lives
        self.tries = 0
        self.msg = ""
        self.final_msg = ""
        self.guessed_letters: set[str] = set()  # Track all guessed letters
        # Initialize blank spaces with underscores for better visibility
        self.blank_spaces = ["_"] * len(self.secret_word)

    def _generate_random_word(self) -> str:
        """Generate a random word from a predefined list."""
        words = ["python", "hangman", "computer", "programming", "developer"]
        return random.choice(words)

    def show_progress(self):
        """Display current game state."""
        # Show guessed letters
        guessed = sorted(list(self.guessed_letters))

        ui = f"""
╔══════════════════════════════════════╗
║          HANGMAN GAME                ║
╠══════════════════════════════════════╣
║ Player: {self.player.name:<28} ║
║ Lives: {self.lives}/{self.max_lives:<28} ║
║ Tries: {self.tries:<28} ║
╠══════════════════════════════════════╣
║ Word: {' '.join(self.blank_spaces):<31} ║
║ Guessed: {', '.join(guessed) if guessed else 'None':<29} ║
╠══════════════════════════════════════╣
║ {self.msg:<37}║
║ {self.final_msg:<37}║
╚══════════════════════════════════════╝
        """
        print(ui)

    def _get_all_letter_indexes(self, letter: str) -> list[int]:
        """
        Find all positions where the letter appears in secret_word.
        Returns list of indexes.
        """
        return [index for index, char in enumerate(self.secret_word) if char == letter]

    def _lost_live(self):
        """Decrease lives by 1."""
        self.lives -= 1

    def _check_win(self) -> bool:
        """
        Check win/loss conditions.
        Returns True if game is over, False otherwise.
        """
        # Check win condition
        if "".join(self.blank_spaces) == self.secret_word:
            self.final_msg = f"🎉 YOU WON in {self.tries} tries!"
            return True

        # Check loss condition
        if self.lives <= 0:
            self.final_msg = f"💀 GAME OVER! Word was: {self.secret_word.upper()}"
            return True

        return False

    def guess_word(self, letter: str) -> bool:
        """
        Process a letter guess.
        Returns True if game continues, False if game is over.
        """
        # Normalize input
        letter = letter.lower().strip()

        # Validate input
        if not letter or len(letter) != 1 or not letter.isalpha():
            self.msg = "⚠️  Invalid input! Enter a single letter."
            return True

        # Check if already guessed
        if letter in self.guessed_letters:
            self.msg = f"⚠️  Already guessed '{letter}'!"
            return True

        # Track the guess
        self.tries += 1
        self.guessed_letters.add(letter)

        # Find letter positions
        letter_indexes = self._get_all_letter_indexes(letter)

        if not letter_indexes:
            self.msg = f"❌ '{letter}' not in word. Lost a life!"
            self._lost_live()
        else:
            self.msg = f"✅ Great! '{letter}' appears {len(letter_indexes)} time(s)!"
            # Fill in the blanks
            for index in letter_indexes:
                self.blank_spaces[index] = letter

        # Check if game is over
        return not self._check_win()

    def play(self):
        """Main game loop."""
        print("\n🎮 Welcome to Hangman!")
        print(f"Player: {self.player.name}\n")

        self.show_progress()

        while True:
            letter = input("\nGuess a letter: ").strip()

            # Process the guess
            continue_game = self.guess_word(letter)
            self.show_progress()

            # Check if game is over
            if not continue_game:
                play_again = input("\nPlay again? (y/n): ").strip().lower()
                if play_again == 'y':
                    self.__init__(self.player, self._generate_random_word())
                    self.play()
                break


# Example usage
if __name__ == "__main__":
    player1 = Player(name="Esteban")
    game = Game(player=player1, secret_word="house")

    # Automated test
    test_letters = ['h', 'o', 'u', 's', '1', 'x', 'e']
    for letter in test_letters:
        game.guess_word(letter)
        game.show_progress()
        if game.final_msg:
            break

    # Or play interactively:
    # game.play()
