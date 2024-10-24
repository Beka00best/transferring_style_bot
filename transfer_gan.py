import os
import torch
import train_gan.net as net
import train_gan.utils as utils


def create_net_v1():
    msg_net = net.Net()
    msg_net_checkpoint = os.path.join('train_gan', 'msgnet_main.pth')
    if os.path.exists(msg_net_checkpoint):
        msg_net.load_state_dict(torch.load(msg_net_checkpoint))
    msg_net.eval()
    return msg_net


def msg_net_v1_processing(msg_net, style, content, image):
    with torch.no_grad():
        if type(content) is str:
            content = utils.tensor_load_rgbimage(content, 256, keep_asp=True)
        msg_net.setTarget(utils.tensor_load_rgbimage(style, 256).unsqueeze(0))
        im = msg_net(content.detach().unsqueeze(0))[0]
        utils.tensor_save_rgbimage(im, image)
