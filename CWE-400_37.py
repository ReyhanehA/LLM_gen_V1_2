#8.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large image without checking its size, leading to potential memory exhaustion
from PIL import Image

img = Image.new('RGB', (100000, 100000), color='white')