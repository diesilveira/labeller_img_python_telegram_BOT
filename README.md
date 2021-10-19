# labeller_images_python_telegramBOT

This is a bot to help collect data for any machine learning project

It was developed using the python-telegram-bot library that you can access from the following link: https://github.com/python-telegram-bot/python-telegram-bot

To be able to use it you just have to download it, install telegram for python:
$ pip install python-telegram-bot --upgrade

Create a configuration file in the same folder as main.py with the name conf.py
copy and paste the following text:

    TOKEN: str = 'TOUR TOKEN'

    # Like D:/Descargas/cleanAndDirtyImages
    PATH_FOLDER: str = 'YOUR PATH'
    
    buttons = ["BUTTON1", "BUTTON2", "BUTTON3", "BUTTON4"]
    
    question = 'QUESTION TO THE PEOPLE ABOUT THE IMAGE?'

In TOKEN you must write the token of your bot, previously created following the steps of telegram
https://core.telegram.org/bots

  In resume:
  send /newbot to BotFather from your telegram
  then you must set the name, shortname and description(optional)
  
  botFather send you your TOKEN.
  
In PATH_FOLDER you must put the path of the folder that contains your set images
in buttons, the name of the buttons, or labels for the image you sent.
and finally in question the question that you will send to next to image.

Last, run the project and voila, the bot is running now.

It arose as a response to one of the great problems with image sets, we do not know which is which, or how to receive feedback from other people about the images we have in order to better label them.
