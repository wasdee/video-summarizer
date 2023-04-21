# Video Summarizer 🌾🤖

Summarize and generate Q&A for videos on "The Future of Farming: How AgriTech and AI are Changing the Game" 🚜🌱.

## Table of Contents 📚
1. [Setup](#setup)
2. [Usage](#usage)
3. [Summaries](#summaries)

## Setup 🛠️

1. Create a new conda environment:

```bash
$ conda env create --file environment.yml
```

2. Install `ffmpeg` and `openai-whisper`:

```bash
$ sudo apt update && sudo apt install ffmpeg
$ pip install openai-whisper
```

## Usage 🚀

1. Download videos from Facebook 🎥:

```bash
$ youtube-dl https://www.facebook.com/ThaiProgrammerSociety/videos/195344343261477/
$ youtube-dl https://www.facebook.com/ThaiProgrammerSociety/videos/548468247395828/
```

2. Convert videos to MP3 🎧:

```bash
$ ffmpeg -i part1.mp4 -vn -acodec libmp3lame -ac 2 -ab 192k -ar 44100 part1.mp3
```

3. Transcribe audio using OpenAI Whisper 🗣️:

```bash
$ whisper part2.mp3 --model large-v2 --output_format all --task translate --output_dir translate/
```

## Summaries 📝

### WriteSonic Summary 🖊️

The use of technology in farming has become critical in recent years 📈. Farmers must be aware of the problems that can arise and have the appropriate tools to address them 🔧. Technology can help farmers collect data and analyze it to understand how their plants are doing 🌿. Drones are increasingly being used to collect spatial data, and the Vettel drone is a new innovation that can fly up and down and control the area more efficiently 🚁. Using drones allows farmers to get the data they need, even in cases where satellite photos are not available due to weather conditions ☁️. The Vettel drone is made of carbon fiber, which makes it lightweight and easy to control 🕹️. The drone works with Nomad software, which plans where to cover the area, how to plan the flight, where to take pictures, and collect the data for further analysis 📊. Once farmers have the data, they can use it to see whether the area is well-planned, and plan the area to make it easier for farmers to work 🌾. Multi-spectrum data can also be used to determine whether the soil is hard or soft, which is essential for some agricultural projects 🚜. Overall, technology is an essential tool that can help farmers address problems and optimize their farmland for maximum yield 🌽.

### Google Bard Summary 📚

The speaker begins by talking about the challenges that farmers face today 🌍. They say that farmers are under pressure to produce more food with less resources, and that they are also facing the challenge of climate change 🌦️.

The speaker then talks about how Vtell's technology can help farmers to address these challenges 🆘. They say that Vtell's drones can be used to collect data on plants, which can then be used to identify problems and potential solutions 🌻. They also say that Vtell's autonomous vehicles can be used to spray chemicals, deliver heavy goods, and measure the quality of water 💦.

The speaker concludes by talking about the potential of drone farming and autonomous vehicles to revolutionize the way that farming is done