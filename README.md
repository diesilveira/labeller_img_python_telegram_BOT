# labeller_images_python_telegramBOT

This is a bot to help collect data for any machine learning project. <br>
It was developed using the python-telegram-bot library that you can access from the following link: https://github.com/python-telegram-bot/python-telegram-bot

## Usage & steps
1. download the repo, and install python-telegram-bot:

```bash
git clone https://github.com/diesilveira/labeller_img_python_telegram_BOT.git
cd labeller_img_python_telegram_BOT
pip install python-telegram-bot --upgrade
```

2. Create a configuration file in the same folder as main.py with the name conf.py
copy and paste the following text:

```bash
TOKEN: str = 'YOUR TOKEN'

#Like D:/Descargas/cleanAndDirtyImages
PATH_FOLDER: str = 'YOUR PATH'
LOCAL = 'false'

BUTTONS = ["BUTTON1", "BUTTON2", "BUTTON3", "BUTTON4"]
QUESTION = 'QUESTION TO THE PEOPLE ABOUT THE IMAGE?'
CHOSE = 'Chose: '
```

In TOKEN you must copy and paste the token of your bot, previously created.<br>
You can see how to at: https://core.telegram.org/bots or following these steps:<br>
For create a bot with telegram and get your TOKEN:
  * send /newbot to BotFather from your telegram
  * then you must to set the name, shortname and description(optional)
  * botFather send you your TOKEN.
  
In PATH_FOLDER you must put the path of the folder that contains your set images (for run local with images in your pc)<br>
If you want to use images from the web you must set LOCAL = 'false', create a file named "url_images.txt" in the same folder of the main.py that contains the name of the image, and the url separated by ";". importan: the url link provided must be a direct link to the file!

In buttons, the name of the buttons, or labels for the image you sent. You can put all the buttons you want.<br>
In question, the question that you will send to next to image.

3. Last, RUN the project and voila, the bot is running now.

In the log.txt file the names of the images will be saved with their respective labels and in the finished file the images that have already been labeled so as not to label them twice

The buttons will be shown in two columns, in case the number of buttons is odd, the first one will occupy the entire row

## Motivation
It arose as a response to one of the great problems with image sets, we do not know which is which, or how to receive feedback from other people about the images we have in order to better label them.

## My Own bot
You can see my own bot https://t.me/CleanDirtyContainer_bot inspired by Rodrigo's ML project on the classification of garbage containers in the Montevideo city https://github.com/rola93/clean-dirty-preprocess-baseline.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Next features in order of importance:
* auto-delete cell images after tag
* correct label when you failed
* improve welcome and help message
* implement internal buffer so that the images go faster
* login users who tag
* optional "skip image" button
* log who tagged
* verify that all buttons are different
* support that only a closed group of users can tag
* admit N labels for the same image, by N different people (that is, instead of a single person saying if it is a clean or dirty container, let N people do it, with N configurable)

## License
[MIT](https://choosealicense.com/licenses/mit/)
