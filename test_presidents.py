# ----------------------------------------------------------------------------
# Author: Amber Ebersohl
#  Date: 24OCT2019
#
# This program calls the DuckDuckGo API and tests that the correct presidential
# list is returned in RelatedTopics when "presidents of the united states" is
# the search criteria
#  ---------------------------------------------------------------------------
import pytest
import requests

#Create list of presidential last names to check against
pres_list = ["Washington","Adams","Jefferson","Madison","Monroe","Jackson","Van Buren","Harrison",
             "Tyler","Polk","Taylor","Fillmore","Pierce","Buchanan","Lincoln","Johnson","Grant",
             "Hayes","Garfield","Arthur","Cleveland","McKinley","Roosevelt","Taft","Wilson",
             "Harding","Coolidge","Hoover","Truman","Eisenhower","Kennedy","Nixon","Ford","Carter",
             "Reagan","Bush","Clinton","Obama","Trump"]

#Get the API Data
url_ddg = "https://api.duckduckgo.com"
resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
rsp_data = resp.json()
rt = rsp_data["RelatedTopics"]

#Loop to put only text from related topics in a list 
pres_resps = []
for item in rt:
    pres_resps.append(item['Text'])
print(pres_resps)

#Tests
@pytest.mark.parametrize("president_list_item", [(pres_list[0]),
                                                (pres_list[1]),
                                                (pres_list[2]),
                                                (pres_list[3]),
                                                (pres_list[4]),
                                                (pres_list[5]),
                                                (pres_list[6]),
                                                (pres_list[7]),
                                                (pres_list[8]),
                                                (pres_list[9]),
                                                (pres_list[10]),
                                                (pres_list[11]),
                                                (pres_list[12]),
                                                (pres_list[13]),
                                                (pres_list[14]),
                                                (pres_list[15]),
                                                (pres_list[16]),
                                                (pres_list[17]),
                                                (pres_list[18]),
                                                (pres_list[19]),
                                                (pres_list[20]),
                                                (pres_list[21]),
                                                (pres_list[22]),
                                                (pres_list[23]),
                                                (pres_list[24]),
                                                (pres_list[25]),
                                                (pres_list[26]),
                                                (pres_list[27]),
                                                (pres_list[28]),
                                                (pres_list[29]),
                                                (pres_list[30]),
                                                (pres_list[31]),
                                                (pres_list[32]),
                                                (pres_list[33]),
                                                (pres_list[34]),
                                                (pres_list[35]),
                                                (pres_list[36]),
                                                (pres_list[37]),
                                                (pres_list[38])])
def test_presidents(president_list_item):
    assert president_list_item in str(pres_resps)
