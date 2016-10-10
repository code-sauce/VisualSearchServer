import sys
USER = "ubuntu"
HOST = "52.90.19.2"
AWS = sys.platform != 'darwin'
private_key =  "~/.ssh/cs5356"
CONFIG_PATH = __file__.split('settings.py')[0]

BUCKET_NAME = "aub3visualsearch"
PREFIX = "nyc"
MODEL_GRAPH_PATH = '/Users/saurabhjain/tensorflow/models/inception/'
INDEX_PATH = "/Users/saurabhjain/tensorflow/data/visual_search_index/"
DATA_PATH ="/Users/saurabhjain/tensorflow/data/train/shoes/"  # all shoes images
