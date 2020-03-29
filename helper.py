import os 
root = os.path.dirname(os.path.abspath(__file__))
# print(rel_root)
assets = os.path.relpath(os.path.join(root, 'assets'), root)
pubs_dir = os.path.join(assets, 'pub_files')
_publications = os.path.relpath(os.path.join(root, '_publications'), root)

class title:
    abb = ['gba', 'msme', 'apec', 'sme', 'gvc']
    def __init__(self, raw_title):
        self.raw_title = raw_title
        self._space_title = raw_title.replace('_', ' ')
    def format(self):
        words = self._space_title.split()
        def cap(word):
            if word in title.abb:
                return word.upper()
            elif len(word) <= 3:
                return word
            return word.capitalize()
        formatted = ' '.join([words[0].capitalize()] + [cap(word.lower()) for word in words[1:]])
        return formatted

def gen_pub_col():
    def pdf_only(file):
        filename, ext = os.path.splitext(file)
        return filename if ext == '.pdf' else None

    raw_titles = [pdf_only(f) for f in os.listdir(pubs_dir)]
    r_pubs = [raw_title for raw_title in raw_titles]
    for r_pub in r_pubs:
        f_pub = title(r_pub).format()
        md_file = os.path.join(_publications, f_pub.replace(" ","-")).lower() + '.md'
        ## pdf2img for the 1st page for pub in os.path.join(pubs_dir, r_pub)
        with open(md_file, "w") as md:
            front_matter = f'''---
title: {f_pub}
date: 2020-01-01
excerpt: |
  by authors
  work-paper-?
sidebar:
  - image: 'assets/images/{r_pub}.jpg'
    image_alt: '{r_pub}'
header:
#   teaser: 'assets/images/{r_pub}.jpg'
  og_image: 'assets/images/{r_pub}.jpg'
  actions:
    - label: '<i class="fas fa-download"></i> Download'
      url: '{os.path.join(pubs_dir, r_pub)}.pdf'
---
# Abstract
Abstract here.
        '''
            md.write(front_matter)
            print(f'''Wrote frontmatter to {md_file}''')

gen_pub_col()

from pdf2image import convert_from_path
# publication_folder = ROOT_DIR+'/static/download/publications/'
img_pub_folder = '/Users/macone/Documents/asc-remake/assets/images'
for file in os.listdir(pubs_dir):
    cover = convert_from_path(pdf_path=os.path.join(
        pubs_dir, file), dpi=100, first_page=1, last_page=1, size=(350,500))[0]
    file_path = os.path.join(img_pub_folder, os.path.splitext(file)[0]+'.jpg')
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'{file} deleted.')
    cover.save(file_path, 'JPEG')
    print(f'{file} saved at {file_path}')

# class jekyll:
#     def __init__(self):
#         self.root_dir = os.path.dirname(os.path.abspath(__file__))
#         self._folders = [i for i in os.listdir(self.root_dir)]
#         self.dir = {folder: os.path.join(self.root_dir, folder) for folder in self._folders}
#         self.config = os.path.join(self.root_dir, '_config.yml')

#     def format_filename(self, dir:str):
#         for item in os.listdir(dir):
#             item_dir = os.path.join(dir, item)
#             item_newdir = os.path.join(dir, item.replace(' ','_'))
#             if os.path.isfile(item_dir):
#                 os.rename(item_dir, item_newdir)
#                 print(f'{os.path.split(item_dir)[1]} -> {os.path.split(item_newdir)[1]}')

#     def create_folder(new_folder:str):
#         try:
#             os.mkdir(os.join(self.root_dir, new_folder))
#         except OSError:
#             print(f'{new_folder} created')
#         else:
#             print(f'folder exists.')


#     def gen_collection(self, collection:str):
#         self.create_folder(f'_{collection}')
#         with open(self.config, 'r') as f:
#             _config = f.readlines()
#             collection_section = _config.index('# collections')
#             content = f'''
#   - scope:
#       path: ''
#             '''
#             _config = _config.insert(collection_section, content)



# class jekyll:
#     def __init__(self):
#         self.root_dir = os.path.dirname(os.path.abspath(__file__))
#         self._folders = [i for i in os.listdir(self.root_dir)]
#         self.dir = {folder: os.path.join(self.root_dir, folder) for folder in self._folders}
#         self.config = os.path.join(self.root_dir, '_config.yml')

#     def format_filename(self, dir:str):
#         for item in os.listdir(dir):
#             item_dir = os.path.join(dir, item)
#             item_newdir = os.path.join(dir, item.replace(' ','_'))
#             if os.path.isfile(item_dir):
#                 os.rename(item_dir, item_newdir)
#                 print(f'{os.path.split(item_dir)[1]} -> {os.path.split(item_newdir)[1]}')

#     def create_folder(new_folder:str):
#         try:
#             os.mkdir(os.join(self.root_dir, new_folder))
#         except OSError:
#             print(f'{new_folder} created')
#         else:
#             print(f'folder exists.')


#     def gen_collection(self, collection:str):
#         self.create_folder(f'_{collection}')
#         with open(self.config, 'r') as f:
#             _config = f.readlines()
#             collection_section = _config.index('# collections')
#             content = f'''
#   - scope:
#       path: ''
#             '''
#             _config = _config.insert(collection_section, content)

