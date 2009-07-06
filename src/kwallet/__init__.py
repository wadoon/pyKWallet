"""
Higher level interface for kwallet
"""
import dbus
import kwallet


import struct, codecs
import kwallet.dbus_api as api
import sys
from random import randint 
from functools import partial
__author__="Alexander Weigl <alexweigl@gmail.com>"
__date__ ="$06.07.2009 00:14:18$"
__version__="0.1"

# module variables
_appName = sys.argv[0].strip('./ ')

rand = partial(randint, 0, 2**32)

TYPE_UNKNOWN=0
TYPE_PASSWORD=1
TYPE_BINARY=2
TYPE_MAP=3

read_method= {
    TYPE_UNKNOWN:api.readEntry,
    TYPE_PASSWORD: api.readPassword,
    TYPE_BINARY: api.readEntry,
    TYPE_MAP:api.readMap
    }


write_method= {
    TYPE_UNKNOWN:api.readEntry,
    TYPE_PASSWORD: api.writePassword,
    TYPE_BINARY: api.readEntry,
    TYPE_MAP:api.writeMap
    }

#module functions

def get_users():api.users()

def set_applicationName(appName):
    kwallet._appName = appName

def get_applicationName():
    return kwallet._appName

def get_walletsName():
    return api.wallets()

def localWallet(  ):
    '''method QString org.kde.KWallet.localWallet()'''
    return api.localWallet()

def networkWallet(  ):
    '''method QString org.kde.KWallet.networkWallet()'''
    return api.networkWallet()

#lowlevel

def closeAllWallets(): return api.closeAllWallets()
def isEnabled(): return api.isEnabled()
def isOpen(wallet_name): return api.isOpen(wallet_name)
#Higher level
class Wallet(object):
    def __init__(self, name, appname=None):
        if not appname:
            appname = get_applicationName()
        
        self.name = name
        self.appName = appname
        self.wId = rand()
        self.handle = api.open(self.name , self.wId , self.appName)
    
    def __contains__(self, key):return self.hasFolder(key)

    def __del__(self):
        #api.close(self.handle, True, self.appName)
        pass
        
    def __iter__(self): 
        return iter(self.folders())

    def __str__(self):
        return "<%s: name=%s, handle=%s, appName=%s>" %("Wallet",
                    self.name, self.handle, self.appName )

    def isOpen(self):
        return api.isOpen(self.handle)    

    def hasFolder(self, name):
        return api.hasFolder(self.handle, name, self.wallet.appName)

    def disconnect(self):
        return   api.disconnectApplication(self.name,self.appName)

    def createFolder(self, name):
        return api.createFolder(self.handle, folder, self.appName)

    def deleteWallet(self):
        return api.deleteWallet(self.name)

    def folders(self):
        return [ Folder(self, folder)
                    for folder in  api.folderList(self.handle,self.appName)]

    def addfolderChangeHandler(self,callback):
        return api.signal_folderListUpdated(callback, self.name)

    def changePassword(self):
        return api.changePassword(self.name, self.wId, self.appName)

    def openFolder(self, foldername):
        return Folder(self, foldername)


class Folder(object):
    def __init__(self, wallet, name):
        self.wallet = wallet
        self.name = name

    def __iter__(self): return iter(self.entries())
    def __contains__(self, key):return self.hasEntry(key)

    def __str__(self):
        return "<%s: wallet=%s, name=%s>" %("Folder",
                self.wallet, self.name )

    def hasEntry(self, name):
        return api.hasEntry(self.wallet.handle, self.name,
                            name, self.wallet.appName)

    def remove(self):
        return api.removeFolder( self.wallet.handle,
                    self.name, self.wallet.appName)

    def entries(self):
        return [ Entry(self.wallet, self, entry)
                    for entry in api.entryList(
                    self.wallet.handle, self.name,
                    self.wallet.appName)
                ]

    def openEntry(self, name):
        return Entry(self.wallet, self, name)


class Entry(object):
    def __init__(self, wallet, folder, name):
        self.wallet = wallet
        self.folder = folder
        self.name = name
        self.__type = None


    def __str__(self):
        return "<%s: wallet=%s, folder=%s, name=%s, type=%s>" %( "Entry",
                self.wallet.name, self.folder.name, self.name, self.get_type() )

    def remove(self):
        return api.removeEntry(self.wallet.handle,
                            self.folder,
                            self.name,
                            self.wallet.appName)
    def rename(self, to):
        return api.renameEntry(self.wallet.handle,
                            self.folder, self.name , to,
                            self.wallet.appName)

    def get_type(self):
        if self.__type is None:
            self.__type = api.entryType(self.wallet.handle,
                            self.folder.name,
                            self.name,
                            self.wallet.appName)
        return self.__type
   

    def set_type(self, type):
        self.__type=type
        api.writeEntry( self.wallet.handle,
                            self.folder.name,
                            self.name,
                            self.value,
                            self.__type,
                            self.wallet.appName)


    def get_value(self):
        print read_method[self.type].func_name
        bytes = read_method[self.type](self.wallet.handle,
                            self.folder.name,
                            self.name,
                            self.wallet.appName)
    
    
        if self.type == TYPE_PASSWORD:
            return bytes
        elif self.type in (TYPE_UNKNOWN, TYPE_BINARY ):
            return bytes
        elif self.type == TYPE_MAP:
            return _mapToDict(bytes)

    def set_value(self,object):
        if type(object) is dict:
            typ=TYPE_MAP
            binary = dictToMap(object)
        elif type(object) in ( str, unicode ):
            typ=TYPE_PASSWORD
            binary = (object)
        else:
            typ=TYPE_UNKNOWN
            binary = unicodeToBytes(repr(object))

        return write_method[typ]( self.wallet.handle,
                            self.folder.name,
                            self.name,
                            binary,
                            self.wallet.appName)

    value= property(get_value, set_value, None, "")
    type = property(get_type, set_type, None, "")


def dictToMap(d):
    dictToMap.buffer = ""

    def pack(fmt, *args):
        dictToMap.buffer +=struct.pack(fmt, *args)
        
    def writestring(s):
        s=codecs.utf_16_be_encode(s)[0]
        pack("!I%ds"%len(s),len(s), s)
       

    pack("!I",len(d))
    
    for i in d:
        writestring(i)
        writestring(d[i])
        
    return dictToMap.buffer

def _mapToDict(bytes):
    return mapToDict( ''.join( [ unichr(i) for i in bytes] ))

def mapToDict(bytes):
    mapToDict.offset=0
    mapToDict.buffer = bytes

    def unpack(fmt):        
        sz = struct.calcsize(fmt)
        val = struct.unpack_from(fmt,
                mapToDict.buffer, mapToDict.offset)
        mapToDict.offset+=sz
        return val[0]

    def readstring():
        chars= unpack("!I")
        print mapToDict.offset, chars
        s = unpack("%ds"%chars)
        return codecs.utf_16_be_decode(s)[0]
    
    d = {}
    items = unpack("!I")
    for i in xrange(items):
        key = readstring()
        value = readstring()
        d[key]=value        
    return d


def unicodeToBytes(s):
     s=codecs.utf_16_be_encode(s)[0]
     return struct.pack("!I%ds"%len(s),len(s), s)

def bytesToUnicode(o):
    s = ""
    
    if type(o) is dbus.Dictionary:
        k, o = o.popitem()

    zipped = zip( o[0::2], o[1::2]  )

    for upper,lower in zipped:
        s += unichr( ( upper << 8) | lower   )

    return s