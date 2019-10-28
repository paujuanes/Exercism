def slices(series, length):
    if series and len(series)>=length>0:
        return [series[i:i+length] for i in range(len(series)-length+1)]
    else:
        raise ValueError("Sorry, the string cannot be empty and length value must be more than 0 and less than string's length.")

#return [series[i:i+length] if series and len(series)>length>0 else raise ValueError("ValueError") for i in range(len(series)-length+1)]