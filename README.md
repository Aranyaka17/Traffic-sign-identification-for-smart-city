# Traffic-sign-identification-for-smart-city
 
 ## Summary:
 The project is a classification problem.The project focuses on identifing traffic signs for smart cities and autonomous vehicle.A deep learning model has been developed to correctly identify these images.Alexnet has been used to solve this problem.
 
 ## Dataset:
 The traffic sign classifier uses a German traffic dataset. The German traffic dataset consists of 39209 32*32 pixels colored images that is used for the training dataset, 12,630 images are used for the testing dataset and 4410 images are used in the validation dataset where each images is a photo of a traffic sign belonging to one of the 43 classes i.e., traffic sign types.

### Link for dataset:  https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip

## Model Architecture:
AlexNet architecture has been used here. The architecture consists of eight layers: five convolutional layers and three fully-connected layers. But this isn’t what makes AlexNet special.

  * It has 8 layers with learnable parameters.
 
  * The input to the Model is RGB images.
 
  * It has 5 convolution layers with a combination of max-pooling layers.
 
  * Then it has 3 fully connected layers.
 
  * The activation function used in all layers is Relu.
 
  * It used two Dropout layers.
 
  * The activation function used in the output layer is Softmax.
 
  * The total number of parameters in this architecture is 24,677,335.

## Demo App:

![image](https://user-images.githubusercontent.com/67574459/114774029-637cb980-9d8d-11eb-8d9e-04ae08d07dea.png)
