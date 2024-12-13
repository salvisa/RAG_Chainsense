# RAG_Chainsense
ChainSense Project

ChainSense is an advanced project integrating supply chain intelligence with real-time weather insights using OpenAI and Pinecone. This project combines data scraping, indexing, and retrieval-augmented generation (RAG) pipelines to provide actionable insights for supply chain disruptions, logistics, and environmental impacts.

Installation

Prerequisites

Python 3.8 or later

ChromeDriver or any other Selenium-compatible web driver installed

An OpenAI API key

A Pinecone API key

Required Python libraries (specified in requirements.txt)

Steps

Clone the repository:

git clone <repository-url>
cd chain_sense_project

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Set up environment variables in a .env file:

OPENAI_API_KEY=<your_openai_api_key>
PINECONE_API_KEY=<your_pinecone_api_key>
PINECONE_ENV=<your_pinecone_environment>

Ensure ChromeDriver is installed and added to your PATH for Selenium to work.

Project Structure

.
├── data                   # Contains raw and processed data files
├── src                    # Source code
│   ├── app.py             # Streamlit app for user interaction
│   ├── data_prep.py       # Preprocesses raw text data for embedding
│   ├── embed_index.py     # Embeds and indexes documents into Pinecone
│   ├── rag_pipeline.py    # RAG pipeline for answering queries
│   ├── test_openai_api.py # Verifies OpenAI API functionality
│   ├── weather_pipeline.py # Indexes and retrieves weather data
│   ├── web_scraper.py     # Scrapes Bloomberg articles
│   └── utils              # Utility functions
├── .env                   # Environment variables
├── requirements.txt       # List of required Python libraries
└── README.md              # Project documentation

Usage

Running the Streamlit App

Start the app:

streamlit run src/app.py

Open the provided localhost URL in your browser to interact with the app.

Preprocessing Data

Place raw text files in the data/text/ directory.

Run the preprocessing script:

python src/data_prep.py

Indexing Documents

Ensure processed files are in data/processed/.

Index the data:

python src/embed_index.py

Testing the OpenAI API

Run the test script:

python src/test_openai_api.py

Weather Data Pipeline

Fetch and index weather data:

python src/weather_pipeline.py

Preprocess and store weather data for specific locations.

Scraping Articles

Scrape articles from Bloomberg:

python src/web_scraper.py

Processed articles will be saved to data/scraped_articles.json.

Module Descriptions

1. app.py

A Streamlit app allowing users to:

Ask supply chain-related queries.

Fetch real-time weather insights.

Analyze combined supply chain and weather impacts.

2. data_prep.py

Prepares raw text data by cleaning and chunking it into manageable segments for embedding.

3. embed_index.py

Generates embeddings for text data using OpenAI models and indexes them in Pinecone.

4. rag_pipeline.py

Implements the RAG pipeline:

Retrieves relevant contexts from Pinecone.

Uses OpenAI's GPT models to generate context-aware answers.

5. test_openai_api.py

A utility script to test the connectivity and functionality of the OpenAI API.

6. weather_pipeline.py

Fetches, processes, and indexes weather data from various locations.

Provides weather data to the RAG pipeline for combined analysis.

7. web_scraper.py

Uses Selenium and BeautifulSoup to scrape Bloomberg for articles related to supply chain topics.

Extracts and stores article metadata and content for analysis.

Environment Variables

Set the following variables in your .env file:

OPENAI_API_KEY=<your_openai_api_key>
PINECONE_API_KEY=<your_pinecone_api_key>
PINECONE_ENV=<your_pinecone_environment>

Dependencies

Install the dependencies using:

pip install -r requirements.txt

Key Libraries:

openai

pinecone

requests

bs4 (BeautifulSoup)

selenium

streamlit

nltk

How It Works

Web Scraper: Fetches supply chain articles from Bloomberg.

Preprocessing: Cleans and chunks raw text data for embedding.

Embedding & Indexing: Uses OpenAI embeddings to index data in Pinecone.

RAG Pipeline: Retrieves indexed data and generates context-aware answers using OpenAI models.

Weather Integration: Incorporates real-time weather data into the analysis pipeline for enhanced insights.

Screenshots

Streamlit Interface



Indexed Data Sample



Known Issues

Bloomberg article scraping may fail if their HTML structure changes.

Pinecone upserts can fail if the API key or environment variables are misconfigured.

OpenAI API rate limits may affect response time.

Future Enhancements

Extend the app to support more data sources.

Add more advanced weather analytics and forecasting.

Enable real-time updates and notifications for supply chain disruptions.

Optimize indexing and retrieval for large-scale datasets.

Troubleshooting

OpenAI API Errors: Ensure your API key is valid and set in .env.

Pinecone Issues: Verify your Pinecone API key and environment are correctly configured.

Selenium WebDriver: Ensure ChromeDriver is installed and matches your browser version.

Dependencies: Install missing libraries using pip install -r requirements.txt.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements and bug fixes.