import random

# Reference code from Scott Blenkhorne's demo of making an UNO card game
class Card:
    """
    Create a Card object
    """
    def __init__(self, rank, suit):
        """
        Initialize Card
        
        Parameters:
            rank (str): a card's rank
            suit (str): a card's suit
        """
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        """Print formated card's rank and suit (eg. A of Hearts, 2 of Clubs)"""
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        """
        Compare two cards with its rank and suit to determine if they are equal

        Parameter:
            other (str): compare the card with other card
        """
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other):
        """
        Check if the cards are less than or equal to so they can be sorted

        Parameter:
            other (str): compare the card with other card
        """
        return self.rank <= other.rank
    
    def __ge__(self, other):
        """
        Check if the cards are greater than or equal to so they can be sorted

        Parameter:
            other (str): compare the card with other card
        """
        return self.rank >= other.rank
    
    def getRank(self):
        """Return the card's rank"""
        return self.rank
    
    def getSuit(self):
        """Return the card's rank"""
        return self.suit
    
class Deck:
    """
    Create a Deck object
    """
    def __init__(self):
        """
        Initialize Deck
        
        Generate a standard deck of 52 cards by creating 52 possible instances of the Card class
        """
        ranks = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
        self.cards = []
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))
    
    def __iter__(self):
        """
        Make deck object iterable

        Return:
            self (list): an iterable deck
        """
        self.currentIndex = 0
        return self
    
    def __next__(self):
        """
        Return next item in the iteration

        Return:
            currentCard (str): current card in the deck
        """
        if self.currentIndex < self.countDeck():
            currentCard = self.cards[self.currentIndex]
            self.currentIndex += 1
            return currentCard
        else:
            raise StopIteration
        
    def countDeck(self):
        """Return the count of the deck of cards"""
        return len(self.cards)
    
    def deal(self, num):
        """
        Return a specified number of cards off the top of the deck
        
        Parameter:
            num (int): the number of cards to deal

        Return:
            dealtCards (list): a list of specified number of cards
        """
        dealtCards = []
        for i in range(num):
            card = self.cards.pop()
            dealtCards.append(card)
        return dealtCards
    
    def dealCard(self):
        """Return one card from deck"""
        return self.deal(1)[0]
    
    def shuffle(self):
        """Shuffle a full deck using import random shuffle"""
        if self.countDeck() < 52:
            print("Only full deck can be shuffled.")
        random.shuffle(self.cards)
    
    def getDeck(self):
        """Return deck"""
        return self.cards

class Player:
    """
    Create a Player object
    """
    def __init__(self, name, deck):
        """
        Initialize Player
        
        Parameters:
            name (str): user or computer
            deck (list): copy of an instance of Deck object
            
        Note:
        The deck parameter is used to create a copy of Deck within Player
        All changes within this class should affect the global deck
        """
        self.name = name
        self.deck = deck
        self.hand = []
        self.book = []
        self.score = 0
    
    def countHand(self):
        """Return the count of the player's hand"""
        return len(self.hand)
    
    def printHand(self):
        """Print the player's hand"""
        print(f"{self.name}'s hand: ")
        i = 1
        for card in self.hand:
            print(f"{i}) {card}")
            i += 1
        print()
    
    def getHand(self):
        """Returns the player's hand"""
        return self.hand
    
    def setHand(self, newHand):
        """
        Set the player's hand to a new hand

        Parameter:
            newHand (list): an empty list for a player hand
        """
        self.hand = newHand
    
    def sortHand(self):
        """Sort the player's hand"""
        self.hand.sort()
    
    def drawCard(self, card):
        """
        Add a new card to the player's hand

        Parameter:
            card (str): card to be added
        """
        self.hand.append(card)
        
    def removeCard(self, card):
        """
        Remove a card from the player's hand

        Parameter:
            card (str): card to be removed
        """
        self.hand.remove(card)
    
    def getBook(self):
        """Return the player's books"""
        return self.book
        
    def addBook(self, bookRank):
        """
        Add a book rank to list

        Parameter:
            bookRank (str): rank of book to be added
        """
        self.book.append(bookRank)
        
    def removeBook(self, book):
        """
        Remove cards in the player's book

        Parameter:
            book (list): a list of the player's book
        """
        for card in book:
            self.removeCard(card)
        
    def getScore(self):
        """Return the player's score"""
        return self.score
        
    def checkHand(self, rank):
        """
        Check the player's hand for a specified rank

        Parameter:
            rank (str): the rank a player asked for
        
        Return:
            duplicateCards (list): a list of the specified rank, if none, it's an empty list
        """
        duplicateCards = []
        for card in self.hand:
            if card.getRank() == rank:
                duplicateCards.append(card)
        return duplicateCards
    
    def checkBook(self):
        """
        Check the player's hand for books
        
        Return:
            rank (str): the book rank, if none, return empty string
        """
        ranks = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for rank in ranks:
            book = self.checkHand(rank)
            if len(book) == 4:
                self.removeBook(book)
                self.addBook(rank)
                self.score += 1
                return "Got fours of", rank
        return "No book yet", ''

class UserPlayer(Player):
    """
    Create a UserPlayer object, subclass of Player class
    """
    def __init__(self, name, deck):
        """
        Initialize UserPlayer

        Parameters:
            name (str): the user player's name
            deck (list): a copy of the deck instance
        
        Note:
        The super().__init__(name, deck) invokes the __init__ method of 
        the Player, ensuring proper initialization of the parent class
        """
        super().__init__(name, deck)
        
    def userAskCard(self):
        """
        Get user input of a card rank, ask computer player for that rank

        Return:
            rank (str): user input of a card rank
        """
        if self.countHand() == 0 and self.deck.countDeck() != 0:
            self.drawCard(self.deck.dealCard())
            
        ranks = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        rank = input("User: Do you have any ")
        if rank not in ranks:
            print("Please choose a rank of 2-10, J, Q, K, or A")
            rank = input("User: Do you have any ")
        print()
        return rank

class ComputerPlayer(Player):
    """
    Create a ComputerPlayer object, subclass of Player class
    """
    def __init__(self, name, deck):
        """
        Initialize ComputerPlayer

        Parameters:
            name (str): the computer player's name
            deck (list): a copy of the deck instance
        
        Note:
        The super().__init__(name, deck) invokes the __init__ method of 
        the Player, ensuring proper initialization of the parent class
        """
        super().__init__(name, deck)
        self.cardsAsked = []

    def compAskCard(self):
        """
        Ask user player for a card rank

        Return:
            rank (str): computer's card rank
        """
        userCards = self.getCardsAsked()
        print(userCards)
        if self.countHand() == 0 and self.deck.countDeck() != 0:
            self.drawCard(self.deck.dealCard())
            
        for card in self.hand:
            rank = card.getRank()
            if rank in userCards:
                print("Computer: Do you have any", rank)
                return rank
        randomCard = random.choice(self.hand)
        rank = randomCard.getRank()
        print("Computer: Do you have any", rank, "\n")
        return rank
    
    def getCardsAsked(self):
        """Return a list of card rank user player has previously asked for"""
        return self.cardsAsked
    
    def trackCardAsked(self, rank):
        """Add a card rank user player asked for"""
        self.cardsAsked.append(rank)
        
    def clearCardsAsked(self):
        """Set list of user player's card ranks to empty"""
        self.cardsAsked = []

class GoFish:
    """
    Create a GoFish object. A game of GO FISH between the user and computer.
    """
    def __init__(self):
        """
        Initialize GoFish Game
        
        Initialize the players (user and computer), current player, and deck
        """
        self.deck = Deck()
        self.playerUser = UserPlayer("User", self.deck)
        self.playerComp = ComputerPlayer("Computer", self.deck)
        
    def dealCards(self):
        """Shuffles the deck and deals 7 cards to each player"""
        self.deck.shuffle()
        self.playerUser.setHand(self.deck.deal(7))
        self.playerComp.setHand(self.deck.deal(7))
                
    def playCard(self, isPlaying):
        """
        While the game is playing, each hand is sorted
        The user's hand is printed and the user player asks the computer for a card with a specific rank
        The computer adds that rank to an empty list to keep track of cards player has asked
        The computer will then print it's hand and ask the user for a card

        Parameters:
            isPlaying (boolean): when game is playing, true is passed and when game is ended, false is returned.
        """
        userBook = []
        compBook = []
        while isPlaying:
            self.playerUser.sortHand()
            self.playerComp.sortHand()
            
            self.playerUser.printHand()
            userRank = self.playerUser.userAskCard()
            self.playerComp.trackCardAsked(userRank)
            while self.userTurn(userRank):
                userRank = self.playerUser.userAskCard()
                self.playerComp.trackCardAsked(userRank)
            
            input("<Enter> to continue\n")
            
            self.playerComp.printHand()
            compRank = self.playerComp.compAskCard()
            while self.compTurn(compRank):
                compRank = self.playerComp.compAskCard()
            self.playerComp.clearCardsAsked()
            
            if not self.deck.countDeck() or (not self.playerUser.countHand() and not self.playerComp.countHand()):
                userBook = self.playerUser.getBook()
                compBook = self.playerComp.getBook()

                self.determineWinner(userBook, compBook)
                isPlaying = False
                break
        
    def userTurn(self, userRank):
        """
        When the computer has cards in its hand and the deck is not 0,
        The computer will check their hand for the card the user has asked for
        and will either give the card or tell the user to draw a card if it doesn't have that card.
        If the computer gives the card to the use, it will check for books and print out books and corresponding ranks.
        If the user is told to "Go fish" after drawing a card, books are also printed.

        Parameter:
            userRank (str): user input

        Return:
            boolean: return False when computer player says 'Go Fish'
        """
        if self.playerComp.countHand() != 0 and self.deck.countDeck() != 0:
            
            duplicateCards = self.playerComp.checkHand(userRank)
            if len(duplicateCards) > 0:
                for card in duplicateCards:
                    self.playerComp.removeCard(card)
                    self.playerUser.drawCard(card)
                print("Computer: I have " + userRank + ". Here you go >:(\n")
                
                checkedBook, bookRank = self.playerUser.checkBook()
                print(f"User: {checkedBook} {bookRank}\n")
                return True
            else:
                print("Computer: Go Fish! (Draw a card)\n")
                self.playerUser.drawCard(self.deck.dealCard())
                
                checkedBook, bookRank = self.playerUser.checkBook()
                print(f"User: {checkedBook} {bookRank}\n")
                self.playerUser.printHand()
                print("-----------------------\n")
                return False

    def compTurn(self, compRank):
        """
        When the user has cards in its hand and the deck is not empty,
        The user will check their hand for the card the computer has asked for
        and will either give the card or tell the computer to draw a card if it doesn't have that card.
        If the computer gives the card to the use, it will check for books and print out books and corresponding ranks.
        If the user is told to "Go fish" after drawing a card, books are also printed.

        Parameter:
            compRank (str): computer generated rank

        Return:
            boolean: return False when user player says 'Go Fish'
        """
        if self.playerUser.countHand() != 0 and self.deck.countDeck() != 0:
            
            duplicateCards = self.playerUser.checkHand(compRank)
            if len(duplicateCards) > 0:
                for card in duplicateCards:
                    self.playerUser.removeCard(card)
                    self.playerComp.drawCard(card)
                print("User: I have " + compRank + ". Here you go >:(\n")
                
                checkedBook, bookRank = self.playerComp.checkBook()
                print(f"Computer: {checkedBook} {bookRank}\n")
                return True
            else:
                print("User: Go Fish! (Draw a card)\n")
                self.playerComp.drawCard(self.deck.dealCard())
                
                checkedBook, bookRank = self.playerComp.checkBook()
                print(f"Computer: {checkedBook} {bookRank}\n")
                self.playerComp.printHand()
                print("-----------------------\n")
                return False
        
    def determineWinner(self, userBook, compBook):
        """
        Print the winner of the game

        Parameters:
            userBook (list): a list of the user accumulated books
            compBook (list): a list of the computer accumulated books
        """
        userScore = self.playerUser.getScore()
        compScore = self.playerComp.getScore()
        print(f"User score: {userScore}; I have {userBook}")
        print(f"Computer score: {compScore}; I have {compBook}")
        if len(userBook) > len(compBook):
            print("User: I win")
        elif len(userBook) < len(compBook):
            print("Computer: I win")
        else:
            print("It's a tie")

# Test case
game = GoFish()
game.dealCards()
game.playCard(True)
