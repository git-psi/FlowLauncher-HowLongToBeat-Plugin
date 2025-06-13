# How Long To Beat - Flow Launcher Plugin

Search a game's playtime on [How Long To Beat](https://howlongtobeat.com) directly from [Flow Launcher](https://www.flowlauncher.com/).

## Features

- Quickly search for any game's estimated completion time.
- Displays Main Story, Main + Extra, and Completionist hours.
- Opens the game's How Long To Beat page in your browser.

## Installation

1. Download or clone this repository.
2. Place the plugin folder in your Flow Launcher `Plugins` directory.

## Usage

- Activate Flow Launcher.
- Type `hltb` followed by the game name (e.g., `hltb Outer Wilds`).
- Select the result to open the game's page on How Long To Beat.

## Dependencies

All required dependencies are included in the `.zip` file of the release, so you do not need to install anything for normal use.

If you want to modify the code or update dependencies, you need to add them to the `/lib` folder. You can do this with the following command (from the project folder):
```sh
python -m pip install --target=lib -r requirements.txt --no-user
```

## Plugin Structure

- `main.py`: Main plugin logic.
- `plugin.json`: Plugin manifest for Flow Launcher.
- `icon.png`: Plugin icon (the How Long To Beat icon).
- `lib/`: Contains dependencies and libraries.

## Configuration

No additional configuration is required.

## License

MIT License
