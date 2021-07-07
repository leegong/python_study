{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNRBIRMC0iXp5iSJf/xgNH5",
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
        "<a href=\"https://colab.research.google.com/github/leegong/python_study/blob/master/Untitled0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LGbUqk80th7w",
        "outputId": "092af724-fb24-4dc9-f13b-2d6dd52e6657"
      },
      "source": [
        "class Student():\n",
        "  def __init__(self, name, age):\n",
        "    self.name=name\n",
        "    self.age=age\n",
        "  def smile(self):\n",
        "    print('haha')\n",
        "\n",
        "p1=Student('Jim', 22)\n",
        "\n",
        "print(p1.name)\n",
        "print(p1.age)\n",
        "print(p1.smile())\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Jim\n",
            "22\n",
            "haha\n",
            "None\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}