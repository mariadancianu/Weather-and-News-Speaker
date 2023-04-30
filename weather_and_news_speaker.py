import json 
import urllib.request
from gtts import gTTS
from playsound import playsound 

# make sure to get these APIs keys and set them here before running the script 
ACCUWEATHER_API_KEY = ''
NEWS_API_KEY = ''

city = 'Milan'
username = 'Maria'
country_id = 'IT'
administrative_area_localized_name = 'Lombardy'


def get_json_data(url):
    """Gets the json data through an API. 
    
    Args:
      url: string
          URL of the API. 
       
    Returns:
      data: json 
          Data returned by the API in the json format. 
    """ 
    
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    
    return data 


def accuweather_get_city_location_key(city=city, 
                                      country_id=country_id, 
                                      administrative_area_localized_name=administrative_area_localized_name):
    """The AccuWeather API forecast searches require a location key. 
    Here we get the location key for the desired city. 
    
    Args:
      city: string, optional, Default = 'Milan'
          Desired city location. 
      country_id: str, optional, Default= 'IT'
          AccuWeather ID of the country where of the city. Here we limit 
          the search to Italy only. To change this check out the AccuWeather
          API documentation. 
      administrative_area_localized_name: str, optional, Default = 'Lombardy'
          AccuWeather localized name of the administrative area of the 
          city. To change this check out the AccuWeather API documentation. 
      
    Returns:
      location_id: int 
          AccuWeather location key. 
    """

    url = f"http://dataservice.accuweather.com/locations/v1/cities/{country_id}/search?apikey={ACCUWEATHER_API_KEY}&q={city}"
    
    location_id = None
    
    data = get_json_data(url)

    for found_cities in data:
        localized_name = found_cities.get(
            'AdministrativeArea', {}).get('LocalizedName', None)
        
        if localized_name == administrative_area_localized_name:
            location_id = found_cities['Key']
            break
    
    return location_id


def accuweather_get_forecast_one_day(location_id):
    """Get the weather forecast for the next day. 
    
    Args:
      location_id: int
          AccuWeather location key. 
          
    Returns:
      weather_text_to_speech: string
          Weather forecast for the next day and the desired city. 
    """

    url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_id}?apikey={ACCUWEATHER_API_KEY}"
    data = get_json_data(url)
    
    weather_text = data.get('Headline', {}).get('Text', None)

    daily_forecasts_list = data.get('DailyForecasts', [])

    if len(daily_forecasts_list) == 0:
        daily_forecasts_dict = {}
    else:
        daily_forecasts_dict = daily_forecasts_list[0]

    temperature_min = daily_forecasts_dict.get('Temperature', {}).get('Minimum', {}).get('Value', None)
    temperature_max = daily_forecasts_dict.get('Temperature', {}).get('Maximum', {}).get('Value', None)

    # convert fahrenheit to celsius 
    if temperature_min is not None:
        temperature_min = (temperature_min - 32) * 5/9
        temperature_min = round(temperature_min)
        
    if temperature_max is not None:
        temperature_max = (temperature_max - 32) * 5/9
        temperature_max = round(temperature_max)
    
    weather_forecast_dict = {}
    weather_forecast_dict['weather_text'] = weather_text
    weather_forecast_dict['temperature_min'] = temperature_min
    weather_forecast_dict['temperature_max'] = temperature_max
    
    return weather_forecast_dict


def get_weather_forecast(city):
    """Gets the weather forecast text to speech. 
    
    Args:
      city: string, optional, Default = 'Milan'
          Desired city location. 
    
    Returns:
      weather_text_to_speech: string
          Weather forecast for the next day and the desired city. 
    """
    
    location_id = accuweather_get_city_location_key(city)
    
    weather_forecast_dict = accuweather_get_forecast_one_day(location_id)
    
    if not weather_forecast_dict:
        return ''
    
    weather_text = weather_forecast_dict['weather_text']
    temperature_min = weather_forecast_dict['temperature_min']
    temperature_max = weather_forecast_dict['temperature_max']

    weather_text_to_speech = f"Here's the weather forecast for tomorrow in {city}. !"
    
    if weather_text is not None:
        weather_text_to_speech = f"{weather_text_to_speech} {weather_text}"
       
    if temperature_min is not None:
        weather_text_to_speech = f"{weather_text_to_speech} with a minimum temperature of {temperature_min} degrees"
    
    if temperature_max is not None:
        weather_text_to_speech = f"{weather_text_to_speech} with a maximum temperature of {temperature_max} degrees"  
  
    return weather_text_to_speech

 
def get_news_headlines(num_articles_max=10):
    """Gets the latest news headlines. 
    
    Args:
      num_articles_max: int, optional, Default=10
          Maximum number of latest news headlines. 
          
    Returns:
      news_headlines_text: string
          Latest headlines news. 
    """
    
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'

    data = get_json_data(url)
    
    articles = data.get('articles', [])
    
    news_headlines_text = 'Here are the latest news headlines.'
  
    articles = articles[:num_articles_max]
    
    for article in articles:
        title = article.get('title', None)
        
        if title is not None:
            news_headlines_text = news_headlines_text + title + '. ! '

    return news_headlines_text

       
def save_and_play_mp3(text_to_speech):
    """Converts the text to speech, creates and plays an mp3 file. 
    
    Args:
      text_to_speech: string 
          Text to be converted to speech. 
          
    Returns:
      None but saves and plays an mp3 file. 
    """
         
    mp3_filename = "weather_and_news_speaker.mp3"
    
    language = "en"
   
    myobj = gTTS(text=text_to_speech, lang=language, slow=False)
    myobj.save(mp3_filename)
     
    playsound(mp3_filename)

   
def WeatherNewsSpeaker(city=city,
                       username=username):
    """Speaker that updates you on the weather forecast for the next 
    day for a given location and on the latest news headlines.
   
    Args:
      city: string, optional, Default = 'Milan'
          Name of the city for which to get the weather forecast. 
      username: string, optional, Default = 'Maria'
          Name of the user. 
          
    Returns:
      None but saves and plays an mp3 with the weather forecast 
      and the latest news headlines. 
    """
   
    weather_forecast_text = get_weather_forecast(city)
    
    news_headlines_text = get_news_headlines()
   
    greetings_text = f"Hi {username}! I hope you had a nice day!"
    
    text_to_speech = f'{greetings_text}. ! {weather_forecast_text} . ! {news_headlines_text}'

    print(text_to_speech)
    
    save_and_play_mp3(text_to_speech)

if __name__ == '__main__':
    WeatherNewsSpeaker()
        
