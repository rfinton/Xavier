from django.db import models

class Campaign(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Config(models.Model):
  AccountID = models.CharField(max_length=200)
  AccountName = models.CharField(max_length=200)
  ScheduleID = models.CharField(max_length=200)
  EndPoint = models.CharField(max_length=200)
  Email = models.CharField(max_length=200, default="")
  FtpUrl = models.CharField(max_length=200, default="")
  FtpUsername = models.CharField(max_length=200, default="")
  FtpPassword = models.CharField(max_length=200, default="")

  def __str__(self):
    return self.AccountID

class Contact(models.Model):
  contact_id = models.CharField(max_length=200)
  efcid = models.CharField(max_length=200)
  purl = models.CharField(max_length=200)
  grad_year = models.CharField(max_length=200)
  firstname = models.CharField(max_length=200)
  lastname = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  gender = models.CharField(max_length=20)
  address_1 = models.CharField(max_length=200)
  address_2 = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zip = models.CharField(max_length=200)
  country = models.CharField(max_length=200)
  gpa = models.CharField(max_length=200)
  email_inq = models.CharField(max_length=200)
  ethnicity = models.CharField(max_length=200)
  high_school_name = models.CharField(max_length=200)
  high_school_ceeb = models.CharField(max_length=200)
  listsource = models.CharField(max_length=200)
  major = models.CharField(max_length=200)
  rank1 = models.CharField(max_length=200)
  rank2 = models.CharField(max_length=200)
  rank3 = models.CharField(max_length=200)
  segment = models.CharField(max_length=200)
  source_filename = models.CharField(max_length=200)
  source_id = models.CharField(max_length=200)
  submit_action = models.CharField(max_length=200)
  sw20k = models.CharField(max_length=200)
  dob = models.CharField(max_length=200)
  distance = models.CharField(max_length=200)
  mobile = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  qrcode_used = models.CharField(max_length=200)
  race = models.CharField(max_length=200)

  def __str__(self):
    return self.purl

class Event(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class InboundDetail(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Inbound(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class OutboundSchedule(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Outbound(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Program(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class ResponseType(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class ServiceType(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Data(models.Model):
  date =            models.DateTimeField()
  score =           models.IntegerField(default=0, null=True, blank=True)

  year =            models.CharField(max_length=200, default=None, null=True, blank=True)
  month =           models.CharField(max_length=200, default=None, null=True, blank=True)
  day =             models.CharField(max_length=200, default=None, null=True, blank=True)
  hour =            models.CharField(max_length=200, default=None, null=True, blank=True)
  weekday =         models.CharField(max_length=200, default=None, null=True, blank=True)
  event_info =      models.CharField(max_length=200, default=None, null=True, blank=True)
  duration =        models.CharField(max_length=200, default=None, null=True, blank=True)
  question =        models.CharField(max_length=200, default=None, null=True, blank=True)
  answer =          models.CharField(max_length=200, default=None, null=True, blank=True)
  link_name =       models.CharField(max_length=200, default=None, null=True, blank=True)
  browser =         models.CharField(max_length=200, default=None, null=True, blank=True)
  os =              models.CharField(max_length=200, default=None, null=True, blank=True)
  referring_url =   models.CharField(max_length=200, default=None, null=True, blank=True)
  ip_address =      models.CharField(max_length=200, default=None, null=True, blank=True)

  element_type =    models.ForeignKey(ServiceType, default=None, null=True, blank=True, on_delete=models.CASCADE)
  question_type =   models.ForeignKey(ResponseType, default=None, null=True, blank=True, on_delete=models.CASCADE)
  contact =         models.ForeignKey(Contact, default=None, null=True, blank=True, on_delete=models.CASCADE)
  event =           models.ForeignKey(Event, default=None, null=True, blank=True, on_delete=models.CASCADE)
  outbound =        models.ForeignKey(Outbound, default=None, null=True, blank=True, on_delete=models.CASCADE)
  schedule =        models.ForeignKey(OutboundSchedule, default=None, null=True, blank=True, on_delete=models.CASCADE)
  inbound =         models.ForeignKey(Inbound, default=None, null=True, blank=True, on_delete=models.CASCADE)
  page =            models.ForeignKey(InboundDetail, default=None, null=True, blank=True, on_delete=models.CASCADE)
  campaign =        models.ForeignKey(Campaign, default=None, null=True, blank=True, on_delete=models.CASCADE)
  program =         models.ForeignKey(Program, default=None, null=True, blank=True, on_delete=models.CASCADE)
  
  def __str__(self):
    return str(self.event)