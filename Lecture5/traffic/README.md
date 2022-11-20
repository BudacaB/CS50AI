Experimenting with the Convolutional Neural Network configuration, I noticed that adding convolutional layers brings a considerable increase
in accuracy, but this does run into diminishing returns pretty quick beyond a point. Also, an increase in the number of filters seems to lead to
an increase in accuracy as well.

I noticed that there is a slight decrease in accuracy with increased numbers of pooling layers, even if with a small pool size, but this does
seem to bring an increase in processing speed of the application due to the size reduction. The same holds for larger pool sizes.

The accuracy seems to be much better for hidden layers of a bigger size, regardless of the number of layers.

For the dropout, the accuracy is better for a low to medium dropout, higher dropout leads to a major drop in accuracy due to the increased
gap in the network.