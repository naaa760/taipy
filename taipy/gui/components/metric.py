# taipy/gui/components/metric.py

def render_metric(value, width='150', height='150'):
    """
    Renders a metric with specified width and height.

    :param value: The value to display in the metric.
    :param width: The width of the metric (can be numeric or CSS units).
    :param height: The height of the metric (can be numeric or CSS units).
    :return: HTML string for the metric.
    """
    # Wrap the metric in a div to apply CSS styles
    html = f'<div style="width: {width}; height: {height}; border: 1px solid black; padding: 10px; box-sizing: border-box;">{value}</div>'
    return html
