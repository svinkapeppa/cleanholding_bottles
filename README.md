# Cleanholding script related to bottles collection

This script helps admins to understand, when containers should be emptied.
It will possibly aggregate some statistics.

## Usage

Read this section to understand, how to use the script.

### Launching

Run `python main.py -h` to see help.

### Input

Input file should fit the following pattern

| Номер контейнера | Дата       | Заполненность до | Заполненность после | Время приезда водителя | Время отъезда водителя |
|------------------|------------|------------------|---------------------|------------------------|------------------------|
| 1                | 20.11.2018 | 10               | 10                  |                        |                        |
| 2                | 20.11.2018 | 105              | 20                  | 19.45                  | 20.13                  |

### Output

Output file will have the following structure

| Номер контейнера | Скорость | Прогнозируемая заполненность |
|------------------|----------|------------------------------|
| 1                | 15       | 94                           |
| 2                | 4        | 15                           |

### Storage

File [db.csv](db.csv) serves as a full log. It will be generated, if not present in the
project directory. All additional information will be taken from this file.

## Requirements

Script is written on Python 3.6, so you have to have it.
Information on additional packages can be found below.

### Packages

See [requirements](requirements.txt) for full list of additional packages.

### Installation

Run `pip install -r requirements.txt` to get all aditional packages.
