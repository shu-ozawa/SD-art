import os
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import trans

MODEL_PATH = r'./model/v1-5-pruned-emaonly.safetensors'
SAVE_PATH = './SD_OUTPUT/'

def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + '(' + str(counter) + ')' + extension
        counter += 1

    return path

original_prompt = 'Dogs in Space'

prompt = trans.pass_unchanged(original_prompt)
negative_prompt = 'nsfw, ng_deepnegative_v1_75t,badhandv4, (worst quality:2), (low quality:2), (normal quality:2), lowres,watermark, monochrome'

num_inference_steps = 50
height = 512
width = 512
device_type = 'cpu'

def render_prompt():
    shorted_prompt = (prompt[:25] + '...') if len(prompt) > 25 else prompt
    shorted_prompt = shorted_prompt.replace(' ', '_')

    generation_path = SAVE_PATH

    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)

    # Calling Stable Diffusion Pipeline
    pipe = StableDiffusionPipeline.from_pretrained(MODEL_PATH)

    return pipe

pipe = render_prompt()

with torch.no_grad():
    if device_type == 'cuda':
        with autocast():
            image = pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                height=height,
                width=width
            )
    else:
        image = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            height=height,
            width=width
        ).images[0]

image_path = uniquify(os.path.join(SAVE_PATH, (prompt[:25] + '...') if len(prompt) > 25 else prompt) + '.png')
print(image_path)

image.save(image_path)

print("\nRENDER FINISHED\n")
