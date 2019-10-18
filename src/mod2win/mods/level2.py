"""
Welcome to level 2 mod!

It's time to write your first complex function and explore 'for' loops.

A function is an action that normally has inputs and outputs.
We call the inputs arguments or args and the output the return value.

Arguments are variables that you decide to pass to the function so it can do some work and
return a value that you can optionally hold in another variable.

Some functions just have inputs and some just have outputs. There are no special names
for these functions but it is helpful to know they are possible to use.

In Python a function is defined by using the keyword: def
To return a value we simply use the keyword: return

When we want to run a function we say "call the function by it's name".
When we want to provide the function inputs we say "Pass the function arguments"

Example function:

def add(a, b):
    return a + b

In the above, a and b are the functions arguments and their sum is the return value.

To call this function and save its output we can write the following:

Example function call:

sum = add(3, 7)

The variable sum will now store the integer 10.

But what if we want to do some more complex actions, then we need to learn about new structures called loops.

Python provides two main looping structures and we are going to go over one of them called "for"

Sometimes we need to repeat an action over and over again and this takes a lot of time typing.

Let's say we needed to add up all the numbers in a list. This means we would type out all of the items of
the list and use addition to sum them up.

Example:
    numbers = [ 1, 3, 4, 5, 2 ]
    sum = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]

That may seem like a short example but what if our list contained all the integers between 1 and 100.

Example:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99 ]
    sum = numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6] + numbers[7] + numbers[8] + numbers[9] + numbers[10] + numbers[11] + numbers[12] + numbers[13] + numbers[14] + numbers[15] + numbers[16] + numbers[17] + numbers[18] + numbers[19] + numbers[20] + numbers[21] + numbers[22] + numbers[23] + numbers[24] + numbers[25] + numbers[26] + numbers[27] + numbers[28] + numbers[29] + numbers[30] + numbers[31] + numbers[32] + numbers[33] + numbers[34] + numbers[35] + numbers[36] + numbers[37] + numbers[38] + numbers[39] + numbers[40] + numbers[41] + numbers[42] + numbers[43] + numbers[44] + numbers[45] + numbers[46] + numbers[47] + numbers[48] + numbers[49] + numbers[50] + numbers[51] + numbers[52] + numbers[53] + numbers[54] + numbers[55] + numbers[56] + numbers[57] + numbers[58] + numbers[59] + numbers[60] + numbers[61] + numbers[62] + numbers[63] + numbers[64] + numbers[65] + numbers[66] + numbers[67] + numbers[68] + numbers[69] + numbers[70] + numbers[71] + numbers[72] + numbers[73] + numbers[74] + numbers[75] + numbers[76] + numbers[77] + numbers[78] + numbers[79] + numbers[80] + numbers[81] + numbers[82] + numbers[83] + numbers[84] + numbers[85] + numbers[86] + numbers[87] + numbers[88] + numbers[89] + numbers[90] + numbers[91] + numbers[92] + numbers[93] + numbers[94] + numbers[95] + numbers[96] + numbers[97] + numbers[98] + numbers[99]

Now that is a lot of typing.

We can do this more easily by using a 'for loop'

Why is it called a for loop? Well it has to do with the following sentence:

For each thing I have I have in my collection take an item out and do something with it and move onto the next one.
We can use variables to store this temporary thing while we take our action.

Example:
    numbers = [ 1, 2, 3, 4, 5, 6, 7, 8]
    sum = 0
    for number in numbers:
        sum += number

At the end of this the variable sum that started at 0 will now store 36

This makes using large collections much easier. It also allows us to not worry about how long our collection is.

In this module you need to write a function called 'lift_gate' that takes in one argument called gate.
gate will be a list of bricks that have their own variables named center_x and center_y

Example:
    brick = Brick()
    brick.center_y = 5

This will place the brick at location 5 on the vertical y axis. You can ignore how brick got this special variable at this time.

"""


class Mod:
    # Remove the # from the next line to make your function work.
    #@staticmethod
    pass  # replace the word pass with your function!
