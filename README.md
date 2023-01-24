# Style Transfer Service
![Image alt](https://github.com/Beka00best/transferring_style_bot/static/neuralstyle.png)

This project is to transfer the style of one image to another image.

## Discription

This is a Telegram bot code that implements a slow and fast transfer of your style from a picture to your photo.

The slow algorithm was taken as a basis from this <a href="https://arxiv.org/abs/1508.06576">article</a>. And the implementation was taken from the official <a href="https://pytorch.org/tutorials/advanced/neural_style_tutorial.html">pytorch tutorial</a>. The full description can be viewed by clicking on the links above.

A fast algorithm using the Msg-Net neural network described in <a href="https://arxiv.org/pdf/1703.06953.pdf ">this article</a>. The training code and all other experiments were taken <a href="https://github.com/zhanghang1989/PyTorch-Multi-Style-Transfer ">from here</a>. I trained msg-net on a very large number of content images from the COCO validation dataset, about 6GB of images and 21 stylistic ones. But in the end, the network has learned to copy not only these styles, but also any (or almost any) other! For more information, see <a href="https://github.com/Beka00best/transferring_style_bot/blob/main/train_gan/train.ipynb">train.ipynb</a>

## Stages:
1. [Make a telegram bot](#Make-a-telegram-bot) :white_check_mark: 
2. [Build a ready-made GAN](#Build-a-ready-made-GAN) :white_check_mark: 
3. [Train and embed your own GAN](#Train-and-embed-your-own-GAN) :white_check_mark: 
4. [Docker](#Docker) :white_check_mark: 
6. [Tests](#Tests) :white_check_mark: 

## Download
Install the dependencies
```sh
git clone https://github.com/Beka00best/transferring_style_bot.git
cd transferring_style_bot
```
Then you have to add config.py with bot token. Token create with BotFather. In config.py add:
```sh
TOKEN = ""
```
### Docker
```sh
docker build -t prog .
```
Viewing images
```sh
docker images
```
### Run
```sh
docker run prog
```
### Other way
If you encounter problems with Docker, you can download it in a different way. You need to have a Linux system. 
1. You need python3
2. You need pip
In the terminal, enter the following commands:
```sh
pip install -r requirements.txt
python3 bot.py
```

### How use bot
After starting the bot.py go to telegram:
```sh
/start
```

You will be taken to this page:
![Image alt](https://github.com/Beka00best/transferring_style_bot/static/1.jpeg)
Then follow the instructions. Press "See an example":
![Image alt](https://github.com/Beka00best/transferring_style_bot/static/2.jpeg)
Then press another buttons, and follow the instructions:
![Image alt](https://github.com/Beka00best/transferring_style_bot/static/3.jpeg)
![Image alt](https://github.com/Beka00best/transferring_style_bot/static/4.jpeg)


### Clean
Delete all images
```sh
docker rmi -f $(docker images -a -q)
```
Stop all containers
```sh
docker stop $(docker ps -a -q)
```
Delete all containers
```sh
docker rm $(docker ps -a -f status=exited -q)
```