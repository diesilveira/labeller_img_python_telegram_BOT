# labeller_images_python_telegramBOT

This is a bot to help collect data for any machine learning project

It was developed using the python-telegram-bot library that you can access from the following link: https://github.com/python-telegram-bot/python-telegram-bot

To be able to use it you just have to download it, install telegram for python:
$ pip install python-telegram-bot --upgrade

Create a configuration file in the same folder as main.py with the name conf.py
copy and paste the following text:

    TOKEN: str = 'YOUR TOKEN'

    # Like D:/Descargas/cleanAndDirtyImages
    PATH_FOLDER: str = 'YOUR PATH'
    
    buttons = ["BUTTON1", "BUTTON2", "BUTTON3", "BUTTON4"]
    
    question = 'QUESTION TO THE PEOPLE ABOUT THE IMAGE?'
    
    LOCAL = 'false'

In TOKEN you must write the token of your bot, previously created following the steps of telegram
https://core.telegram.org/bots

  In resume:
  send /newbot to BotFather from your telegram
  then you must set the name, shortname and description(optional)
  
  botFather send you your TOKEN.
  
In PATH_FOLDER you must put the path of the folder that contains your set images

In buttons, the name of the buttons, or labels for the image you sent, you can put all the buttons you want
In question, the question that you will send to next to image.

And finally if you have to run with images from web, set LOCAL='false' like at the example, you must to have a file named "url_images.txt" in the same folder of the main.py that contains the name of the image, and the url separated by ";". this is very important!

Last, run the project and voila, the bot is running now.

It arose as a response to one of the great problems with image sets, we do not know which is which, or how to receive feedback from other people about the images we have in order to better label them.

In the log.txt file the names of the images will be saved with their respective labels and in the finished file the images that have already been labeled so as not to label them twice

The buttons will be shown in two columns, in case the number of buttons is odd, the first one will occupy the entire row

You can see my own bot https://t.me/CleanDirtyContainer_bot inspired by Rodrigo's ML project on the classification of garbage containers in the Montevideo city https://github.com/rola93/clean-dirty-preprocess-baseline.

## License
[MIT](https://choosealicense.com/licenses/mit/)
