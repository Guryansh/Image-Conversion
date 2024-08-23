from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': 'images'})
google_crawler.crawl(
    keyword='face',
    max_num=100, )
