from sonic_image_editing import GlobalConfig
from sonic_image_editing import SonicImageEditing

def run_sie():
    gc = GlobalConfig()
    if gc.validate_file(file_path=gc.input_audio_file_path, file_type="audio"):
        print(f"Valid file: {gc.input_audio_file_path}")
    if gc.validate_file(file_path=gc.input_image_file_path, file_type="image"):
        print(f"Valid file: {gc.input_image_file_path}")

    sie = SonicImageEditing(global_config = gc)


if __name__ == "__main__":
    run_sie()