from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_community.document_loaders import UnstructuredURLLoader

load_dotenv()
search = GoogleSearchAPIWrapper()

def main(place , start_date , day_count):
    results = top5_results(place, day_count)
    urls = extractinfo(results)
    url_data = load(urls)
    response = generate(url_data, start_date, day_count)
    return response

def top5_results(place, days):
    query = f"{days} day {place} itinerary for tourists"
    print("\n\n===========================================\n"+query+"\n===========================================")
    results = search.results(query, 2)
    print(f"Top 2 results retrieved successfully. Here are the results: {results}")
    return results

def extractinfo(results):
    print("Extracting information from search results...")
    urls = []

    # Iterate through the data and extract information
    for item in results:
        urls.append(item["link"])
    print("Information extracted successfully.")
    return urls

def load(urls):
    print("Loading data from URLs...")
    print(f"urls: {urls}")
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()
    print("Data loaded successfully.")
    return data


def generate(data, date, days):
    print("Initializing Google Generative AI model...")
    llm_g = ChatGoogleGenerativeAI(model="gemini-pro")
    Travel_Itinerary_Guide_Prompt = """
    Task: Generate a personalized travel itinerary based on information retrieved from Google.

    Instructions:
    1. Provide details about your destination(s) based on Google search results.
    2. Include information such as popular attractions, recommended activities, and notable points of interest.
    3. Specify the dates and duration of your trip.
    4. Optionally, share any specific preferences, restrictions, or interests you have during the trip.
    5. The AI will create a comprehensive travel itinerary, considering the weather forecast for the specified dates and locations.
    6. The itinerary will include recommendations for activities, attractions, and any adjustments based on weather conditions.
    7. Review the generated itinerary and let the AI know if you'd like any modifications or additional details.

    Example Input:
    Destination(s) Information: {data}
    Dates: {date}
    Duration: {day_count}

    Note: The more details you provide, the more personalized and accurate the itinerary will be.
    """
    prompt = Travel_Itinerary_Guide_Prompt.format(data = data, date= date, day_count = days)
    print("Generating travel itinerary...")
    response = llm_g.invoke(prompt)
    response = response.content
    itinerary = response
    print("Travel itinerary generated successfully.")
    return itinerary
