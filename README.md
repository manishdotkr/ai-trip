
# AI Travel Itinerary Guide System 🤖 📑

This Python project is an AI proof-of-concept (POC) that assists users in planning their travel itineraries. The project utilizes Streamlit for displaying data in the `app.py` file, while the rest of the code resides in `utils.py`. The core functionality involves querying the Google Search API using the `GoogleSearchAPIWrapper` from `langchain`, extracting relevant information from the search results, unloading URLs with the `UnstructuredURLLoader`, and generating a travel itinerary using the `ChatGoogleGenerativeAI` model from `langchain_google_genai`. The generated itinerary is then displayed using Streamlit.

## Getting Started

### Prerequisites
- Bash
- Python 3.x
- Pipenv

### Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/officialmanishkr98/ai-trip.git
   cd ai-trip
   ```

### Running the Application

1. Ensure you are in the project directory.

2. Run the application using bash:
   ```sh
   bash startup.sh
   ```

3. Access the application in your web browser at `http://localhost:8501`.

## Project Structure

- `app.py`: Streamlit application for user interaction.
- `utils.py`: Contains core functionality for querying the Google Search API, extracting information, and generating travel itineraries.
- `startup.sh`: Shell script for automatically running the entire code.
- `Pipfile` and `Pipfile.lock`: Dependency management files.

## Usage

1. Enter the place you want to visit, start date, and number of days of your travel in the Streamlit application.
2. Click the "Get started" button to retrieve the best travel plan for your vacation.
3. The application will display the generated travel itinerary.

## Usefull Links
- GOOGLE CSE ID: [Link](https://programmablesearchengine.google.com/u/1/controlpanel/all)
- GEMINI API KEY: [Link](https://console.cloud.google.com/apis)

## Acknowledgements

- Streamlit: [https://streamlit.io/](https://streamlit.io/)
- langchain: [https://pypi.org/project/langchain/](https://pypi.org/project/langchain/)
- langchain_google_genai: [https://pypi.org/project/langchain-google-genai/](https://pypi.org/project/langchain-google-genai/)

```