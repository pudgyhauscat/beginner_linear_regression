{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM8Vm7rXS3Z/P8+sj5wpabp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/pudgyhauscat/beginner_linear_regression/blob/main/Data_Generator_LRT.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "cuSA5uJBEqcX"
      },
      "outputs": [],
      "source": [
        "#the data generation step included above can be fit into a class and ported out of this program\n",
        "#this will be useful, because we're going to use the same data generation steps in later notebooks. \n",
        "#this class will initialize data sets in the exact same way that we initialized the data set here and \n",
        "#we won't waste time coding it later\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "class data_set_generator:\n",
        "    x_1 = np.random.randint(low = 1, high = 20, size = 100)\n",
        "    x_2 = np.random.randint(low = 1, high = 20, size = 100)\n",
        "    x_3 = np.random.randint(low = 1, high = 20, size = 100)\n",
        "    \n",
        "    def __init__(self):\n",
        "      self.intercept = np.random.randint(low = 1, high = 20, size = 1)\n",
        "      self.X_0 = np.column_stack([x_1, x_2, x_3])\n",
        "      \n",
        "    def calculate_y(self, weight_1, weight_2, weight_3):\n",
        "      linear_y = [weight_1*x for x in x_1]\n",
        "      linear_y_2 = [linear_y[i] + weight_2*x_2[i] for i in range(0,len(x_2))]\n",
        "      linear_y_3 = [linear_y_2[i] - weight_3*x_3[i] for i in range(0, len(x_3))]\n",
        "      self.linear_y = np.array(linear_y_3) + self.intercept\n",
        "      noise = noise = np.random.normal(10, 3, 100)\n",
        "      self.linear_y_noise = [linear_y_3[i] + noise[i] for i in range(0, len(noise))]"
      ]
    }
  ]
}