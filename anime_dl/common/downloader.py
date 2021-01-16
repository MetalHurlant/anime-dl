#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cloudscraper
from tqdm import tqdm


class Downloader(object):

    @staticmethod
    def file_downloader(ddl, file_name, referer, cookies):
        headers = {
            'Territory': 'US',
            'Referer': referer
        }

        sess = cloudscraper.create_scraper()

        dlr = sess.get(ddl, stream=True, cookies = cookies, headers = headers)  # Downloading the content using python.
        with open(file_name, "wb") as handle:
            for data in tqdm(dlr.iter_content(chunk_size=1024)):  # Added chunk size to speed up the downloads
                handle.write(data)
        print("Download has been completed.")  # Voila