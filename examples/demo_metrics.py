from taipy.gui import Gui
value = 50

# Create a simple page to demonstrate metrics usage
page = """
# Metrics Demonstration

## Working with Numeric Values
<|{value}|metric|width=150|height=150|>  <!-- Numeric values should display correctly -->

## Using CSS Units for Width and Height
<div style="width: 150px; height: 150px;">
    <|{value}|metric|>  <!-- CSS units applied -->
</div>

<div style="width: 150rem; height: 150rem;">
    <|{value}|metric|>  <!-- CSS units applied -->
</div>

## Custom Height Metric
<|{value}|metric|width=150|height=100|>  <!-- Custom height for layout -->
"""

# Run the GUI with the defined page
Gui(page).run()
