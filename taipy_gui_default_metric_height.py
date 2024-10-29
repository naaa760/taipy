from taipy.gui import Gui
import taipy.gui.builder as tgb

def create_metric(value, width=None, height=None):
    """
    Create a Taipy GUI metric component with optional width and height.
    
    Parameters:
    value (str): The value to be displayed in the metric.
    width (int or str, optional): The width of the metric. Can be an integer (treated as pixels) or a string with a CSS unit (e.g., "150px", "10rem").
    height (int or str, optional): The height of the metric. Can be an integer (treated as pixels) or a string with a CSS unit (e.g., "300px", "20rem").
    
    Returns:
    tgb.Metric: The Taipy GUI metric component with the specified width and height.
    """
    metric_props = {}
    if width is not None:
        if isinstance(width, int):
            width = f"{width}px"
        metric_props["width"] = width
    if height is not None:
        if isinstance(height, int):
            height = f"{height}px"
        metric_props["height"] = height
    return tgb.metric("{value}", type="none", **metric_props) # type: ignore

# Demonstration of the issue and solution
value = 50

with tgb.Page() as page:
    create_metric(value, width=200, height=100)

Gui(page).run(title="Frontend Demo")