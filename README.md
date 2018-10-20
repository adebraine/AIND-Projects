# Artificial Intelligence Nano-degree at Udacity

## Facial Keypoint Detection and Real-time Filtering
In this project we explored OpenCV and face detection applications, then build a Facial Keypoint Detection algorithm and finally add a sunglasses filter automatically on each face. We also adapt our algorithm to function on live video.

<img src="Facial Keypoint Detection and Real-time Filtering/images/face4.gif" width="400">
<img src="Facial Keypoint Detection and Real-time Filtering/images/face5.gif" width="400">

## Machine Translation
The goal of this project is to build a Deep Neural Network to accept English sentences and return French translations. The text data is first preprocessed and turned into integers passed through different Neural Network Models which have their performance analyzed to then build a final robust model. The final model is then used to demonstrate the translation task. 

We first built a simple RNN with Gated Recurrent Unit cells (GRU), and then added more complexity. We explored embedding, bidirectionality, and an encoder-decoder.

The dataset used is relatively small compared to typical machine translation datasets like [WMT](http://www.statmt.org/) to avoid long training times.

## Voice User Interface
Built a deep neural network that functions as part of an end-to-end automatic speech recognition (ASR) pipeline!  

## Dog Breed Image Classifier
In this project, we explore Convolutional Neural Networks as a means to classify images. This project remains a learning excerise but could be expanded as a pipeline that can be used within a web or mobile app to process real-world, user-supplied images. Given an image of a dog, our algorithm will identify an estimate of the canine’s breed. If supplied an image of a human, the code will identify the resembling dog breed. 

## Sudoku Game Playing Agent

**Sudoku** consists of a 9x9 grid, and the objective is to fill the grid with digits in such a way that each row, each column, and each of the 9 principal 3x3 subsquares (units) contains all of the digits from 1 to 9. 

The main goal of this project is to build an intelligent agent that will solve every sudoku puzzles. The project introduces two key concepts, **constraint propagation** and **search**.

## Isolation Game Playing Agent

The purpose of this project was to develop an adversarial search agent to play the game "Isolation".  Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board.  Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game.  The first player with no remaining legal moves loses, and the opponent is declared the winner.

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a 7x7 rectangular grid (like a chess or checkerboard).  The agents can move to any open cell granted that it respect the chess knight movement restrictions.

Additionally, agents will have a fixed time limit each turn to search for the best move and respond.  If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins.

Two search agents were implemented in this projects, **MiniMax** and **Alpha-Beta pruning with iterative deepening** along with multiple **Heuristic Functions**.

## Planning Search Agent

The goal of this project is to solve deterministic logistics planning problems for an Air Cargo Transport System using a planning search agent. 

The first step was to implement the different actions, initial states and goals of the problem described bellow then use **uninformed planning search algorithms (non-heuristic)** and compare results obtained.

Then we developed **domain-independent Heuristics** and **Mutual Exclusion Relations (Mutex)** with a **planning graph** and used **A\* Search** in an attempt to find more efficient methodologies. 

The planning graph is a polynomial-size approximation of the exponential tree that represents all possible paths. The planning graph can be used to provide automated admissible heuristics for any domain.

Finally, we compared the results between each methodologies in order to determine optimal solutions for each problem.

## Sign Language Recognition System

The overall goal of this project is to build a word recognizer for American Sign Language video sequences, demonstrating the power of probabalistic models.  In particular, this project employs  [hidden Markov models (HMM's)](https://en.wikipedia.org/wiki/Hidden_Markov_model) to analyze a series of measurements taken from videos of American Sign Language (ASL) collected for research (see the [RWTH-BOSTON-104 Database](http://www-i6.informatik.rwth-aachen.de/~dreuw/database-rwth-boston-104.php)). 

The raw data, train, and test sets are pre-defined.  We derived a variety of feature sets (Part 1), as well as implement three different model selection criterion to determine the optimal number of hidden states for each word model (Part 2). Finally, in Part 3 we implemented the recognizer and compared the effects the different combinations of feature sets and model selection criteria.

## Recurrent Neural Networks: Time Series Prediction and Text Generation

This project consists of two problems. One is to build a Recurrent Neural Network (RNN) to perform time series prediction of stock prices and the other is to build a RNN to generate English sentences character-by-character.