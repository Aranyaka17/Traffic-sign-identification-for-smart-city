# Traffic-sign-identification-for-smart-city
 
 ## Summary:
 The project is a classification problem.The project focuses on identifing traffic signs for smart cities and autonomous vehicle.A deep learning model has been developed to correctly identify these images.Alexnet has been used to solve this problem.
 
 ## Dataset:
 The traffic sign classifier uses a German traffic dataset. The German traffic dataset consists of 39209 32*32 pixels colored images that is used for the training dataset, 12,630 images are used for the testing dataset and 4410 images are used in the validation dataset where each images is a photo of a traffic sign belonging to one of the 43 classes i.e., traffic sign types.

### Link for dataset:  https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip

## Model Architecture:
AlexNet architecture has been used here. The architecture consists of eight layers: five convolutional layers and three fully-connected layers. But this isn’t what makes AlexNet special.

Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 32, 32, 96)        34944     
_________________________________________________________________
batch_normalization (BatchNo (None, 32, 32, 96)        384       
_________________________________________________________________
activation (Activation)      (None, 32, 32, 96)        0         
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 16, 16, 96)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 16, 16, 256)       614656    
_________________________________________________________________
batch_normalization_1 (Batch (None, 16, 16, 256)       1024      
_________________________________________________________________
activation_1 (Activation)    (None, 16, 16, 256)       0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 8, 8, 256)         0         
_________________________________________________________________
zero_padding2d (ZeroPadding2 (None, 10, 10, 256)       0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 10, 10, 512)       1180160   
_________________________________________________________________
batch_normalization_2 (Batch (None, 10, 10, 512)       2048      
_________________________________________________________________
activation_2 (Activation)    (None, 10, 10, 512)       0         
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 5, 5, 512)         0         
_________________________________________________________________
zero_padding2d_1 (ZeroPaddin (None, 7, 7, 512)         0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 7, 7, 1024)        4719616   
_________________________________________________________________
batch_normalization_3 (Batch (None, 7, 7, 1024)        4096      
_________________________________________________________________
activation_3 (Activation)    (None, 7, 7, 1024)        0         
_________________________________________________________________
zero_padding2d_2 (ZeroPaddin (None, 9, 9, 1024)        0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 9, 9, 1024)        9438208   
_________________________________________________________________
batch_normalization_4 (Batch (None, 9, 9, 1024)        4096      
_________________________________________________________________
activation_4 (Activation)    (None, 9, 9, 1024)        0         
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 4, 4, 1024)        0         
_________________________________________________________________
flatten (Flatten)            (None, 16384)             0         
_________________________________________________________________
dense (Dense)                (None, 512)               8389120   
_________________________________________________________________
batch_normalization_5 (Batch (None, 512)               2048      
_________________________________________________________________
activation_5 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout (Dropout)            (None, 512)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               262656    
_________________________________________________________________
batch_normalization_6 (Batch (None, 512)               2048      
_________________________________________________________________
activation_6 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 43)                22059     
_________________________________________________________________
batch_normalization_7 (Batch (None, 43)                172       
_________________________________________________________________
activation_7 (Activation)    (None, 43)                0         
=================================================================
Total params: 24,677,335
Trainable params: 24,669,377
Non-trainable params: 7,958
_________________________________________________________________
