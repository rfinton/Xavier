import os

def merge_dicts():
  campaign = []
  event = []
  inbound_detail = []
  inbound = []
  outbound_schedule = []
  outbound = []
  program = []
  response_type = []
  service_type = []
  campaign_dict = open("Campaign-dictionary.csv", "w")
  event_dict = open("Event-dictionary.csv", "w")
  inbound_detail_dict = open("Inbound Detail-dictionary.csv", "w")
  inbound_dict = open("Inbound-dictionary.csv", "w")
  outbound_schedule_dict = open("Outbound Schedule-dictionary.csv", "w")
  outbound_dict = open("Outbound-dictionary.csv", "w")
  program_dict = open("Program-dictionary.csv", "w")
  response_type_dict = open("Response Type-dictionary.csv", "w")
  service_type_dict = open("Service Type-dictionary.csv", "w")

  for root, folders, files in os.walk('.'):
    for folder in folders:
      for _root, _folders, _files in os.walk(folder):
        for f in _files:
          with open(os.path.join(folder, f)) as csv_file:
            if "dictionary" in f:
              for line in csv_file:
                keypair = line.split(',')
                
                if f == "Event-dictionary.csv":
                  if keypair not in event:
                    event.append(keypair)

                if f == "Inbound Detail-dictionary.csv":
                  if keypair not in inbound_detail:
                    inbound_detail.append(keypair)

                if f == "Inbound-dictionary.csv":
                  if keypair not in inbound:
                    inbound.append(keypair)

                if f == "Outbound Schedule-dictionary.csv":
                  if keypair not in outbound_schedule:
                    outbound_schedule.append(keypair)

                if f == "Outbound-dictionary.csv":
                  if keypair not in outbound:
                    outbound.append(keypair)

                if f == "Program-dictionary.csv":
                  if keypair not in program:
                    program.append(keypair)

                if f == "Response Type-dictionary.csv":
                  if keypair not in response_type:
                    response_type.append(keypair)

                if f == "Service Type-dictionary.csv":
                  if keypair not in service_type:
                    service_type.append(keypair)

                if f == "Campaign-dictionary.csv":
                  if keypair not in campaign:
                    campaign.append(keypair)

  for item in campaign:
    campaign_dict.write(item[0] + ',' + item[1])

  for item in event:
    event_dict.write(item[0] + ',' + item[1])

  for item in inbound_detail:
    inbound_detail_dict.write(item[0] + ',' + item[1])

  for item in inbound:
    inbound_dict.write(item[0] + ',' + item[1])

  for item in outbound_schedule:
    outbound_schedule_dict.write(item[0] + ',' + item[1])

  for item in outbound:
    outbound_dict.write(item[0] + ',' + item[1])

  for item in program:
    program_dict.write(item[0] + ',' + item[1])

  for item in response_type:
    response_type_dict.write(item[0] + ',' + item[1])

  for item in service_type:
    service_type_dict.write(item[0] + ',' + item[1])

  campaign_dict.close()
  event_dict.close()
  inbound_detail_dict.close()
  inbound_dict.close()
  outbound_schedule_dict.close()
  outbound_dict.close()
  program_dict.close()
  response_type_dict.close()
  service_type_dict.close()