# Script to scrape images from Google Images
!git clone https://github.com/Joeclinton1/google-images-download.git
!cd google-images-download && sudo python setup.py install
!googleimagesdownload --keywords "Vehicle License Plate" --limit 10
