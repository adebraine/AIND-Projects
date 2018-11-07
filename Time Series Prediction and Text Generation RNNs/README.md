# Recurrent Neural Networks: Time Series Prediction and Text Generation

This project consists of two problems. One is to build a Recurrent Neural Network (RNN) to perform time series prediction of stock prices and the other is to build a RNN to generate English sentences character-by-character.

## Time Series Prediction
The Network architecture explored in this project is an RNN using Long Term Short Term Memory (LSTM) cells. The model is trained on a dataset consisting of daily stock prices. We first normalized the data to avoid issues with the activation functions and cut the data into `windows` consisting of sequences of prices of a determined length followed by the next immediate price value as illustrated below. This methodology allows us to isolate price values that are right before a prediction.

<img src="images/timeseries_windowing_training.gif"/>

The model architecture chosen was a two layer RNN with an LSTM layer and an output layer with a single value as it is a regression problem.

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm_36 (LSTM)               (None, 50)                10400     
_________________________________________________________________
dense_18 (Dense)             (None, 1)                 51        
=================================================================
Total params: 10,451.0
Trainable params: 10,451
Non-trainable params: 0.0
_________________________________________________________________
```

The model showed a surprisingly good performance for its simplicity. The idea will be explored further in a different project. 

![](images/predict.png)

## Text Generation
The goal of this project is to train an RNN on a novel and generate sentences similar to the ones found in the novel. The model generates text automatically character-by-character. The data consist of a complete version of Sir Arthur Conan Doyle's classic book The Adventures of Sherlock Holmes. The text is first pre-processed to eliminates unwanted characters and leave only words and punctuations. The same `window` concept is applied as seen below. 

![](images/text_windowing_training.gif)

The model architecture chosen was a two layer RNN with an LSTM layer and an output layer with 33 possible outputs that represent all uniques characters in the dataset. It is a classification problem.

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm_2 (LSTM)                (None, 200)               187200    
_________________________________________________________________
dense_2 (Dense)              (None, 33)                6633      
_________________________________________________________________
activation_1 (Activation)    (None, 33)                0         
=================================================================
Total params: 193,833
Trainable params: 193,833
Non-trainable params: 0
_________________________________________________________________
```

While the model was able to generate English words, it wasn't able to generate proper sentences but it is expected with such a small architecture and dataset. Natural Language Processing concepts are explored further in the Machine Translation project.

    input chars = 
    in to love for irene adler. all emotions, and that one particularly, were abhorrent to his cold, pre"

    predicted chars = 
    ptisters on his hand and expeated in the sintory as his light and as and leaking before i fan the ot"