import os

def merge_data():
  header = None
  data_csv = open('data.csv', 'w')

  for root, folders, files in os.walk('.'):
    for folder in folders:
      for _root, _folders, _files in os.walk(folder):
        for _file in _files:
          if _file == 'data.csv':
            with open(os.path.join(folder, _file)) as csv_file:
              if not header:
                header = True
                data_csv.write(csv_file.readline())
                
                for line in csv_file:
                  data_csv.write(line)
              
              else:
                next(csv_file)
                for line in csv_file:
                  data_csv.write(line)

  data_csv.close()