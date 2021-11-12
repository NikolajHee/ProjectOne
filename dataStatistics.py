

#Skrevet af Nikolaj Hertz
#s214644
import numpy as np
import warnings


def dataStatistics(data, statistic):
    """
    Parameters
    ----------
    data: Nx3 matrix with colums temperature, groth rate and bacteria.
    statistic: required statistical scalar.

    Returns
    -------
    Scalar, the result of the statistical measurement.  
    """
    temp = data[:, 0]
    growth_Rate = data[:, 1]
    bacteria = data[:, 2]
    errorMsg = 'Wrong input.'

    rows, col = np.shape(data)

    statStr = np.array(["mean temperature", "mean growth rate", "std temperature", "std growth rate",
                        "rows", "mean cold growth rate", "mean hot growth rate"])
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        statFlo = np.round(np.array([np.mean(temp), np.mean(growth_Rate), np.std(temp), np.std(growth_Rate),
                                     rows, np.mean(temp[temp < 20]), np.mean(temp[temp > 50])]), 3)

    # sikkerhedsnet for hvis parameteren statistic har en udefineret værdi
    if not np.any((statStr == statistic.lower())):
        return errorMsg

    # array med den efterspurgte statistiske værdi
    expectedStat = ((statStr == statistic.lower()) * statFlo)

    try:
        result = expectedStat[expectedStat != 0][0]
    except IndexError:
        result = 0.0
    finally:
        return result