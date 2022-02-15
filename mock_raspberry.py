from time import sleep
import json
import sys
from git import Repo
from github import Github

class RaspPIManager(object):

    def __init__(self):
        ''' Constructor '''
        self.listOfAccess = []
        self.isReading = False
        self.githubUserToken = ''
        self.filepathToToken = './token.dat'
        self.filepathAccessFile = './repository/access_list.dat'

    def setToken(self):
        ''' Reading token from file '''
        # Opening file
        try:
            token = open(self.filepathToToken, "r")
        except IOError:
            print('Por favor, verifique o arquivo com o token.')

        self.githubUserToken = str(token.readline())
        token.close()
        print(self.githubUserToken)

    def writeTag(self, data):
        ''' Write function '''

        #while True:
        #    #text = 'Tiago Onofre'
        #    print("Aproxime a tag")
        #    reader.write(json.dumps(data))
        #    print('Tag preenchida!')
        #    sleep(5)
        #    GPIO.cleanup()
        #    break
        print("Writed")

    def readTag(self):
        ''' Read function '''

        #try:
        #    while True:
        #        print("Aproxime a tag")
        #        id, data = reader.read()
        #        print(data)
        #        # send data to repo
        #        sleep(5)
        #except KeyboardInterrupt:
        #    GPIO.cleanup()
        #    raise
        return "data test"

    def pushToRepo(self):
        ''' Push data to repo '''

        #gituser = Github(self.githubUserToken)
        repo_dir = './'
        repo = Repo(repo_dir)#gituser.get_user().get_repo("IoT-RFID-RASPPI")
        fileList = [
            self.filepathAccessFile
        ]
        commitMessage = 'Updating access list in the repository'
        repo.index.add(fileList)
        repo.index.commit(commitMessage)
        origin = repo.remote('origin')
        origin.push()

    def writeAccessData(self, data):
        ''' Write read data to file '''

        # Opening file
        try:
            accessFile = open(self.filepathAccessFile, "a+")
        except IOError:
            print('Por favor, verifique o arquivo para depositar os acessos.')

        accessFile.seek(0)
        data_file = accessFile.read(1000)
        size = len(data_file)
        # if is not empty
        if size > 0:
            accessFile.write('\n\n')
            accessFile.write('{} - '.format(size+1))

        accessFile.write(data)
        accessFile.close()

    def argsService(self, args):
        ''' Arguments processing '''

        if len(args) != 2:
            print('''Por favor execute conforme o exemplo:
python3 raspberry.py r ou w
r -> leitura
w -> escrita''')
            sys.exit(1)

        if args[1].lower() == 'r':
            self.isReading = True

    def exec(self, args):
        ''' Main method '''

        self.argsService(args)

        if self.isReading:
            print("reading method")
            self.writeTag("test")
            sys.exit(0)
        #else

        print("writing method")
        self.setToken()
        data = self.readTag()
        self.writeAccessData(data)
        self.pushToRepo()
        sys.exit(0)

#--------------------------------------------------------------------------------------------------

manager = RaspPIManager()

manager.exec(sys.argv)
