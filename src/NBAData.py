import requests
from nba_api.stats.endpoints import commonplayerinfo, shotchartdetail, playerdashptshots
from nba_api.stats.static import players
import json as json
from Enums import Output
class NBAData:

    def __init__(self):
        self.FileMappings = {
            Output.json: self.__getDataJson,
            Output.csv: self.__getDataCsv
        }

    def getData(self, player: str, fileType: Output ):

        playerData = players.find_players_by_full_name(player)
        shotCharts = {}

        for player in playerData:
            shotCharts[player['full_name']] = playerdashptshots.PlayerDashPtShots(team_id=0,player_id=player['id'])
        
        return self.FileMappings[fileType](shotCharts)

    def __getDataJson(self, shotCharts) -> str:
        return {key : value.overall.get_json() for key, value in shotCharts.items()} 

    def __getDataCsv(self, shotCharts) -> str:
        return {key : value.overall.get_data_frame().to_csv() for key, value in shotCharts.items()} 

