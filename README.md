# Plastic Classification Using CNN
This project uses a Convolutional Neural Network (CNN) to classify plastic waste into different categories. By leveraging deep learning, the model helps in the automated sorting of plastic types, facilitating efficient recycling and waste management.

## Features
#### Deep Learning Model: 
Built with TensorFlow/Keras to classify plastic waste images.

Preprocessing: 
Includes data augmentation and normalization for enhanced accuracy.

#### Efficient Classification: 
Categorizes plastic waste into predefined classes.

#### Customizable: 
The model architecture can be fine-tuned for specific datasets.

## Requirements
Before running the project, ensure you have the following installed:

#### Python (>= 3.7)
#### TensorFlow/Keras
#### NumPy
#### Matplotlib
#### OpenCV
#### Scikit-learn
#### Pandas

### Install dependencies with:

bash
Copy code
pip install -r requirements.txt

### Dataset
The dataset used in this project contains images of plastic waste categorized into multiple classes.

### Source:

#### javascript
/dataset/
    /train/
        /class_1/
        /class_2/
        ...
    /test/
        /class_1/
        /class_2/
        ...
## Model Architecture
### The CNN architecture includes:

Convolutional Layers for feature extraction
MaxPooling Layers for dimensionality reduction
Dense Layers for classification
Dropout for regularization
Model Summary:



Training the Model
To train the model:

### Clone the repository:
#### bash
git clone https://github.com/ShubhamDwn/Plastic_Classification_using_CNN.git
cd Plastic_Classification_using_CNN
Prepare your dataset in the specified format.
Run the training script:
#### bash
python train.py
The trained model will be saved as model.h5 in the project directory.
Evaluating the Model
To evaluate the model's performance:

#### bash
python evaluate.py
This script outputs metrics like accuracy, precision, recall, and confusion matrix.


## Usage
To use the trained model for predictions:

bash
Copy code
python predict.py --image path/to/image.jpg
The script outputs the predicted class and confidence score.

## Future Enhancements
Add more plastic categories for finer classification.
Use transfer learning with pre-trained models like ResNet or EfficientNet.
Implement real-time classification using a webcam feed.
Contributing
Contributions are welcome! If you have ideas or suggestions, feel free to fork the repository and submit a pull request.


## Author
Developed by Shubham Ekanath Dhavan, Asashish Mulani, Prachi Wandre, Samruddhi Patil.
Feel free to reach out for collaborations or queries!

