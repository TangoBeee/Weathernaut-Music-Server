from flask import Flask, send_file
import random

app = Flask(__name__)

# Predefined lists of songs for different weather conditions
weather_songs = {
    "sunny": [
    "./music/Aqua-Euphoria-with-Lucentia-432-Hz(chosic.com).mp3",
    "./music/Dont-Forget-Me-Alternative-Version-from-2018(chosic.com).mp3",
    "./music/Dont-Forget-Me(chosic.com).mp3",
    "./music/Evening-Improvisation-with-Ethera(chosic.com).mp3",
    "./music/Fly-Away-When-The-Fog-Settled-Down(chosic.com).mp3",
    "./music/Journey-Of-Your-Spirit-with-Lucentia(chosic.com).mp3",
    "./music/Komiku_-_11_-_Friends_2068(chosic.com).mp3",
    "./music/Otjanbird-Pt.-I(chosic.com).mp3",
    "./music/Sea-Of-Thoughts-with-Lucentia(chosic.com).mp3",
    "./music/Serena-Longer-Version(chosic.com).mp3"
],
    "rainy": [
    "./music/Aqua-Euphoria-with-Lucentia-432-Hz(chosic.com).mp3",
    "./music/Dont-Forget-Me-Alternative-Version-from-2018(chosic.com).mp3",
    "./music/Dont-Forget-Me(chosic.com).mp3",
    "./music/Evening-Improvisation-with-Ethera(chosic.com).mp3",
    "./music/Fly-Away-When-The-Fog-Settled-Down(chosic.com).mp3",
    "./music/Journey-Of-Your-Spirit-with-Lucentia(chosic.com).mp3",
    "./music/Komiku_-_11_-_Friends_2068(chosic.com).mp3",
    "./music/Otjanbird-Pt.-I(chosic.com).mp3",
    "./music/Sea-Of-Thoughts-with-Lucentia(chosic.com).mp3",
    "./music/Serena-Longer-Version(chosic.com).mp3"
],

    "cloudy": [
    "./music/Aqua-Euphoria-with-Lucentia-432-Hz(chosic.com).mp3",
    "./music/Dont-Forget-Me-Alternative-Version-from-2018(chosic.com).mp3",
    "./music/Dont-Forget-Me(chosic.com).mp3",
    "./music/Evening-Improvisation-with-Ethera(chosic.com).mp3",
    "./music/Fly-Away-When-The-Fog-Settled-Down(chosic.com).mp3",
    "./music/Journey-Of-Your-Spirit-with-Lucentia(chosic.com).mp3",
    "./music/Komiku_-_11_-_Friends_2068(chosic.com).mp3",
    "./music/Otjanbird-Pt.-I(chosic.com).mp3",
    "./music/Sea-Of-Thoughts-with-Lucentia(chosic.com).mp3",
    "./music/Serena-Longer-Version(chosic.com).mp3"
],

    "snowy": [
    "./music/Aqua-Euphoria-with-Lucentia-432-Hz(chosic.com).mp3",
    "./music/Dont-Forget-Me-Alternative-Version-from-2018(chosic.com).mp3",
    "./music/Dont-Forget-Me(chosic.com).mp3",
    "./music/Evening-Improvisation-with-Ethera(chosic.com).mp3",
    "./music/Fly-Away-When-The-Fog-Settled-Down(chosic.com).mp3",
    "./music/Journey-Of-Your-Spirit-with-Lucentia(chosic.com).mp3",
    "./music/Komiku_-_11_-_Friends_2068(chosic.com).mp3",
    "./music/Otjanbird-Pt.-I(chosic.com).mp3",
    "./music/Sea-Of-Thoughts-with-Lucentia(chosic.com).mp3",
    "./music/Serena-Longer-Version(chosic.com).mp3"
],

    "atmospheric": [
    "./music/Aqua-Euphoria-with-Lucentia-432-Hz(chosic.com).mp3",
    "./music/Dont-Forget-Me-Alternative-Version-from-2018(chosic.com).mp3",
    "./music/Dont-Forget-Me(chosic.com).mp3",
    "./music/Evening-Improvisation-with-Ethera(chosic.com).mp3",
    "./music/Fly-Away-When-The-Fog-Settled-Down(chosic.com).mp3",
    "./music/Journey-Of-Your-Spirit-with-Lucentia(chosic.com).mp3",
    "./music/Komiku_-_11_-_Friends_2068(chosic.com).mp3",
    "./music/Otjanbird-Pt.-I(chosic.com).mp3",
    "./music/Sea-Of-Thoughts-with-Lucentia(chosic.com).mp3",
    "./music/Serena-Longer-Version(chosic.com).mp3"
]

}

@app.route('/weather/<condition>.mp3')
def serve_random_song(condition):
    # Check if the weather condition exists in your predefined lists
    if condition in weather_songs:
        # Randomly select a song for the given weather condition
        selected_song = random.choice(weather_songs[condition])
        # Serve the selected song as an audio file
        return send_file(selected_song, mimetype="audio/mpeg")
    else:
        return "Weather condition not found", 404


