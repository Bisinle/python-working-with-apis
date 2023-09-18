
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    # return json.dumps(json.loads(response.content),indent=4)
    return response.content
  def program_school(self):
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
      programs_list.append(program['agency'])
    return programs_list[3]




all_programs = GetPrograms().get_programs()
programs = GetPrograms().program_school()
for program in set(programs):
  print(program)
