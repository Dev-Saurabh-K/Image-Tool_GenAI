from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import InjectedToolArg, tool
from typing import Annotated

@tool
def get_image_url(topic: str) -> str:
    """This function fetches the image url from the given api endpoint for target topic"""
    url:f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={topic}&gsrnamespace=6&prop=imageinfo&iiprop=url&format=json"