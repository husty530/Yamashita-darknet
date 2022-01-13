import sys

ag = sys.argv
data_dir = ag[1]
classes = int(ag[2])
cfg_template = ag[3]
width = int(ag[4])
height = int(ag[5])
channels = int(ag[6])
batch_size = int(ag[7])
subdivisions = int(ag[8])
max_batches = int(ag[9])

writing_lines = []
filters = 15 + classes * 3
with open(cfg_template, 'r') as file:
  for line in file:
    if 'width=' in line:
      writing_lines.append(f'width={width}\n')
    elif 'height=' in line:
      writing_lines.append(f'height={height}\n')
    elif 'channels=' in line:
      writing_lines.append(f'channels={channels}\n')
    elif 'batch=' in line:
      writing_lines.append(f'batch={batch_size}\n')
    elif 'subdivisions=' in line:
      writing_lines.append(f'subdivisions={subdivisions}\n')
    elif 'max_batches' in line:
      writing_lines.append(f'max_batches={max_batches}\n')
    elif 'steps=' in line:
      writing_lines.append(f'steps={int(max_batches*0.8)},{int(max_batches*0.9)}\n')
    elif 'classes=' in line:
      writing_lines.append(f'classes={classes}\n')
    elif 'filters=255' in line:
      writing_lines.append(f'filters={filters}\n')
    else:
      writing_lines.append(line)
with open(f'{data_dir}/.cfg', 'w') as file:
  for line in writing_lines:
    file.write(line)
with open(f'{data_dir}/.data', 'w') as file:
  file.write(f'class = {classes}\n')
  file.write(f'train = workspace/{data_dir}/train.txt\n')
  file.write(f'valid = workspace/{data_dir}/valid.txt\n')
  file.write(f'names = workspace/{data_dir}/.names\n')
  file.write(f'backup = workspace/{data_dir}/backup\n')