import imageio
import numpy as np

gif_path = 'original.gif'
output_path = 'multiplied.gif'

def multiply_gif(gif, factor):
    new_gif = []
    for frame in gif:
        new_frame = np.tile(frame, (factor, factor, 1))
        new_gif.append(new_frame)
    return new_gif

def create_multiplied_gif(gif_path, output_path):
    gif = imageio.mimread(gif_path)
    factor = 1
    for i in range(20):
        new_gif = multiply_gif(gif, factor)
        imageio.mimsave(f'{output_path}{factor}.gif', new_gif, fps=15)
        factor *= 2

create_multiplied_gif(gif_path, output_path)

