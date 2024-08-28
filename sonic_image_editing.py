import json, os
import filetype
from PIL import Image
import mutagen
from mutagen.mp3 import HeaderNotFoundError

class GlobalConfig:
    """
    This config file reads from global_config.json and initializes values to be used in a Python environment. 
    """

    def __init__(self):
        """
        Initialize GlobalConfig class with variables from global_config.json
        """

        if os.getcwd().endswith("libraries") or os.getcwd().endswith("tests"):
            config_path = os.path.abspath(
                os.path.abspath(
                    os.path.join(os.getcwd(), os.pardir, "global_config.json")
                )
            )
        else:
            config_path = os.path.abspath(
                os.path.join(os.getcwd(), "global_config.json")
            )

        with open(config_path, "r") as f:
            self.config = json.load(f)

        # Read inputs from global_config.json
        self.input_audio_file = self.config.get("input_audio_file")
        self.input_image_file = self.config.get("input_image_file")
        self.filter_intensity = self.config.get("filter_intensity")

        # Append file variables into full addresses
        self.input_audio_file_path = os.path.join(os.getcwd(), "input", "audio", self.input_audio_file)
        self.input_image_file_path = os.path.join(os.getcwd(), "input", "images", self.input_image_file)
    def validate_file(self, file_path, file_type):
        """
        GlobalConfig function to validate acceptable file types being used 

        Args:
        - file_path (str): Path to input file for validation
        - file_type (str): Type of file expected -- "image" or "audio"

        Returns:
        - boolean
        """
        if not os.path.exists(file_path):
            print("Path does not exist")
            return False
        
        kind = filetype.guess(file_path)
        if not kind:
            print("Unable to detect file type")
            return False
        
        if file_type.lower() == "image":
            try:
                with Image.open(file_path) as img:
                    img.verify()
                    return True
            except (IOError, SyntaxError):
                return False
        
        if file_type.lower() == "audio":
            try:
                audio_file = mutagen.File(file_path)
                if audio_file is not None:
                    print(f"Audio format: {audio_file.mime[0]}")
                    print(f"Duration: {audio_file.info.length} seconds")
                    return True
                else:
                    print("Unsupported audio file format.")
            except HeaderNotFoundError:
                print("Invalid MP3 file.")
                return False
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
   
        # Default action is to return false if no other tree has been valid
        return False

class SonicImageEditing:
    """
    Class of functions for interpretting audio files into a filter for image files.
    """
    def __init__(self, global_config):
        """
        Initializes SonicImageEditing class variables.
        """

        if global_config:
            self.gc = global_config
        else:
            self.gc = GlobalConfig()

    def package_audio_qualities(self):
        """
        Package together a dictionary of qualities describing the audio file
        """ 
        return {}
    
    def package_image_qualities(self):
        """
        Package together a dictionary of qualities describing the base image file
        """
        return {}
    
    def normalize_audio_qualities(self):
        """
        Normalize audio qualities dictionary into usable ranges based on existing image details
        """
        return {}

        

        


