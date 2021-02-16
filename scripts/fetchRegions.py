import urllib.request, json 
import os

def printRegion(region, parent, path):
    print(path, region['title'])
    # mkdir path + "/" + region['title'] if it doesn't exist
    
    try:
        os.mkdir(path + "/" + region['title'])
    except FileExistsError:
        print("Directory exists, this is fine")

    # create the markdown here region['title'] + ".md"
    print("open file", path + "/" + region['title'] + ".md")
    f = open(path + "/" + region['title'] + ".md", "w")

    # add the top metadata stuff ---
    f.write("---\n")

    # if there is a parent, set the parent 
    if parent != None:
        f.write("parent: " + parent['title'] + "\n")
       
    # has_children: region['children'].isEmpty
    if len(region['children']) > 0:
        f.write("has_children: true\n")
    else:
        f.write("has_children: false\n")
   
    # title: region['title']
    f.write("title: " + region['title'] + "\n")
    # close the top stuff ---
    f.write("---\n")

    f.write("# " + region['title'] + "\n")
    f.close()
    for child in region['children']:
        printRegion(child, region, path + "/" + region['title'])

with urllib.request.urlopen("http://tranquil-garden-84812.herokuapp.com/region") as url:
    data = json.loads(url.read().decode())
    for region in data['result']:
        printRegion(region, None, "../docs")
