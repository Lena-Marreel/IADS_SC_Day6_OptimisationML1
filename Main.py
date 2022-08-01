{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Lena-Marreel/IADS_SC_Day6_OptimisationML1/blob/main/Main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!python \"Main.py\""
      ],
      "metadata": {
        "id": "m1aW59cJlSb0",
        "outputId": "530a4c91-78dc-4b01-cdba-3665a52ab256",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "evaluate():\n",
            "BanditTestBatch: casesIDs: \n",
            "0 \n",
            "1 \n",
            "2 \n",
            "3 \n",
            "4 \n",
            "\n",
            "BanditTestBatch: numCases: 5\n",
            "BanditTestBatch: optimal reward: 1560.0\n",
            "BanditTestBatch: random reward: 1337.5\n",
            "Total repeats: 10\n",
            "\n",
            "Batch performance                By-case performance as: Sum rewards\n",
            "\n",
            "repeats    SumRew   Regret        case01   case02   case03   case04   case05\n",
            "\n",
            "      1   1299.00   261.00        254.00   191.00   145.00   205.00   504.00\n",
            "      2   1309.50   250.50        253.50   210.50   145.50   192.50   507.50\n",
            "      3   1310.00   250.00        257.00   211.67   143.33   197.67   500.33\n",
            "      4   1331.25   228.75        257.50   218.25   148.75   209.25   497.50\n",
            "      5   1333.80   226.20        258.40   221.40   150.80   208.00   495.20\n",
            "      6   1331.33   228.67        258.67   217.50   148.67   210.17   496.33\n",
            "      7   1333.86   226.14        257.86   214.57   148.29   211.43   501.71\n",
            "      8   1331.50   228.50        257.25   214.00   148.13   212.12   500.00\n",
            "      9   1330.11   229.89        256.00   213.67   148.33   214.67   497.44\n",
            "     10   1335.20   224.80        256.20   214.50   148.30   216.50   499.70\n",
            "\n",
            "evaluate(): DONE\n",
            "\n",
            "Your selected algorithm: reward: 1335.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "R5Id7RtrlWzT"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "name": "Welcome to Colaboratory",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}