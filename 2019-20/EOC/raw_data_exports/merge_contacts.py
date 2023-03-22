import os

def merge_contacts():
  contacts = set()
  header = ""

  for root, folders, files in os.walk('.'):
    for folder in folders:
      for _root, _folders, _files in os.walk(folder):
        for _file in _files:
          if _file == 'contacts.csv':
            with open(os.path.join(folder, _file)) as csv_file:
              header = csv_file.readline()
              for line in csv_file:
                contacts.add(line)
                  
  contacts_csv = open('contacts.csv', 'w')
  contacts_csv.write(header)

  for item in contacts:
    contacts_csv.write(item)

  contacts_csv.close()