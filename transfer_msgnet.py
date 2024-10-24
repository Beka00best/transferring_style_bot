import os

import torch
from torch.autograd import Variable

from train_gan import utils
from train_gan.msgnet import Net


def create_net_v2():
    style_model = Net(ngf=128)
    msg_net_checkpoint = os.path.join('train_gan', '21styles.model')
    model_dict = torch.load(msg_net_checkpoint)
    model_dict_clone = model_dict.copy()
    for key, value in model_dict_clone.items():
        if key.endswith(('running_mean', 'running_var')):
            del model_dict[key]
    style_model.load_state_dict(model_dict, False)
    return style_model


def msg_net_v2_processing(style_model, style, content, image):
    content_image = utils.tensor_load_rgbimage(content, size=512, keep_asp=True).unsqueeze(0)
    style = utils.tensor_load_rgbimage(style, size=512).unsqueeze(0)
    style = utils.preprocess_batch(style)

    style_v = Variable(style)
    content_image = Variable(utils.preprocess_batch(content_image))
    style_model.setTarget(style_v)
    output = style_model(content_image)
    utils.tensor_save_bgrimage(output.data[0], image, False)
