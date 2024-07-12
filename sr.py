from simple_spaced_repetition import Card

# Creating a new Card object with initial state
card = Card()
print(card)  # Output: Card(status=learning, step=0, interval=None, ease=2.5)

# Getting the options for the card
#The options method provides four possible responses for reviewing the card: 
#'again', 'hard', 'good', and 'easy'. 
# Each response corresponds to a different new state for the card.
options = card.options()
print(options)
# Output: [
#   ('again', Card(status=learning, step=0, interval=0:01:00, ease=2.5)),
#   ('hard', Card(status=learning, step=1, interval=0:06:00, ease=2.5)),
#   ('good', Card(status=learning, step=1, interval=0:10:00, ease=2.5)),
#   ('easy', Card(status=reviewing, step=0, interval=4 days, 0:00:00, ease=2.5))
# ]

# Printing the interval for each option
for answer, new_card in card.options():
    print(answer, new_card.interval)
# Output:
# again 0:01:00
# hard 0:06:00
# good 0:10:00
# easy 4 days, 0:00:00



# The attributes of the card include:
#status: Indicates the learning phase of the card, initially set to "learning".
#step: Represents the current step in the learning process, initially set to 0.
#interval: The time interval until the card should be reviewed again, initially set to None.
#ease: A factor that influences how quickly the intervals increase, initially set to 2.5.


#The options returned include:

#'again': If the card is answered incorrectly, it remains in the learning phase with a 
# short interval (e.g., 1 minute).#
#'hard': If the card is answered correctly but with difficulty, it stays in the learning phase but
#  the interval is slightly longer (e.g., 6 minutes).
#'good': If the card is answered correctly, the interval increases (e.g., 10 minutes) while still 
# in the learning phase.
#'easy': If the card is answered very easily, it transitions to the reviewing phase with a much 
# longer interval (e.g., 4 days).