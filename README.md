# Noise-Generator
**A tool to generate different kinds of noises! Such as: Discrete noise, spotted noise, static noise, perlin noise, ect...**


## Usage
- Discrete Noise
    ```python3 main.py -d width height name_of_file```
- Spotted Noise
    ```python3 main.py -s width height infrequence, density, inverse, name_of_file```
  - width: Width of noise texture
  - height: Weight of noise texture
  - infrequence: Frequency of not getting a "spot" in spotted noise
  - density: Amount of "spots" in spotted noise
  - inverse: Will inverse the colors in spotted noise
  - name_of_file: Name that the noise texture will get saved as
 
## Dependencies
  - Python3
  - numpy (python)
    - Installtion: ```pip3 install numpy```
  - matplotlib (python)
    - Installtion ```pip3 install matplotlib```

## TODO
  - [x] Discrete Noise⠀]
  - [x] Spotted Noise⠀⠀⠀]
  - [ ] Static Noise⠀⠀⠀⠀⠀]---- Colors?
  - [ ] Perlin Noise⠀⠀⠀⠀]
  - [ ] Fractal Noise⠀⠀]
  - [ ] GUI
