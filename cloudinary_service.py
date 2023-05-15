# Import
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary.api

from dotenv import load_dotenv
load_dotenv()

# Config
cloudinary.config(
  cloud_name = "dvqgbcaet",
  api_key = "296397624558122",
  api_secret = "sAWwsn5b0l_DvWwvfjHoN6aTCUw",
  secure = True
)

# Upload
upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg", public_id="olympic_flag")

# Transform
url, options = cloudinary_url("olympic_flag", width=100, height=150, crop="fill")