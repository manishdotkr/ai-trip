from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_community.document_loaders import UnstructuredURLLoader

load_dotenv()

search = GoogleSearchAPIWrapper()


def top5_results(place, days):
    query = place + " travel itinerary for " + str(days) + " days"
    print("\n\n===========================================\n"+query+"\n===========================================")
    return search.results(query, 2)


tool = Tool(
    name="Google Search Snippets",
    description="Search Google for top results for best travel guide.",
    func=top5_results,
)


def extractinfo(result):
    titles = []
    links = []
    snippets = []

    # Iterate through the data and extract information
    for item in result:
        titles.append(item["title"])
        links.append(item["link"])
        snippets.append(item["snippet"])
    return titles, links, snippets

def load(urls):
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()
    return data


def generate(data, date, days):
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
    response = llm_g.invoke(prompt)
    response = response.content
    itinery = response
    return itinery
