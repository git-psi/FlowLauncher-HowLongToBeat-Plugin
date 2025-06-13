import sys
import os

# Import depuis le dossier local 'Lib'
lib_path = os.path.join(os.path.dirname(__file__), "Lib")
sys.path.insert(0, lib_path)

from flowlauncher import FlowLauncher
from howlongtobeatpy import HowLongToBeat
import webbrowser

class HLTBPlugin(FlowLauncher):
    def query(self, query):
        if not query:
            return [{
                "Title": "Enter a game name",
                "IcoPath": "icon.png",
            }]

        search_query = query.strip()
        results = HowLongToBeat().search(search_query)

        if not results:
            return [{
                "Title": f"No results for: {search_query}",
                "IcoPath": "icon.png",
            }]

        best_match = max(results, key=lambda x: x.similarity)
        url = f"https://howlongtobeat.com/game?id={best_match.game_id}"

        return [{
            "Title": best_match.game_name,
            "SubTitle": f"Main: {best_match.main_story}h | +Extra: {best_match.main_extra}h | 100%: {best_match.completionist}h",
            "IcoPath": "icon.png",
            "JsonRPCAction": {
                "method": "open_url",
                "parameters": [url],
                "dontHideAfterAction": False
            }
        }]
    
    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    HLTBPlugin()