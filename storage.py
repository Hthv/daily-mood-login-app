import json

# import path locations (directory)
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_FILE = DATA_DIR / "checkin.json"
PHOTO_DIR = DATA_DIR / "photos"

# import all past data from the checkins
def load_all():
    """"Return a list of all check-ins"""
    if not DATA_FILE.exists():
        return []
    # if no check-ins exist, return empty list.
    with open(DATA_FILE, "r", encoding = "utf-8") as f:
        return json.load(f)
    # open the check-in, in read mode.
    # encode it to utf-8 so it reads all the text including emoji
    # f is just a variable

# load data into folder
def save_all(checkins):
    """Write check-in records to the file"""
    DATA_DIR.mkdir(parents = True, exist_ok = True)

    with open(DATA_FILE, "w", encoding = "utf-8") as f:
        json.dump(checkins, f, indent = 2)

# load data by date
def get_by_date(date_str):
    """Return the check-in log by date"""
    for checkin in load_all():
        if checkin["date"] == date_str:
            return checkin
    return None

# save check-in by date. replace if needed to
def save_checkin(entry):
    """Save a check-in. If date already exist, replace it"""
    new_list = []
    for checkin in load_all():
        if checkin["date"] != entry["date"]:
            new_list.append(checkin)
    new_list.append(entry)
    save_all(new_list)

if __name__ == "__main__":
    save_checkin({
        "date": "2026-11-02",
        "mood": "happy",
        "prompts": [],
        "note": "test"
    })

    print(get_by_date("2026-11-02"))
    print(get_by_date("1996-11-02"))
