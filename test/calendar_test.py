
import sys
from pathlib import Path
sys.path.insert(1, "..")
from src.mycalendar.calendarPage import relative_to_assets, ASSETS_PATH

def test_path():
    new_path = relative_to_assets("button_1.png")
    assert new_path == ASSETS_PATH/Path("button_1.png")