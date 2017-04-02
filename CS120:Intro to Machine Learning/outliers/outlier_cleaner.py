#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    for i in range(len(predictions)):
        cleaned_data.append((ages[i][0],net_worths[i][0], net_worths[i][0] - predictions[i][0]))
    cleaned_data.sort(key = lambda data: data[2])
    cleaned_data = cleaned_data[len(cleaned_data)/10:]
    ### your code goes here

    return cleaned_data

