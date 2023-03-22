import csv

emails = []
firstlast = []
no_email = 0
outfile = open('xula.nonresp.csv', 'w')

with open('Xavier F19 Deposited FTF as of 2.1.19 with email.csv', 'r') as infile:
  reader = csv.reader(infile, delimiter=',')
  reader.next()

  for row in reader:
    fl = (row[1].lower() + row[2].lower()).replace(' ', '')
    firstlast.append(fl)
    emails.append(row[3].lower())

with open('xavier.male.nonresp.studio.export.csv', 'r') as infile:
  reader = csv.reader(infile, delimiter=',')
  writer = csv.writer(outfile, delimiter=',', lineterminator='\n')

  for row in reader:
    em = row[3].lower()

    if em:
      if em not in emails:
        writer.writerow(row)
    else:
      fl = (row[1].lower() + row[2].lower()).replace(' ', '')
      no_email += 1

      if fl not in firstlast:
        writer.writerow(row)
      else:
        print('Matched found by name: ' + fl)

print('# of contacts missing email address: ' + str(no_email))