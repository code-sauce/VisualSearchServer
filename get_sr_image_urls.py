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
BATCH_SIZE = 30000
batch = 0

s = solr.SolrConnection('http://solr-prod.s-9.us:8983/solr/shoprunner')


results = s.query('*:*', fields=['image_url', 'id'], rows=BATCH_SIZE, start=batch*BATCH_SIZE).results
f = open('/Users/saurabhjain/Desktop/sr_image_urls.txt', 'w')
while len(results) > 0:
    s = solr.SolrConnection('http://solr-prod.s-9.us:8983/solr/shoprunner')
    results = s.query('*:*', fields=['image_url'], rows=BATCH_SIZE, start=batch*BATCH_SIZE).results
    images = []
    batch += 1

    print 'received %s - %s results' % ((batch-1)*BATCH_SIZE, batch*BATCH_SIZE)
    image_sets = [x['image_url'] for x in results]
    count = 0
    for image_set in image_sets:
        # has all resolutions. we pick the biggest one for best match (hopefully?)
        best_match_image_url = None
        for image in image_set:
            if image.startswith('180x180|'):
                best_match_image_url = image[8:]
                break
        if not best_match_image_url:
            continue
        images.append(best_match_image_url)

    #f.write('\n'.join(['<img src="%s"></img>' % x for x in images]))
    f.write('\n'.join(images))
    print 'Written: %s - %s results to file' % ((batch-1)*BATCH_SIZE, batch*BATCH_SIZE)
