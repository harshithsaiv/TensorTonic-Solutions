def double_exponential_smoothing(series: list, alpha: float, beta: float) -> list:
    """
    Returns the smoothed level at every time step.
    """

    # Initial level
    level = series[0]

    # Initial trend
    trend = series[1] - series[0]

    # Include the initial level
    levels = [level]

    # Process observations starting from the second value
    for i in range(1, len(series)):
        previous_level = level

        # Update level first
        level = alpha * series[i] + (1 - alpha) * (previous_level + trend)

        # Then update trend using the NEW level
        trend = beta * (level - previous_level) + (1 - beta) * trend

        levels.append(level)

    return levels