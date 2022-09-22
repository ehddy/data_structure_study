import math
import matplotlib.pyplot as plt


N = 10

upperFunction = lambda n: int(math.pow(2, n))
lowerFunction = lambda n: int(math.pow(2, n*0.5))
similarFunction = lambda n: int(math.pow(2, n*0.72))


def abc(N):
    global gTotalCount

    if N <= 0:
        return 1

    gTotalCount += 1

    return abc(N-1) + abc(N-2)


def gatherData():
    global gTotalCount

    resultCounts = []

    upperValues = []
    lowerValues = []
    similarValues = []

    print("Data is gathering...")

    for n in range(N):
        print(f"  current input size is '{n:2}'.")

        gTotalCount = 0
        abc(n)

        resultCounts.append(gTotalCount)

        upperValues.append(upperFunction(n))
        lowerValues.append(lowerFunction(n))
        similarValues.append(similarFunction(n))

    print("done.")

    return resultCounts, upperValues, lowerValues, similarValues


def visualizeData(resultCounts, upperValues, lowerValues, similarValues):
    figure = plt.figure("1.13.py")
    axes = figure.add_subplot()

    axes.plot(resultCounts, label="Result")
    axes.plot(upperValues, label=r"$2^N$", linestyle="--")
    axes.plot(similarValues, label=r"$2^{0.72N}$", linestyle="--")
    axes.plot(lowerValues, label=r"$2^{\frac{N}{2}}$", linestyle="--")

    axes.legend(loc="upper left")

    axes.set_xlabel(r"$N$")
    axes.set_ylabel(r"$T(N)$")

    axes.set_ylim([0, 150])

    plt.tight_layout()
    plt.show()


# Gather data. 
resultCounts, upperValues, lowerValues, similarValues = gatherData()

# Visualize data.
visualizeData(resultCounts, upperValues, lowerValues, similarValues)
