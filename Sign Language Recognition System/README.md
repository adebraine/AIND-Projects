# Sign Language Recognition System

The overall goal of this project is to build a word recognizer for American Sign Language video sequences, demonstrating the power of probabalistic models.  In particular, this project employs  [hidden Markov models (HMM's)](https://en.wikipedia.org/wiki/Hidden_Markov_model) to analyze a series of measurements taken from videos of American Sign Language (ASL) collected for research (see the [RWTH-BOSTON-104 Database](http://www-i6.informatik.rwth-aachen.de/~dreuw/database-rwth-boston-104.php)).  In this video, the right-hand x and y locations are plotted as the speaker signs the sentence.
[![ASLR demo](http://www-i6.informatik.rwth-aachen.de/~dreuw/images/demosample.png)](https://drive.google.com/open?id=0B_5qGuFe-wbhUXRuVnNZVnMtam8)

The raw data, train, and test sets are pre-defined.  We derived a variety of feature sets (Part 1), as well as implement three different model selection criterion to determine the optimal number of hidden states for each word model (Part 2). Finally, in Part 3 we implemented the recognizer and compared the effects the different combinations of feature sets and model selection criteria.  

An example frame is shown here:

![](http://www-i6.informatik.rwth-aachen.de/~dreuw/database/rwth-boston-104/overview/images/orig/098-start.jpg)

# Table of Contents
1. [Feature Selection](#Feature_Selection)
2. [Model Selection](#Model_Selection)
3. [Recognizer](#Results)

# Feature Selection

The objective of feature selection when training a model is to choose the most relevant variables while keeping the model as simple as possible, thus reducing training time.

To build a training set, we need to collect the features for all the words in the training set. Each word in the training set has multiple examples from various videos.

The features selected are as follows:

- normalized Cartesian coordinates
    - used *mean* and *standard deviation* statistics and the [standard score](https://en.wikipedia.org/wiki/Standard_score) equation to account for speakers with different heights and arm length
    
- polar coordinates
    - calculated polar coordinates with [Cartesian to polar equations](https://en.wikipedia.org/wiki/Polar_coordinate_system#Converting_between_polar_and_Cartesian_coordinates)
    - used the [np.arctan2](https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.arctan2.html) function and *swapped the x and y axes* to move the $0$ to $2\pi$ discontinuity to 12 o'clock instead of 3 o'clock. By swapping the x and y axes, that discontinuity move to directly above the speaker's head, an area not generally used in signing.

- delta difference
    - used the difference in values between one frame and the next frames as features

- Normalized and standardized polar coordinates
    - We decided to focus on the polar coordinates feature and compare the effect of a normalization and standardization of said feature.
    - The polar coodinates feature yielded the best preliminary resuts between all requested features. Standardization and normalization are common methodologies to ensure that all the different inputs in a data set have a similar scale and aren't orders of magnitude different from each other. This allows for data to be comparable.
    - The methodologies chosen were, a normalization around the mean, and a standardization of the data (mean of 0, std of 1).

# Model Selection
The objective of Model Selection is to tune the number of states for each word HMM prior to testing on unseen data.  We implemented three methods: 
- Log likelihood using cross-validation folds (CV)
- Bayesian Information Criterion (BIC)
- Discriminative Information Criterion (DIC) 

#### Cross-validation folds
If we simply score the model with the Log Likelihood calculated from the feature sequences it has been trained on, we should expect that more complex models will have higher likelihoods. However, that doesn't tell us which would have a better likelihood score on unseen data.  The model will likely be overfit as complexity is added.  To estimate which topology model is better using only the training data, we can compare scores using cross-validation.  One technique for cross-validation is to break the training set into "folds" and rotate which fold is left out of training.  The "left out" fold scored.  This gives us a proxy method of finding the best model to use on "unseen data". In the following example, a set of word sequences is broken into three folds using the [scikit-learn Kfold](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html) class object. We implemented this technique in `SelectorCV`.

#### Scoring models with other criterion
Scoring model topologies with **BIC** balances fit and complexity within the training set for each word.  In the BIC equation, a penalty term penalizes complexity to avoid overfitting, so that it is not necessary to also use cross-validation in the selection process.  There are a number of references on the internet for this criterion.  These [slides](http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf) include a formula you may find helpful for your implementation.

The advantages of scoring model topologies with **DIC** over BIC are presented by Alain Biem in this [reference](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf) (also found [here](https://pdfs.semanticscholar.org/ed3d/7c4a5f607201f3848d4c02dd9ba17c791fc2.pdf)).  DIC scores the discriminant ability of a training set for one word against competing words.  Instead of a penalty term for complexity, it provides a penalty if model liklihoods for non-matching words are too similar to model likelihoods for the correct word in the word set.

#### Advantages and Disadvantages
The Bayesian Information Criterion (BIC) maximizes the likelihood of the data while penalizing large-size models. By penalizing large models, BIC is able to deal with overfitting, over-fitted models are those with high complexity. For our application, BIC is the fastest model to train which is a significant advantage. 

The average log likelihood cross validation model (CV) doesn't try to find the model that works "best" unlike BIC but rather to find the model with the best out of sample predictive accuracy. CV deals with overfitting by using k folds, in other words an overfitted model will be found by continuously changing the out of sample set.

The discriminative information criterion (DIC) (According to http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf) shows an 18% improvement over the BIC. However, it is a more complex model and takes a lot more time to compute for our application. It maximizes the likelihood of the data while minimizing the likelihood that the data belongs to another competing classification group. 

# Recognizer
The objective of this section is to "put it all together".  Using the four feature sets created and the three model selectors, we experimented with the models and presented our results below.  Instead of training only five specific words as in the previous section, we trained the entire set with a feature set and model selector strategy.  

#### The results are summarized below:

**We decided to exclude the DIC model as it was taking a considerable amount of time to run.**

| Model    | Features           | WER     | Correct_Readings | Total_Readings | Time_Seconds |
| :------- | :----------------- | :------ | :--------------- | :------------- | :----------- |
| CV       | Polar_Mean_Norm    | 0.45506 | 97               | 178            | 184.384197   |
| BIC      | Polar_Standardized | 0.52247 | 85               | 178            | 81.081174    |
| CV       | Polar_Standardized | 0.52809 | 84               | 178            | 174.424786   |
| BIC      | Polar_Mean_Norm    | 0.53933 | 82               | 178            | 75.417659    |
| BIC      | Polar              | 0.54494 | 81               | 178            | 81.599614    |
| BIC      | Ground             | 0.55056 | 80               | 178            | 80.490078    |
| CV       | Polar              | 0.55618 | 79               | 178            | 191.050865   |
| CV       | Ground             | 0.59551 | 72               | 178            | 165.715989   |
| CV       | Norm               | 0.60674 | 70               | 178            | 186.061091   |
| BIC      | Norm               | 0.61236 | 69               | 178            | 83.534748    |
| Constant | Polar              | 0.61798 | 68               | 178            | 24.738856    |
| BIC      | Delta              | 0.61798 | 68               | 178            | 90.241075    |
| Constant | Norm               | 0.62360 | 67               | 178            | 24.780451    |
| CV       | Delta              | 0.63483 | 65               | 178            | 202.013700   |
| Constant | Delta              | 0.64045 | 64               | 178            | 25.251380    |
| Constant | Ground             | 0.66854 | 59               | 178            | 23.819365    |

According to the table above, the `CV` and `BIC` models were significantly better than the `Constant` model as expected. Both the CV and BIC are more complex and proven selection models. Additionally, we can see from the requested features that the `polar` feature lead to superior results for all selection models. From that initial conclusion, we decided to implement variants of the `polar` feature.

Our two custom features were a normalized polar feature and a standardized polar feature. Both allowed for more similarily scaled data and lead to improved results compared to their non-standardized/normalized counter part. While the standardized feature lead to better results than the normalized feature for the `BIC` selection model, they both lacked compared to the normalized feature used with the `CV` selection model. We were also interested in the `DIC` selection model which should have lead to improved results according to our research but we decided to cancel the computation after it exceeded *two hours*. 

Our initial assumption that a set of data either normalized or standardized would improve results by ensuring comparability between datasets seem to be validated. Additionally, normalization reduces the "weight" of outliers which could be a reason why it outperformed the standardization feature.

In conclusion, the `normalized polar` feature along with the `CV` model selection can be considered "best" according to our results.

To improve our WER even more, we could explore a more efficient way to implement the `DIC` algorithm to reduce the computation time. Additionally, we could implement **word associations** to see which word go along with other words more often, more specifically which verb go with which noun more often. 
