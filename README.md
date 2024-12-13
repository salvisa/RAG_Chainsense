# ChainSense Project

ChainSense is an advanced project integrating supply chain intelligence with real-time weather insights using OpenAI and Pinecone. This project combines data scraping, indexing, and retrieval-augmented generation (RAG) pipelines to provide actionable insights for supply chain disruptions, logistics, and environmental impacts.

---

## Installation

### Prerequisites
1. Python 3.8 or later
2. ChromeDriver or any other Selenium-compatible web driver installed
3. An OpenAI API key
4. A Pinecone API key
5. Required Python libraries (specified in `requirements.txt`)

### Steps
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd chain_sense_project
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up environment variables in a `.env` file:
    ```plaintext
    OPENAI_API_KEY=<your_openai_api_key>
    PINECONE_API_KEY=<your_pinecone_api_key>
    PINECONE_ENV=<your_pinecone_environment>
    ```
5. Ensure `ChromeDriver` is installed and added to your PATH for Selenium to work.

---

## Project Structure

```
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
```

---

## Usage

### Running the Streamlit App
1. Start the app:
    ```bash
    streamlit run src/app.py
    ```
2. Open the provided localhost URL in your browser to interact with the app.

### Preprocessing Data
1. Place raw text files in the `data/text/` directory.
2. Run the preprocessing script:
    ```bash
    python src/data_prep.py
    ```

### Indexing Documents
1. Ensure processed files are in `data/processed/`.
2. Index the data:
    ```bash
    python src/embed_index.py
    ```

### Testing the OpenAI API
Run the test script:
```bash
python src/test_openai_api.py
```

### Weather Data Pipeline
1. Fetch and index weather data:
    ```bash
    python src/weather_pipeline.py
    ```
2. Preprocess and store weather data for specific locations.

### Scraping Articles
1. Scrape articles from Bloomberg:
    ```bash
    python src/web_scraper.py
    ```
2. Processed articles will be saved to `data/scraped_articles.json`.

---

## Module Descriptions

### 1. `app.py`
- A Streamlit app allowing users to:
  - Ask supply chain-related queries.
  - Fetch real-time weather insights.
  - Analyze combined supply chain and weather impacts.

### 2. `data_prep.py`
- Prepares raw text data by cleaning and chunking it into manageable segments for embedding.

### 3. `embed_index.py`
- Generates embeddings for text data using OpenAI models and indexes them in Pinecone.

### 4. `rag_pipeline.py`
- Implements the RAG pipeline:
  - Retrieves relevant contexts from Pinecone.
  - Uses OpenAI's GPT models to generate context-aware answers.

### 5. `test_openai_api.py`
- A utility script to test the connectivity and functionality of the OpenAI API.

### 6. `weather_pipeline.py`
- Fetches, processes, and indexes weather data from various locations.
- Provides weather data to the RAG pipeline for combined analysis.

### 7. `web_scraper.py`
- Uses Selenium and BeautifulSoup to scrape Bloomberg for articles related to supply chain topics.
- Extracts and stores article metadata and content for analysis.

---

## Environment Variables
Set the following variables in your `.env` file:

```plaintext
OPENAI_API_KEY=<your_openai_api_key>
PINECONE_API_KEY=<your_pinecone_api_key>
PINECONE_ENV=<your_pinecone_environment>
```

---

## Dependencies

Install the dependencies using:
```bash
pip install -r requirements.txt
```

### Key Libraries:
- `openai`
- `pinecone`
- `requests`
- `bs4` (BeautifulSoup)
- `selenium`
- `streamlit`
- `nltk`

---

## How It Works
1. **Web Scraper**: Fetches supply chain articles from Bloomberg.
2. **Preprocessing**: Cleans and chunks raw text data for embedding.
3. **Embedding & Indexing**: Uses OpenAI embeddings to index data in Pinecone.
4. **RAG Pipeline**: Retrieves indexed data and generates context-aware answers using OpenAI models.
5. **Weather Integration**: Incorporates real-time weather data into the analysis pipeline for enhanced insights.

---

## Known Issues
- Bloomberg article scraping may fail if their HTML structure changes.
- Pinecone upserts can fail if the API key or environment variables are misconfigured.
- OpenAI API rate limits may affect response time.

---

## Future Enhancements
- Extend the app to support more data sources.
- Add more advanced weather analytics and forecasting.
- Enable real-time updates and notifications for supply chain disruptions.
- Optimize indexing and retrieval for large-scale datasets.

---

## Troubleshooting
1. **OpenAI API Errors**: Ensure your API key is valid and set in `.env`.
2. **Pinecone Issues**: Verify your Pinecone API key and environment are correctly configured.
3. **Selenium WebDriver**: Ensure ChromeDriver is installed and matches your browser version.
4. **Dependencies**: Install missing libraries using `pip install -r requirements.txt`.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for enhancements and bug fixes.

---
