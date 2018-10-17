# Machine Translation

The goal of this project is to build a Deep Neural Network to accept English sentences and return French translations. The text data is first preprocessed and turned into integers passed through different Neural Network Models which have their performance analyzed to then build a final robust model. The final model is then used to demonstrate the translation task. 

We first built a simple RNN with Gated Recurrent Unit cells (GRU), and then added more complexity. We explored embedding, bidirectionality, and an encoder-decoder.

The dataset used is relatively small compared to typical machine translation datasets like [WMT](http://www.statmt.org/) to avoid long training times.

## Preprocessing
For a neural network to predict on text data, it first has to be turned into data it can understand. Text data like "dog" is a sequence of ASCII character encodings.  Since a neural network is a series of multiplication and addition operations, the input data needs to be number(s).

We can turn each character into a number or each word into a number.  These are called character and word ids, respectively.  Character ids are used for character level models that generate text predictions for each character.  A word level model uses word ids that generate text predictions for each word.  Word level models tend to learn better, since they are lower in complexity, so we'll use those.

When batching the sequence of word ids together, each sequence needs to be the same length.  Since sentences are dynamic in length, we can add padding to the end of the sequences to make them the same length.

## Model Designs
We experimented with the following various neural network architectures.
- Model 1 is a simple RNN (GRU)
- Model 2 is a RNN (GRU) with Embedding
- Model 3 is a Bidirectional RNN (GRU)
- Model 4 is an Encoder-Decoder RNN (GRU)
- Model 5 is a model designed to outperform the last four

## Performance Analysis

The Accuracies achieved:
- `Simple RNN Model`: Simple_Model Accuracy on Test Set: **74.16%**
- `Embedding Model`: Embedded_Model Accuracy on Test Set: **90.79%**
- `Bidirectional Model`: bd_Model Accuracy on Test Set: **80.64%**
- `Encoder-Decoder Model`: encdec_Model Accuracy on Test Set: **64.40%**
- `Final Model`: final_Model Accuracy on Test Set: **93.29%**

We saw the best improvement when we introduced the word embedding technique into our model. It is expected as embeddings in deep learning have shown to be very effective, it pulls words with common "meanings" together.

Next, we also saw improvements by adding bidirectionality to our Recurrent layers which is in a sense adding two parallel independent RNNs. 

We saw a lower accuracy when introducing the encoder-decoder technique, however combining all three techniques together was able to achieve great performance. Therefore, The encoder-decoder has shown to be effective when combined with word embedding and especially, bidirectional recurrent layers.

The final model achieved a **93%** accuracy on the test set.

```
Input = 'he saw a old yellow truck'
Output = 'il a vu un vieux camion jaune'

Input = 'new jersey is sometimes quiet during autumn , and it is snowy in april .'
Output = 'l' inde est le gel habituellement en janvier et il est jamais agréable à l' automne'
```