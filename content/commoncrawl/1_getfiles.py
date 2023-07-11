
import requests
import gzip
import io
from warcio import ArchiveIterator

def get_urls_for_domain(domain, index_list):
    urls = []
    # http://index.commoncrawl.org/CC-MAIN-2023-06-index?url=idman24.com/*&output=json
    for index in index_list:
        cc_url  = "http://index.commoncrawl.org/CC-MAIN-{0}-index?url={1}/*&output=json".format(index, domain)
        response = requests.get(cc_url)
        if response.status_code == 200:
            pages = response.content.splitlines()
            for page in pages:
                urls.append(json.loads(page)['url'])
    return urls

#urls=get_urls_for_domain("newsyouneed.info", ["2023-14"])
#print(urls)



def get_page_content(url):
    #offset, length = int(url.split('=')[1]), int(url.split('&')[2].split('=')[1])
    
    offset, length = 328655012,48579
    offset_end = offset + length - 1
    # com,icccricketworldcupstreaming)/ 20230130121809 {"url": "https://icccricketworldcupstreaming.com/", "mime": "text/html", "mime-detected": "text/html", "status": "200", "digest": "U5PGEQNM5EHVW26ZG5ZXHYNNL6FGEUZP", "length": "48579", "offset": "328655012", "filename": "crawl-data/CC-MAIN-2023-06/segments/1674764499816.79/warc/CC-MAIN-20230130101912-20230130131912-00046.warc.gz", "charset": "UTF-8", "languages": "eng"}
    prefix = 'https://commoncrawl.s3.amazonaws.com/'
    prefix = 'https://data.commoncrawl.org/'
    url="crawl-data/CC-MAIN-2023-06/segments/1674764499845.10/warc/CC-MAIN-20230131055533-20230131085533-00326.warc.gz"
    # https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-06/segments/1674764499845.10/warc/CC-MAIN-20230131055533-20230131085533-00326.warc.gz
    # We'll get the file via HTTPS so we don't need to worry about S3 credentials
    resp = requests.get(prefix + url, headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})

    # The page is stored compressed (gzip) to save space
    # We can extract it using the GZIP library
    raw_data = io.BytesIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)
    
    # What we have now is just the WARC response, formatted:
    data = f.read()

    print(data)
    
    response = ""
    
    for record in ArchiveIterator(data):
        if record.rec_type == 'response':
            response = record.content_stream().read()

    return response

print(get_page_content(""))
