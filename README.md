# Weather-and-News-Speaker
A simple speaker system to get the latest news and the weather forecast.   
- it uses the [AccuWeather API](https://developer.accuweather.com/api-flow-diagram) to get the weather forecast for the next day for a fixed location (Milan, Europe);  
- it uses the [News API](https://newsapi.org/) to get the latest news headlines;
- it uses the [Google Text-to-Speech](https://pypi.org/project/gTTS/) python library to convert the text to speech and save it as an mp3 file;
- it uses the [playsound](https://pypi.org/project/playsound/) python library to play the mp3 file;
- it is scheduled to run on a daily basis at the same time (9 pm). 

An example of the text converted to speech:   
![](https://github.com/mariadancianu/Weather-and-News-Speaker/blob/main/example_text_to_speech.png)


## Technologies 

Python version: 3.11. 

Python libraries:
- urllib
- gtts
- json 
- playsound 

## Status
Project is: *in progress*. 

## Warnings
Please make sure to generate your API keys for the AccuWeather API and News API before running the script.  
You will have to update the corresponding variables at the top of the weather_and_news_speaker.py file (ACCUWEATHER_API_KEY and NEWS_API_KEY).


## Contact 
Created by mary_0094@hotmail.it, feel free to get in touch! :woman_technologist:
