import csv
import pytz
from datetime import datetime
from django.utils import timezone

from report.models import Campaign, Config, Contact
from report.models import Event, Inbound, InboundDetail
from report.models import Outbound, OutboundSchedule, Program
from report.models import ResponseType, ServiceType, Data
'''
with open('config.csv', 'r') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = Config(
      AccountID=keypair[0],
      AccountName=keypair[1],
      ScheduleID=keypair[2],
      EndPoint=keypair[3],
      Email=keypair[4],
      FtpUrl=keypair[5],
      FtpUsername=keypair[6],
      FtpPassword=keypair[7]
    )
    tmp.save()

with open('Campaign-dictionary.csv', 'r') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = Campaign(id=keypair[0], name=keypair[1])
    tmp.save()

with open('Event-dictionary.csv') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = Event(id=keypair[0], name=keypair[1])
    tmp.save()

with open('Outbound-dictionary.csv', 'r') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = Outbound(id=keypair[0], name=keypair[1])
    tmp.save()

with open('Outbound Schedule-dictionary.csv', 'r') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = OutboundSchedule(id=keypair[0], name=keypair[1])
    tmp.save()

with open('Inbound-dictionary.csv', 'r') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = Inbound(id=keypair[0], name=keypair[1])
    tmp.save()

with open('Inbound Detail-dictionary.csv', 'r') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = InboundDetail(id=keypair[0], name=keypair[1])
    tmp.save()

with open('Program-dictionary.csv') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = Program(id=keypair[0], name=keypair[1])
    tmp.save()

with open('Response Type-dictionary.csv') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = ResponseType(id=keypair[0], name=keypair[1])
    tmp.save()

with open('Service Type-dictionary.csv') as fs:
  header = fs.readline()

  for line in fs:
    keypair = line.split(',')
    tmp = ServiceType(id=keypair[0], name=keypair[1])
    tmp.save()

with open('contacts.csv', 'r') as fs:
  header = fs.readline()
  reader = csv.reader(fs)
  
  for line in reader:
    tmp = Contact(
      contact_id=line[0],
      efcid=line[1],
      purl=line[2],
      grad_year=line[3],
      firstname=line[4],
      lastname=line[5],
      email=line[6],
      gender=line[7],
      address_1=line[8],
      address_2=line[9],
      city=line[10],
      state=line[11],
      zip=line[12],
      country=line[13],
      gpa=line[14],
      email_inq=line[15],
      ethnicity=line[16],
      high_school_name=line[17],
      high_school_ceeb=line[18],
      listsource=line[19],
      major=line[20],
      rank1=line[21],
      rank2=line[22],
      rank3=line[23],
      segment=line[24],
      source_filename=line[25],
      source_id=line[26],
      submit_action=line[27],
      sw20k=line[28],
      dob=line[29],
      distance=line[30],
      mobile=line[31],
      phone=line[32],
      qrcode_used=line[33],
      race=line[34]
    )
    tmp.save()
'''
with open('data.csv', 'r') as fs:
  header = fs.readline()

  for counter, line in enumerate(fs):
    data = line.split(',')

    tmp = Data(
      date=pytz.utc.localize(datetime.strptime(data[1], '%m/%d/%Y %I:%M:%S %p')),
      score=int(data[10]),

      year=data[2],
      month=data[3],
      day=data[4],
      hour=data[5],
      weekday=data[6],
      event_info=data[9],
      duration=data[15],
      question=data[16],
      answer=data[17],
      link_name=data[20],
      browser=data[23],
      os=data[24],
      referring_url=data[22],
      ip_address=data[25],

      program=Program.objects.get(id=data[21]),
      campaign=Campaign.objects.get(id=data[19]),
      element_type=ServiceType.objects.get(id=data[7]),
      contact=Contact.objects.get(id=data[0]),
      event=Event.objects.get(id=data[8])
    )

    if data[18] == '':
      question_type=None
    else:
      question_type=ResponseType.objects.get(id=data[18])

    if data[13] == '':
      inbound=None
    else:
      inbound=Inbound.objects.get(id=data[13])

    if data[14] == '':
      page=None
    else:
      page=InboundDetail.objects.get(id=data[14])

    if data[11] == '':
      outbound=None
    else:
      outbound=Outbound.objects.get(id=data[11])

    if data[12] == '':
      schedule=None
    else:
      schedule=OutboundSchedule.objects.get(id=data[12])

    tmp.save()
    #tmp.contact.add(Contact.objects.get(id=data[0]))
