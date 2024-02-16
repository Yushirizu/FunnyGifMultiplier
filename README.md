# GIF Multiplier

This Python script takes an input GIF, multiplies each frame by a specified factor, and creates a new GIF with the multiplied frames. Additionally, it allows for downscaling the resulting frames.

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Yushirizu/FunnyGifMultiplier.git
    ```

2. **Install the required dependencies:**

    ```bash
    pip install imageio numpy
    ```

3. **Run the script:**

    ```bash
    python main.py
    ```

## Parameters

- `gif_path`: Path to the input GIF file.
- `output_path`: Path to save the multiplied GIF files.
- `downscale_factor`: Factor by which the frames are downscaled.

## Example

```python
import imageio
import numpy as np

gif_path = '3dgifmaker05954.gif'
output_path = 'multiplied.gif'

create_multiplied_gif(gif_path, output_path, downscale_factor=8)

