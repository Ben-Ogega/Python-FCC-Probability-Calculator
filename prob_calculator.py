import copy
import random


class Hat:
    def __init__(self, **args):

        self.contents = []

        for i, j in args.items():
            for k in range(j):
                self.contents.append(i)

    def draw(self, no_of_balls_drawn):
        # if no_of_balls_drawn > len(self.contents):
        #     return self.contents
        no_of_balls_drawn = min(no_of_balls_drawn, len(self.contents))
        # we set an empty list into which we will populate the number of balls drawn
        balls_drawn = []
        # since this is a random process, we will loop through the range of the number of balls drawn,
        # and noting the random number of balls drawn, ie 3, 3, 2 etc.
        for i in range(no_of_balls_drawn):
            rand_integer = random.randint(0, len(self.contents) - 1)
            balls_drawn.append(self.contents[rand_integer])  # appending the number of balls drawn at index rand_int
            self.contents.pop(rand_integer)

        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []  # An empty list that will hold the expected number of balls.
    # Iterate through the range of the number of experiments
    for i, j in expected_balls.items():
        for k in range(j):
            expected.append(i)

    Success_count = 0  # creating our success count and initially setting it to zero.

    # Create a deepcopy of the hat from the Hat class
    # Draw balls from the hat using the draw method that is in the Hat class

    # Deepcopy the contents of the Hat class...

    contents_copy = copy.deepcopy(hat.contents)
    # Initialize the second count, that is the color count.
    # ie (color_count)

    for item in range(num_experiments):
        balls_drawn = hat.draw(num_balls_drawn)
        hat.contents = copy.deepcopy(contents_copy)
        color_count = 0

        for i in expected:
            for j in balls_drawn:

                if i == j:
                    color_count += 1
                    balls_drawn.pop(balls_drawn.index(j))
                    break

            if color_count == len(expected):
                Success_count += 1

    return Success_count / num_experiments
