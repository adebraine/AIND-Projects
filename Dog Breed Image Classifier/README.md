[//]: # (Image References)

[image1]: ./images/sample_dog_output.png "Sample Output"
[image2]: ./images/vgg16_model.png "VGG-16 Model Keras Layers"
[image3]: ./images/vgg16_model_draw.png "VGG16 Model Figure"


## Project Overview
In this project, we explore Convolutional Neural Networks as a means to classify images. This project remains a learning excerise but could be expanded as a pipeline that can be used within a web or mobile app to process real-world, user-supplied images. Given an image of a dog, our algorithm will identify an estimate of the canine’s breed. If supplied an image of a human, the code will identify the resembling dog breed. 

![Sample Output][image1]

We first built a Convolutional Neural Network (CNN) from scratch then compared its performance to a CNN built with transfer learning from the ResNet-50 Model.

## CNN from Scratch
At first we started with 5 epochs and Loss plot callback function written below to get some intuition of how changing parameters affected the accuracy. We decided to keep training time low as this project is a learning exercise.

We started with started with a model comprised of three Convolutional layers and with **[2, 4, 8] filters** and no global average pooling. We started with a low amount of trainable parameters and build up from that. We decided to take that approach to build some intuition. 

We added a **hidden layer with 256 nodes** to the MLP at the end of the CNN as a way to add more complexity to the network, thinking that adding a layer would  enable it to fit to a wider range of patterns and since it was its first hidden layer, we didn't think that it would overfit. However, this lead to a model with too many trainable parameters for my computer to train in a reasonable amount of time, **3,203,331 parameters**. We then decided to add a global average pooling layer to reduce the amount of trainable parameters to just **71,331**. We trained the model and it lead to an accuracy of **1.67%** after 5 epochs.

The next step was to **increase the number of filters** and see how the model behaved, we first started with **[16, 32, 64] filters** as described above which lead to **109,677** parameters. The idea was that more filters would allow the network to see a wider range of patterns and by adding more filters for the deeper layer that should see more complex shapes would benefit more from the added amount of filters. This approach led to an accuracy of **2.2727%** which was a good improvement over the previous approach. We then decided to further increase the **number of filters to [64, 128, 256]** for **360,189** trainable parameters and an accuracy of **2.6316%**. Less of an improvement jump that previously seen.

Finally, plotting the training losses and validation losses live while **increasing the number of epochs by 5** seemed to lead to significant improvements but settled at **50 epochs** due to the enormous increase in training time. The final accuracy achieved was **16.7%** and **14.8%** as the model was ran twice.

In conclusion, we plan to further experiment with hyperparameters to build more conclusive intuitions but it would have to be done over time as repeated training is very time consuming.

## CNN from Transfer Learning
We started with the VGG16 architecture but then settled on using the ResNet-50 model, we experimented with the following:
- **[1, 2]** dense layers with **[100, 300, 1000, 2000]** nodes
    - The results were fairly unconclusive, the accuracy hovered around 83% but dropped to 78% when using a too small amount of nodes. Using no dense layers but only an output layer resulted again in an accuracy hovering around 83%. Therefore, we don't think adding more dense layers added much benefits. However, what we did see is that the validation losses remained below the training losses longer if using those dense layers.
- **[10, 20, 32, 64]** Batch size
    - Changing the batch size lead to very different accuracies, 10 being the lowest and 32 being the best accuracy. However, 64 was very close with a notable increase in training speed. 
- **[Flatten, GlobalAveragePooling, GlobalMaxPooling]** as a starting layer
    - These produced very similar results. however, flatten seem to consistantly give 1% additional test accuracy and decided to go with that one.
- **[Dropout(0.5), Dropout(0.2), No Dropout]** layers
    - It seemed that Dropout(0.5) gave the best results, we imagine that it helped with over-fitting. The increase in accuracy wasn't too noticable, close to 1%.
- **[SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax, Nadam]** optimizers
    - Adadelta seemed to give the best results. Only this optimizer lead to an accuracy beyond 83%.
- **[5, 10, 20, 30, 50, 100]** epochs
    - We saw significant improvements in accuracy from 5 to 30 epochs but a fairly insignificant increase beyond that but with a large increase in training time. We did not see the advantage of going beyond 30 epochs as the accuracy seemed to be close to identical afterwards.

In conclusion, it seemed that the simpler model, with no additional layers,  provided good accuracy (around 82%) and was faster to train. However, a slightly more complex model did seem to increase the test accuracy a bit. A trade-off between training time and accuracy is apparent. We imagine that more fine-tuning could lead to an even bigger increase in accuracy.

## Predictions
We tried to choose dog images that a slightly different than a standard dog profile picture. We chose one with a dog slightly contorted jumping position and one zoomed in image. The results are either accurate or very close. The first one was hard for me to identify and could very well be a smooth for terrier but it isn't as obvious. The second one is a border collie but was identified as an english_setter which have a somewhat similar facial structure but have a more spotty color pattern. These results let me to believe that a sort of image augmentation of the dataset to increase the number of unorthodox inputs could potentially improve the accuracy in these less obvious situations. 

![](images/1.png)
![](images/2.png)

The human to dog breed matching was very entertaining and we can see some resemblance in the images. My picture led to two different images whenever we retrained the algorithm, English_toy_spaniel or Havanese. Both are fairly round faced hairy dogs and we have a fairly round face with a beard.

![](images/3.png)

In conclusion, to improve the algorithm, we would explore image augmentation, further fine tuning of hyper parameters and exploring other algorithms to transfer learn from.
