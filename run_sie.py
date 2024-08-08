from sonic_image_editing import GlobalConfig
from sonic_image_editing import SonicImageEditing

def run_sie():
    gc = GlobalConfig()
    sie = SonicImageEditing(global_config = gc)


if __name__ == "__main__":
    run_sie()