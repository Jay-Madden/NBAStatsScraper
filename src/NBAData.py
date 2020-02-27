import requests
from nba_api.stats.endpoints import commonplayerinfo, shotchartdetail
from nba_api.stats.static import players
import json as json
import 
class NBAData:

    def getData(self, player: str, ):
        shotchart = shotchartdetail.ShotChartDetail(team_id=0,player_id=2544)
        panda = shotchart.shot_chart_detail.get_data_frame()
        #to_drop = ['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'GAME_DATE', 'HTM', 'VTM', 'EVENT_TYPE']
        panda = panda.to_csv()
        with open('data.csv', 'w') as f:
            f.write(str(panda))
