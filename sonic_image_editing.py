import json, os

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

        self.input_image = self.config.get("input_image_file")

        self.input_audio = self.config.get("input_audio_file")

        self.filter_intensity = self.config.get("filter_intensity")

    def validate_file(self, file_path, file_type):
        """
        GlobalConfig function to validate acceptable file types being used 

        Args:
        - file_path (str): Path to input file for validation
        - file_type (str): Type of file expected -- "image" or "audio"

        Returns:
        - bool_valid (bool)
        """


        return bool_valid

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


