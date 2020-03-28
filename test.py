# import os
# for root, dirs, files in os.walk("."):
#     print(root)
#     # for d in dirs:
#         # print(d)
#         # print(os.path.relpath(os.path.join(root, d), d))
#     # for f in files:
#     #     print(os.path.relpath(os.path.join(root, f), "."))

# import os
# path = {}
# path['cwd'] = os.getcwd()
# path['dirname'] = os.path.dirname(os.path.abspath(__file__))
# path['base'] = os.path.basename(__file__)
# path['abspath'] = os.path.abspath(__file__)
# path['assets'] = os.path.join(path['dirname'],'assets')
# for k, i in path.items():
#     print(k, i)
# relpath = os.path.relpath(path['assets'], path['dirname'])
# print('relpath', relpath)
# print(path['assets'][len(path['dirname']):])
s = '''~/Library/Application Support/Adobe

~/Library/Caches/Adobe

~/Library/Saved Application State/com.adobe.Reader.savedState

~/Library/Caches/com.adobe.Reader

~/Library/Caches/com.adobe.InstallAdobeAcrobatReaderDC

~/Library/Preferences/Adobe

~/Library/Preferences/com.adobe.Reader.plist

~/Library/Preferences/com.adobe.AdobeRdrCEFHelper.plist

~/Library/Logs/Adobe_ADMLogs

~/Library/Logs/Adobe

~/Library/Cookies/com.adobe.InstallAdobeAcrobatReaderDC.binarycookies
'''
for x in [i for i in s.split('\n') if len(i) != 0]:
    print('rm -rf '+x)