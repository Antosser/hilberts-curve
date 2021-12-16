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
5. Create a minecraft datapack and drop the .mcfunction file in

### Automatically
1. Open minecraftDatapackAll.py
2. Create a minecraft datapack and drop the .mcfunction file in

## Use image.py as a library
1. Make a new python file
2. import image.py
```python
import image
```
3. Generate the image
```python
image.generate(level)
```
