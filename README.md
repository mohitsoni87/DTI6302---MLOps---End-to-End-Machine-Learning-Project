# Fashion MNIST Model Training and Hyperparameter Tuning

This Jupyter notebook demonstrates the training of Convolutional Neural Networks (CNN) and Feedforward Neural Networks (FNN) on the Fashion MNIST dataset using TensorFlow and Keras. Additionally, it leverages the Keras Tuner library for hyperparameter optimization using Bayesian Optimization.

## Table of Contents
1. [Installation](#installation)
2. [Imports](#imports)
3. [Data Loading and Preprocessing](#data-loading-and-preprocessing)
4. [Constants and TensorBoard Setup](#constants-and-tensorboard-setup)
5. [Model Builders](#model-builders)
6. [Hyperparameter Tuning](#hyperparameter-tuning)
7. [Model Evaluation and Selection](#model-evaluation-and-selection)
8. [Saving the Best Model](#saving-the-best-model)

## Installation
To run this notebook, you need to install the `keras-tuner` library. You can install it using the following command:

```bash
pip install keras-tuner
