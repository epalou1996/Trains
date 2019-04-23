# Trains

Hi, this is an early python code i wrote to calculate the collision of 2 trains that part from the same point and that are in the same line, its pretty much basic and dirty, but in the momment made me a little proud.

The code is in spanish, so are the notes and prints in console, therefore i will explain how it works in a short way in here
(I could translate it, but i want to mantain it the same way it was written)

The first part is a set of prints and inputs to set the user, and ask for the parameters to run the program.
Then the user inputs the aceleration of each train, the time between their starts, and the topspeed of both trains.
If the first train starts with more aceleration, then the collision is not going to happen, so the program runs an if, that print this and finish the program.

Then some variables are calculated, some are easier(time to get topspeed, difference between acelerations, the power of the brakes which is limited) and the other ones that are represented by leters are product of the diferential ecuations i used to solve the problem in paper. The ecuation to get the precise time of collision in wich the train 2 could full-brake, and still hit the train1, was big, so some terms were replaced by these letters to make it clearer to me.

The time of the crash before brakes, is calculated via cuadratic ecuation, the absurd result is turned down by the program, and reports the time in which they will collide if no action is taken, after that, calculates the lowest time of possible collision if the second train starts with the aceleration given, and then full-brakes in the last momment possible, and print the result.

if you are interested in the logic of the physics, contact me. thank you if you take your time to read this, and have a nice day!
Also if you have any advice for a new guy in GitHub, i will be grateful.

gmail: eduardopalou96@gmail.com
