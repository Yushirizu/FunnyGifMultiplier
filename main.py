import imageio
import numpy as np

gif_path = '3dgifmaker05954.gif'
output_path = 'multiplied.gif'

def multiply_gif(gif, factor, scale_factor=1):
    new_gif = []
    for frame in gif:
        new_frame = np.tile(frame, (factor, factor, 1))
        new_frame = new_frame[::scale_factor, ::scale_factor, :]
        new_gif.append(new_frame)
    return new_gif


def create_multiplied_gif(gif_path, output_path, downscale_factor=4):
    gif = imageio.mimread(gif_path)
    factor = 1
    for i in range(20):
        new_gif = multiply_gif(gif, factor, downscale_factor)
        imageio.mimsave(f'{output_path}{factor}.gif', new_gif, fps=15)
        factor *= 2


create_multiplied_gif(gif_path, output_path, downscale_factor=8)
