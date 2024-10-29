from taipy.gui import Gui

def create_metric(value, width=None, height=None):
    """
    Create a Taipy GUI metric component with optional width and height.
    
    Parameters:
    value (str): The value to be displayed in the metric.
    width (int or str, optional): The width of the metric. Can be an integer (treated as pixels) or a string with a CSS unit (e.g., "150px", "10rem").
    height (int or str, optional): The height of the metric. Can be an integer (treated as pixels) or a string with a CSS unit (e.g., "300px", "20rem").
    
    Returns:
    str: The HTML markup for the metric component with the specified width and height.
    """
    if width is not None:
        if isinstance(width, int):
            width = f"{width}px"
    if height is not None:
        if isinstance(height, int):
            height = f"{height}px"
    return f"<|{value}|metric|width={width}|height={height}|>"

# Demonstration of the issue and solution
value = 50

page = """
{create_metric(value)}           ## Works
{create_metric(value, width=300, height=300)}  ## Height working, Width working
{create_metric(value, width="150px", height="300px")}
{create_metric(value, width="300px", height="300px")}  ## Height working, Width working
{create_metric(value, width="150rem", height="150rem")}
{create_metric(value, width="300rem", height="150rem")}
"""

Gui(page).run()