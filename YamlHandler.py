import yaml, os

class YamlHandler:
    """
    YamlHandler is used to handle direct fileaccess with yml files

    it needs modules:
    -   yaml
    -   os
    """

    def __init__ (self, filename):
        """
        initialize YamlHandler

        parameter: filename - contains files name
        """
        self.__ymlFilename = filename

        if not self.__findYml():
            self._newYmlFile()

    def __findYml (self):
        """
        checks if ymlFilename exists in current directory

        returns True or False
        """
        if self.__ymlFilename in os.listdir():
            return True
        else:
            return False

    def _readYml (self):
        """
        reads ymlFilenames content into variable if it exists

        otherwise it returns an error: fileNotFound
        """
        if self.__findYml():
            with open(self.__ymlFilename, 'r') as self.__fstream:
                self.__ymlContent = yaml.safe_load(self.__fstream)
        else:
            raise FileNotFoundError(f"file '{self.__ymlFilename}' does not exists in directory '{os.getcwd()}'")

    def _writeYml (self, append = True):
        """
        writes ymlContent into file ymlFilename if exists

        param append is default true, if set to false existing file will be overwritten

        otherwise it returns an error: fileNotFound
        """
        if self.__findYml() and append:

            with open(self.__ymlFilename, 'a') as self.__fstream:
                yaml.dump(self.__ymlContent, self.__fstream)

        elif self.__findYml and not append:

            with open(self.__ymlFilename, 'w') as self.__fstream:
                yaml.dump(self.__ymlContent, self.__fstream)

        else:

            raise FileNotFoundError(f"file '{self.__ymlFilename}' does not exists in directory '{os.getcwd()}'")

    def _getYmlContent (self):
        """
        returns yaml files content as dict()
        """
        return self.__ymlContent

    def getYmlFilename (self):
        """
        returns configfiles filename
        """
        return self.__ymlFilename

    def _newYmlFile (self):
        """
        creates an new file with the name in the YamlHandler object
        """
        if not self.__findYml():
            self.__fstream = open(self.__ymlFilename, 'w')
            self.__fstream.close()

    def __str__ (self):
        """
        returns yaml files content as seen in the file itself
        """
        with open(self.__ymlFilename, 'r') as self.__fstream:
            return self.__fstream.read()

    def _validateYmlContent (self,content):
        """
        returns true if ymlContent is object of class dict
        """
        return isinstance(content, dict) 

    def setYmlContent(self,newYmlContent):
        """
        sets ymlContent to the value of newYmlContent -> it has to be a dict()
        """
        if self._validateYmlContent(newYmlContent):
            self.__ymlContent = newYmlContent
        else:
            raise TypeError(f"newYmlcontent has wrong type: '{type(newYmlContent)}' it has to be 'dict'")


# Test
if __name__ == "__main__":

    import yaml,os

    yml = YamlHandler('config.yml')
    yml._readYml()   
    yml.setYmlContent({'test': {'zeile1':35}}) 
    yml._writeYml(False)
    yml._readYml()
    print(yml._getYmlContent())
    print(yml)

    