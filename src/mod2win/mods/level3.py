"""
Welcome to level 3 mod!

In this mod you will need to use some old skills with variables and functions while
we introduce the concept of conditionals.

In programming we sometimes need to make decisions based on the value of a variable.

What if we are controlling a robot and it needs to turn off after a certain amount of time.
If we used a variable for time and checked its value against our shut off time we could help
out robot pal.

Example:
    robot = Robot()
    robot.time_on = 15
    if robot.time_on > 5:
        robot.off()

In the above you may notice a few special things. "if" and '>"

We are asking if the robot time on is greater than 5 then we turn off our robot.

We can ask other questions too. What if our robot's time_on is less than something? or equal to something?

Example:
    if robot.time_on == 10:
        robot.dance()

We use the equal sign twice to ask the question is something equals something else.
We need to use it twice because = was already taken to give values to our variables.

Here are all the questions we can ask:
 * > (Greater than)
 * < (Less than)
 * >= (Greater than or equal to)
 * <= (Less than or equal to)
 * == (equal to)

There is one more type of variable that really helps with conditionals and asking questions.
Sometimes you need to ask yes or no questions and a number response just won't help.
What if we need to ask a question like is our robot dancing?

Example:
     if robot.is_dancing() is True:
         play_music()

Notice how we asked the question with 'is True'
True in this case is called a boolean value which there are only 2 of:
 * True
 * False

We expect the is_dancing function to return a boolean of True or False based on the robot's state.
We then compare this return to the word True or False to take action.

In this mod you'll have access to the following variables:
 * num_coins (integer)
 * jump_speed (float)

You'll need to write a function named collect_coin that takes in an argument called color

The following colors are available:
 * 'blue'
 * 'gold'
 * 'green'
 * 'orange'
 * 'pink'
 * 'purple'
 * 'red'

When you come across a color you should return a score for it.

Example:
    def myFunc(variable_name)
    if variable_name == "colorName":
        return 10
    ...
"""


class Mod:
    # Place your variables on the next line
    # num_coins = 20
    # jump_speed = 10

    # Remove the # from the next line to make your function work
    #@staticmethod
    pass  # write your function here
    # def collect_coin(color):

    @staticmethod
    def win():
        # This can't be good!
        return False
