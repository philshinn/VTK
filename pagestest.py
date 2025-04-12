import xml.etree.ElementTree as etree

def readDrawIOXMLFile(fileName):                               # parses an exported draw.io regular XML graphical VUI design into python objects
        dbg = True
        if dbg: print("--> readXMLFile")
        tree = etree.parse(fileName)                                    # parse the XML file
        root = tree.getroot()                                           # get the root
        if dbg: print("Hello",root.items())
        for diagram in root:
            if dbg: print(diagram)
            mxGraphModel = diagram[0]
            root = mxGraphModel[0]
            for element in root:
                 if dbg: print(element.tag)


        #for child in realRoot:                                              # for each object in the file
        #    if child.tag == 'object':                                       # parse it and assign it to a python representation
        #        self.objectReadHandler(child)
        if dbg: print("<-- readXMLFile")

if __name__ == "__main__":
    dbg = False
    result = readDrawIOXMLFile("VTK 2.35.xml")
