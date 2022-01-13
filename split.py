import os, sys

data_dir = sys.argv[1]
percentage_valid = float(sys.argv[2])

file_train = open('train.txt', 'w')
file_valid = open('valid.txt', 'w')
count = 0
index_valid = round(100 / percentage_valid)
file_list = []
for root, dirs, files in os.walk('dataset/'):
  for ext in ['.png', '.PNG', '.jpg', '.JPG', '.jpeg', '.JPEG', '.bmp', '.BMP']:
    file_list.extend([os.path.join(root, file) for file in files if ext in file])
for pathAndFilename in file_list:
  count = count + 1
  title, ext = os.path.splitext(os.path.basename(pathAndFilename))
  if count % index_valid == 0:
    file_valid.write(f'workspace/{data_dir}/dataset/{title}{ext}\n')
  else:
    file_train.write(f'workspace/{data_dir}/dataset/{title}{ext}\n')
file_train.close()
file_valid.close()
print(f'completed dividing {count} image files into "train.txt" and "valid.txt".')