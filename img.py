from PIL import Image
import 
from io import BytesIO

response = requests.get("https://photos.google.com/photo/AF1QipMlNgshYMHQ7o6lupbubdPp-tCkqtp9gptVQz9n")
img = Image.open(BytesIO(response.content))