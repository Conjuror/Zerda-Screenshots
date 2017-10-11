
import os

counter = 1
colspan = 47
with open("html_sample", "w") as r:

    # write table format EN head
    r.write("""
<h1 class="language">en</h1>
    <hr>
        <table>
        
            <tr>
                <th colspan="{}">
                    <span class="deviceName">phoneScreenshots</span>
                </th>
            </tr>
            <tr>""".format(colspan))
    with open("images.list", "r") as f:
        for l in [x.strip() for x in f.readlines() if x.startswith("####")]:
            x = l[5:].split(". ")
            if x[0].startswith("_"):
                continue
            sample = """
<td>            
    <a href="./en/{}.png" target="_blank" class="screenshotLink">
        <img class="screenshot"
             src="./en/{}.png"
           style="width: 100%;"
             alt="en phoneScreenshots"
    data-counter="{}" />
    </a>
</td>
"""
            r.write(sample.format(x[0], x[0], counter))
            counter += 1

    r.write("""

            </tr>
        
        </table>
    
        <h1 class="language">id</h1>
        <hr>
        <table>
        
            <tr>
                <th colspan="{}">
                    <span class="deviceName">phoneScreenshots</span>
                </th>
            </tr>
        <tr>""".format(colspan))
    counter = 1
    with open("images.list", "r") as f:
        for l in [x.strip() for x in f.readlines() if x.startswith("####")]:
            x = l[5:].split(". ")
            if x[0].startswith("_"):
                continue
            sample = """
<td>            
    <a href="./id/{}.png" target="_blank" class="screenshotLink">
        <img class="screenshot"
             src="./id/{}.png"
           style="width: 100%;"
             alt="id phoneScreenshots"
    data-counter="{}" />
    </a>
</td>
"""
            r.write(sample.format(x[0], x[0], counter))
            counter += 1

    r.write("""
          </tr>
      </table>""")

    print("COUNTER: {}".format(counter-1))


# print file_dict
# for root, dir, fns in os.walk("."):
#     for f in fns:
#         filename, fileext = os.path.splitext(f)
#         if fileext == '.png':
#             if file_dict.has_key(filename):
#                 os.rename(f, filename+"_"+file_dict[filename]+".png")
#             else:
#                 print("Missing {}".format(filename))



###
# 0-1. Onboarding - first
# 0-2. Onboarding - second
# 0-3. Onboarding - third
# 0-4. Onboarding - forth
# 1-1. Home | Long tap on top site
# 1-2. Home | Menu
# 2-1. HOME | Menu | Downloads empty
# 2-2. Home | Menu | Downloads with items
# 2-3. Home | Menu | Downloads with items | item_menu
# 2-4. Home | Menu | Downloads with items | item_menu | Delete file
# 2-5. Home | Menu | Downloads with items | tap on a missing file
# 3-1. Home | Menu | History empty
# 3-2. Home | Menu | History item | item menu (with CLEAR BROWSING HISTORY)
# 3-3. Home | Menu | History item | CLEAR BROWSING HISTORY
# 4-1. Home | Menu | My shots | No screenshots
# 4-2. Home | Menu | My shots | Screenshot item | info
# 4-3. Home | Menu | My shots | Screenshot item | Delete
# 4-4. Home | Menu | My shots | Screenshot item | Delete | DELETE
# 4-5. Home | Menu | My shots | Tap on missing screenshot
# 5-1. Home | Menu | Turbo mode | -> off
# 5-2. Home | Menu | Turbo mode | -> on
# 6-1. Home | Menu | Block image | -> on
# 6-2. Home | Menu | Block image | -> off
# 7-1. Home | Menu | Settings
# 7-2. Home | Menu | Settings | Language
# 7-3. Home | Menu | Settings | Default search engine
# 7-4. Home | Menu | Settings | Clear browsing data
# 7-5. Home | Menu | Settings | Clear browsing data | CLEAR DATA
# 7-6. Home | Menu | Settings | Save downloads to
# 7-7. Home | Menu | Settings | Give feedback
# 7-8. Home | Menu | Settings | Give feedback | No, send feedback
# 7-9. Home | Menu | Settings | Share with friends
# 7-10. Home | Menu | Settings | About
# 7-11. Home | Menu | Settings | About | Your Rights
# 8-1. Home | Menu | Clear cache
# 8-2. Home | Menu | Capture screenshot | Screenshot saved
# 8-3. Home | Menu | Capture screenshot | Failed to capture
# 9-1. Home | Error page
# 9-2. Context menu inside Zerda
# 9-3. Context menu inside Zerda | Save image | finished
# 9-4. Context menu inside Zerda | Download a file | Download using mobile data confirm
# 9-5. Context menu inside Zerda | Download a file | Download started
# 9-6. Context menu inside Zerda | Download a file | Download finished
# 9-7. Context menu inside Zerda | Download a file | Download: No SD card detected
# 9-8. Context menu inside Zerda | Download a file | Download: Saved to SD card
# 9-9. Context menu inside Zerda | Download a file | Download: SD card is full
# 10-1. Context menu from outside app
