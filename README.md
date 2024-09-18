# gofish.py features
Our program is a game of Go Fish. It's meant to be a game between a user and computer. The game starts with a deck of 52 cards, shuffled, and dealt seven cards to each player. Each player takes turn to ask for a card to make the most books (fours of a kind).

# computer intelligence
The computer can keep track of the cards the user asked for. The computer will take in the user input and add it to a list, and when it's the computer's turn, it can choose a common card between that list and its hand, if there is no common card, it will choose and ask for a random card in its hand.

# class organization
We have two classes for creating a Card and Deck objects. The Card object gives a printed string of a card's rank and suit (eg "A of Hearts"). The Deck object generates 52 instances of the Card object.

We have a parent class for creating Player object and two child classes for creating Computer Player and User Player objects. A Player object can draw and remove a card, remove a book, check its hand for duplicate cards, and check its hand for books. Name and deck, a copy instance of Deck object, are passed to the Player object, to create a player. Additional data are stored as a player's hand, book, and score.

The User Player object has an additional method to ask for a card from the computer. The Computer Player object also has its own methods to ask the user for a card, which implement the computer intelligence mentioned above.

# current status
Our current status is that we have a completed and playable go fish game with a minor issue in which the program is not adding up to 13 books at the end. But it is not necessarily a hinder because then we can have a tie between the computer and user. We tried to debug it by changing the if statements in checking the players' hand and the deck length when the game is coming to an end.

# how to run program
By clicking run, you are shown the user's hand and prompted with "Do you have any __". You can ask the computer for a card in the user's hand by inputting a rank in ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']. 

Please be an honest player because we did not restrict user input to only ask for the cards in their hand and not any other ones. 

If the computer has any cards with that rank in its hand, it will say "I have it" and the card(s) will be added to the user's hand. If the computer does not have any cards, it will say "Go Fish" and a card will be added to the user's hand from the deck.

You will get another turn if the computer has any duplicate cards. If not, then it's the computer's turn asking for a card. It will keep a list of user input to compare its hand. This list will be cleared after the computer finishes its turn. The game ends when there is no more cards in the deck or both the players' hands are empty.