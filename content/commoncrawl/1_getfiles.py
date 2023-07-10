
import requests
import gzip
import io
from warcio import ArchiveIterator

def get_urls_for_domain(domain, index_list):
    urls = []
    for index in index_list:
        cc_url  = "http://index.commoncrawl.org/CC-MAIN-{0}-index?url={1}/*&output=json".format(index, domain)
        response = requests.get(cc_url)
        if response.status_code == 200:
            pages = response.content.splitlines()
            for page in pages:
                urls.append(json.loads(page)['url'])
    return urls

urls=get_urls_for_domain("newsyouneed.info", ["2023-14"])
print(urls)


def get_page_content(url):
    offset, length = int(url.split('=')[1]), int(url.split('&')[2].split('=')[1])
    offset_end = offset + length - 1
    prefix = 'https://commoncrawl.s3.amazonaws.com/'
    
    # We'll get the file via HTTPS so we don't need to worry about S3 credentials
    resp = requests.get(prefix + url, headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})

    # The page is stored compressed (gzip) to save space
    # We can extract it using the GZIP library
    raw_data = io.BytesIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)
    
    # What we have now is just the WARC response, formatted:
    data = f.read()

    response = ""
    
    for record in ArchiveIterator(data):
        if record.rec_type == 'response':
            response = record.content_stream().read()

    return response
