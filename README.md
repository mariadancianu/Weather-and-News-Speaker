# Weather-and-News-Speaker
A simple speaker system to get the latest news and the weather forecast.   
- it uses the [AccuWeather API](https://developer.accuweather.com/api-flow-diagram) to get the weather forecast for the next day for a fixed location (Milan, Italy);  
- it uses the [News API](https://newsapi.org/) to get the latest news headlines;
- it uses the [Google Text-to-Speech](https://pypi.org/project/gTTS/) python library to convert the text to speech and save it as an mp3 file;
- it uses the [playsound](https://pypi.org/project/playsound/) python library to play the mp3 file;

An example of the final text converted to speech, including 1 day weather forecast and the news headlines:   

<p float="left">
  <img src="https://github.com/mariadancianu/Weather-and-News-Speaker/blob/main/example_text_to_speech.png" width="850" height="200"/>
</p> 

#### AccuWeather API 

The AccuWeather API is free for a maximum of 50 calls per developer per day. This is enough for this project: only 1 call per day is needed.
   
First you have to create a developer account: go to https://developer.accuweather.com/, click on *REGISTER* and fill in the registration details. 
   
After the registration you will have to generate an API key: 
- go to *MY APPS* and click on *Add a new APP* 
- fill in all the required details (make sure to select Python as the programming language) and click on *CREATE APP*

If you want to get familiar with the API you can follow these steps. Once you have the API key you can access the 1 day weather forecast through the *Forecast API*. This API requires a *locationKey* that can be accessed through the *Locations API*.

<p float="left">
  <img src="https://github.com/mariadancianu/Weather-and-News-Speaker/blob/main/AccuWeather_API.png" width="750" height="400"/>
</p> 

Click on *Locations API*, go to the *Text Search* section and click on *City Search (results narrowed by countryCode*). You can find your country code here: https://developer.accuweather.com/countries-by-region.   

<p float="left">
  <img src="https://github.com/mariadancianu/Weather-and-News-Speaker/blob/main/AccuWeather_Locations_API_1.png" width="750" height="300"/>
</p> 

Update the following fields:
- country_code in the Resource URL
- apikey in the Query Parameters
- q in the Query Parameters: this is the name of your city 
- click on *Send this request* 

<p float="left">
  <img src="https://github.com/mariadancianu/Weather-and-News-Speaker/blob/main/AccuWeather_Locations_API_2.png" width="750" height="420"/>
</p>

If the request was successful, you will receive a *HTTP/1.1 200 OK* response followed by the results of the query in a json format. The json includes the location key to be used in the *Forecast API*. Check the file [location_id_milan.json](https://github.com/mariadancianu/Weather-and-News-Speaker/blob/main/location_id_milan.json) to see an example of the response for this query for the city of Milan. 

Now that you have the *locationKey* go to *Forecast API* and click on *1 Day of Daily Forecasts*. 

Similarly to the *Locations API*, you will have to update the following fields:
- locationKey in the Resource URL
- apikey in the Query Parameters
- click on *Send this request* 

Check the file [weather_forecast_2023-03-04.json](https://github.com/mariadancianu/Weather-and-News-Speaker/blob/main/weather_forecast_2023-04-30.json) to see an example of the response for this query for the city of Milan. Note that the temperature is in degrees Fahrenheit. 


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
