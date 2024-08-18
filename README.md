# Social Insights Dashboard "WhispersAnalytics"

## Overview

The Social Insights Dashboard is a comprehensive web application designed to provide deep insights into social media data, trends, sentiment analysis, user profile monitoring, and customer inquiries handling through a chatbot. It is built using Django for the backend and a combination of JavaScript, CSS, HTML, and Bootstrap for the frontend, leveraging various Python packages and tools for real-time data analysis and visualization.

## Key Features

- **Sentiment Analysis**: Analyzes sentiments on Twitter (or X) in real-time based on user-specified keywords and model preferences. Includes Arabic sentiment analysis using a pre-trained BERT model.
- **Trend Tracking**: Visualizes trend spread and comparisons through interactive graphs.
- **Chatbot**: Integrated for handling customer inquiries using deep learning models and techniques (in early stages).
- **Social Media Monitoring**: Monitors and visualizes user profiles across Twitter, Facebook, and Instagram, providing insights into engagement rates and post performance.

## Technologies Used

### Backend

- **Django**: Framework for building the web application.
- **Python Packages**:
  - Data Scraping: Tweepy, Twint, Instagramy, Pytrends, Selenium.
  - Data Manipulation: Pandas, Numpy.
  - Sentiment Analysis: Transformers (Hugging Face BERT), TextBlob.
  - Visualization: Plotly.
- **Database**: SQLite for caching specific processes.

### Frontend

- **Languages**: JavaScript, CSS, HTML.
- **Frameworks/Libraries**: Bootstrap, Chart.js

## Project Structure

### Sentiment Analysis

- **Classes**: Handle real-time data scraping from Twitter using Twint and Tweepy, data manipulation with Pandas, and sentiment analysis using BERT and TextBlob models.
- **Features**: Generates a dashboard with sentiment analysis pie chart, word clouds, and examples of positive and negative sentiment tweets based on user queries.

### Trend Tracking

- **Classes**: Utilize Pytrends for data scraping and Plotly (Python version) for visualization.
- **Features**: Display choropleth map, bar chart, and scatter plot to visualize trend spread and comparisons. Caches data in SQLite for efficiency.

### Social Media Monitoring

- **Classes**: Scrape user's profile data and posts from Twitter, Facebook, and Instagram using Selenium, Twint, and Instagramy. Manipulate data with Pandas.
- **Features**: Provide insights into user profiles through bar charts and time series graphs, showcasing engagement rates and recent posts performance across platforms.

### Chatbot

- **Description**: Handles customer inquiries using deep learning models and techniques (in early stages).
- **Features**: Create chatbots and view demos of them for users.

## Future Scope

This project is envisioned to expand its capabilities to smartphone applications, enhancing accessibility and usability for a broader audience. Additionally, it aims to incorporate:

- **Advanced Authorization Levels**: Implement more granular authorization levels to enhance security and user access control within the application.
- **Fully Deployed and Functional Chatbot**: Develop and deploy a fully functional chatbot that can effectively handle customer inquiries, providing a seamless user experience and improving customer engagement.

## Conclusion

The Social Insights Dashboard is a powerful tool for businesses and individuals to track social trends, analyze sentiments, monitor their social media presence, and handle customer inquiries effectively. By integrating advanced data scraping, manipulation, and visualization techniques, it offers a comprehensive solution for gaining valuable insights from social media data.

**Important Note:** Some of the used packages or classes may not be functioning correctly at the moment.
