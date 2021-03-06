import solr
from math import log
from PIL import Image
import os
import requests
from StringIO import StringIO
import os
import threading
DATA_DIR = '/Users/saurabhjain/Desktop/images'
#DATA_DIR = '/shoprunner/VisualSearchServer/images/'

MAX_PER_CATEGORY = 40
start = 0
BATCH_SIZE = 10000
batch_count = 0

if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

s = solr.SolrConnection('http://solr-prod.s-9.us:8983/solr/shoprunner')
images = []
results = s.query('*:*', fields=['image_url', 'id'], rows=BATCH_SIZE, start=batch_count*BATCH_SIZE).results
while len(results) > 0:
    s = solr.SolrConnection('http://solr-prod.s-9.us:8983/solr/shoprunner')
    results = s.query('*:*', fields=['image_url', 'id'], rows=BATCH_SIZE, start=batch_count*BATCH_SIZE).results
    batch_count += 1
    image_sets = [(x['image_url'], x['id']) for x in results]
    print 'results received from SOLR'
    count = 0
    for image_set, doc_id in image_sets:
        count += 1
        # has all resolutions. we pick the biggest one for best match (hopefully?)
        best_match_image_url = None
        for image in image_set:
            if image.startswith('180x180|'):
                best_match_image_url = image[8:]
                break
        if not best_match_image_url:
            continue
        if count % 100 == 0:
            print count
        images.append((best_match_image_url, doc_id))

    image_label_count = 0
    for image_url, doc_id in images:
        #print doc_id
        image_label_count += 1
        #response = requests.get(image_url)
        try:
            #img = Image.open(StringIO(response.content))
            os.system('curl "%s" -O %s.jpg' % (image_url, doc_id))
            image_label = '%s.jpg' % doc_id
            #img.save(DATA_DIR + '/%s' % image_label)
        except Exception as ex:
            print ex