# Flappy-bird-AI
Flappy bird game with AI (Using ANN with Genetic algorithm)

About:- This is a game made using pygame library and the AI is added using NEAT(NeuroEvolution of Augmenting Topologies). NEAT uses combinations of genetic algorithm and artificial neural network for learning. This game just is made to demonstrate the learning phase of the algorithm. Still one can store the final chromosome in a file which can be used as final solution to the game.

How its done?

The genetic algorithm produces generation of chromosomes. These are used as input to a neural network. Depending on the results given when a chromosome is applied, it is given a fitness value. And NEAT then uses this fitness value to select few chromosomes to generate new generation. this is done till we find a chromosome which works fine for the given application. We can store this chromosome as result and use it to generate same result every time.

In our game we made the naural network play our game. This is done by passssing environment to the nearal netwrok. In our case we passed location of bird and the gap between the pipes to the ANN and it tells when to jump. And depending on how much time a bird survives the game we set the fitness. This way over a period of generations we get to a point where brid chromosome fimally knows how to play the game.

Some limitations:
NEAT in itself is fast but its speed is limited by fitness calculation function. Like in our case fitness is calculated during a single round of the game. So if a single round goes on for 1hr and we have to have 100 such rounds then total time to run the algorithm will be 100hrs. But if fitness function takes 1 sec then 100 round will take 100 sec only.
So NEAT must be used where the fitness calculation function can be executed in short time.
