# Hilber's Curve Generator
Generate images of hilbert's curve or make a minecraft datapack out of it

## Image generation
1. Open the image.py file
2. Enter level of the curve. The width is equal to 3 to the level of the level times 3 ((3**x*)3)
3. Wait for the curve to generate

## Generate a minecraft datapack
### Manually
1. Open minecraftDatapack.py
2. Enter the level of the curve
3. Enter the scale/multiplier of the "maze" in python
4. Wait for a .mcfunction file to generate
5. Create a minecraft datapack and drop the .mcfunction file inside the "functions" directory

### Automatically
1. Open minecraftDatapackAll.py
2. Create a minecraft datapack and drop the .mcfunction files inside the "functions" directory

## hilbertsCurve.py as a library
1. Create a new python file
2. import hilbertsCurve.py
```python
from hilbertsCurve import hilbertsCurve
```
3. Create the curve
```python
curve = hilbertsCurve(size)
# Returns an array of coordinates (2d array) of the curve from first point to last
```
