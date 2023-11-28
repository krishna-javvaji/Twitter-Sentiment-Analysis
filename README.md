# Twitter Sentiment Analysis

## Description
This project performs sentiment analysis on tweets obtained via the Twitter API. It uses Python, Tweepy, and TextBlob to analyze and categorize tweets based on their sentiment as positive, negative, or neutral.


## Installation

To set up this project locally, follow these steps:

```bash
git clone https://github.com/krishna-javvaji/twitter-sentiment-analysis
cd twitter-sentiment-analysis
pip install -r requirements.txt
```

## Usage
Usage
To run the sentiment analysis:

```bash
python sentiment_analysis.py
```

## Features
Search and analyze tweets with specific keywords.
Sentiment analysis using TextBlob.
Easy to use and extend for different keywords or analysis criteria.

Example of fetching and analyzing tweets:

```
python
# Fetch tweets
public_tweets = api.search_tweets(q="keyword")

# Perform sentiment analysis
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

```
## Built With
Python
Tweepy - For accessing the Twitter API.
TextBlob - For performing sentiment analysis.


## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Authors and Acknowledgment
@krishna-javvaji - Initial work
Special thanks to online resources and communities that helped in the development of this project.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Project Status
The project is currently in a beta stage and open for improvements and contributions.

## Contact
My Mail - kjavvaji@uncc.edu, hemanth.y.vjws6@gmail.com
Project Link: https://github.com/yourusername/twitter-sentiment-analysis
