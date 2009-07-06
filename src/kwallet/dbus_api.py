#!/usr/bin/python

__author__="Alexander Weigl <alexweigl@gmail.com>"
__date__=""
__version__="0.1"

__all__= ( 'SERVICENAME', 'PATH',
           '_proxy',
           'signal_allWalletsClosed,'
           'signal_applicationDisconnected,'
           'changePassword,'
           'close,'
           'close,'
           'closeAllWallets,'
           'createFolder,'
           'deleteWallet,'
           'disconnectApplication,'
           'entryList,'
           'entryType,'
           'folderDoesNotExist,'
           'folderList,'
           'signal_folderListUpdated,'
           'hasEntry,'
           'hasFolder,'
           'isEnabled,'
           'isOpen,'
           'isOpen,'
           'keyDoesNotExist,'
           'localWallet,'
           'networkWallet,'
           'open,'
           'openAsync,'
           'openPath,'
           'openPathAsync,'
           'readEntry,'
           'readEntryList,'
           'readMap,'
           'readMapList,'
           'readPassword,'
           'readPasswordList,'
           'reconfigure,'
           'removeEntry,'
           'removeFolder,'
           'renameEntry,'
           'users,'
           'signal_walletAsyncOpened,'
           'signal_walletClosed,'
           'signal_walletClosed,'
           'signal_walletCreated,'
           'signal_walletDeleted,'
           'signal_walletListDirty,'
           'signal_walletOpened,'
           'wallets,'
           'writeEntry,'
           'writeEntry,'
           'writeMap,'
           'writePassword,'
        ) 

SERVICENAME='org.kde.kwalletd'
INTERFACE='org.kde.KWallet'
PATH='/modules/kwalletd'

import dbus
dbus.SystemBus()
__sessionBus = dbus.SessionBus()

_proxy = dbus.Interface( __sessionBus.get_object(SERVICENAME, PATH) ,
                                dbus_interface=INTERFACE)
    

    
def signal_allWalletsClosed( callback ,  ):
    '''signal void org.kde.KWallet.allWalletsClosed()'''
    return _proxy.connect_to_signal("allWalletsClosed", callback, None)    
    
def signal_applicationDisconnected( callback , wallet, application ):
    '''signal void org.kde.KWallet.applicationDisconnected(QString wallet, QString application)'''
    return _proxy.connect_to_signal("applicationDisconnected", callback, None)    
    
def changePassword( wallet, wId, appid ):
    '''method void org.kde.KWallet.changePassword(QString wallet, qlonglong wId, QString appid)'''
    return _proxy.changePassword(wallet, wId, appid)
    
def close( wallet, force ):
    '''method int org.kde.KWallet.close(QString wallet, bool force)'''
    return _proxy.close(wallet, force)
    
def close( handle, force, appid ):
    '''method int org.kde.KWallet.close(int handle, bool force, QString appid)'''
    return _proxy.close(handle, force, appid)
    
def closeAllWallets(  ):
    '''method void org.kde.KWallet.closeAllWallets()'''
    return _proxy.closeAllWallets()
    
def createFolder( handle, folder, appid ):
    '''method bool org.kde.KWallet.createFolder(int handle, QString folder, QString appid)'''
    return _proxy.createFolder(handle, folder, appid)
    
def deleteWallet( wallet ):
    '''method int org.kde.KWallet.deleteWallet(QString wallet)'''
    return _proxy.deleteWallet(wallet)
    
def disconnectApplication( wallet, application ):
    '''method bool org.kde.KWallet.disconnectApplication(QString wallet, QString application)'''
    return _proxy.disconnectApplication(wallet, application)
    
def entryList( handle, folder, appid ):
    '''method QStringList org.kde.KWallet.entryList(int handle, QString folder, QString appid)'''
    return _proxy.entryList(handle, folder, appid)
    
def entryType( handle, folder, key, appid ):
    '''method int org.kde.KWallet.entryType(int handle, QString folder, QString key, QString appid)'''
    return _proxy.entryType(handle, folder, key, appid)
    
def folderDoesNotExist( wallet, folder ):
    '''method bool org.kde.KWallet.folderDoesNotExist(QString wallet, QString folder)'''
    return _proxy.folderDoesNotExist(wallet, folder)
    
def folderList( handle, appid ):
    '''method QStringList org.kde.KWallet.folderList(int handle, QString appid)'''
    return _proxy.folderList(handle, appid)
    
def signal_folderListUpdated( callback , wallet ):
    '''signal void org.kde.KWallet.folderListUpdated(QString wallet)'''
    return _proxy.connect_to_signal("folderListUpdated", callback, None)    
    
    
def hasEntry( handle, folder, key, appid ):
    '''method bool org.kde.KWallet.hasEntry(int handle, QString folder, QString key, QString appid)'''
    return _proxy.hasEntry(handle, folder, key, appid)
    
def hasFolder( handle, folder, appid ):
    '''method bool org.kde.KWallet.hasFolder(int handle, QString folder, QString appid)'''
    return _proxy.hasFolder(handle, folder, appid)
    
def isEnabled(  ):
    '''method bool org.kde.KWallet.isEnabled()'''
    return _proxy.isEnabled()
    

def isOpen( namehandle ):
    '''method bool org.kde.KWallet.isOpen({string,int} handle)'''
    return _proxy.isOpen(namehandle)
    
def keyDoesNotExist( wallet, folder, key ):
    '''method bool org.kde.KWallet.keyDoesNotExist(QString wallet, QString folder, QString key)'''
    return _proxy.keyDoesNotExist(wallet, folder, key)
    
def localWallet(  ):
    '''method QString org.kde.KWallet.localWallet()'''
    return _proxy.localWallet()
    
def networkWallet(  ):
    '''method QString org.kde.KWallet.networkWallet()'''
    return _proxy.networkWallet()
    
def open( wallet, wId, appid ):
    '''method int org.kde.KWallet.open(QString wallet, qlonglong wId, QString appid)'''
    return _proxy.open(wallet, wId, appid)
    
def openAsync( wallet, wId, appid, handleSession ):
    '''method int org.kde.KWallet.openAsync(QString wallet, qlonglong wId, QString appid, bool handleSession)'''
    return _proxy.openAsync(wallet, wId, appid, handleSession)
    
def openPath( path, wId, appid ):
    '''method int org.kde.KWallet.openPath(QString path, qlonglong wId, QString appid)'''
    return _proxy.openPath(path, wId, appid)
    
def openPathAsync( path, wId, appid, handleSession ):
    '''method int org.kde.KWallet.openPathAsync(QString path, qlonglong wId, QString appid, bool handleSession)'''
    return _proxy.openPathAsync(path, wId, appid, handleSession)
    
def readEntry( handle, folder, key, appid ):
    '''method QByteArray org.kde.KWallet.readEntry(int handle, QString folder, QString key, QString appid)'''
    return _proxy.readEntry(handle, folder, key, appid)
    
def readEntryList( handle, folder, key, appid ):
    '''method QVariantMap org.kde.KWallet.readEntryList(int handle, QString folder, QString key, QString appid)'''
    return _proxy.readEntryList(handle, folder, key, appid,  utf8_strings=True)
    
def readMap( handle, folder, key, appid ):
    '''method QByteArray org.kde.KWallet.readMap(int handle, QString folder, QString key, QString appid)'''
    return _proxy.readMap(handle, folder, key, appid)
    
def readMapList( handle, folder, key, appid ):
    '''method QVariantMap org.kde.KWallet.readMapList(int handle, QString folder, QString key, QString appid)'''
    return _proxy.readMapList(handle, folder, key, appid)
    
def readPassword( handle, folder, key, appid ):
    '''method QString org.kde.KWallet.readPassword(int handle, QString folder, QString key, QString appid)'''
    return _proxy.readPassword(handle, folder, key, appid)
    
def readPasswordList( handle, folder, key, appid ):
    '''method QVariantMap org.kde.KWallet.readPasswordList(int handle, QString folder, QString key, QString appid)'''
    return _proxy.readPasswordList(handle, folder, key, appid)
    
def reconfigure(  ):
    '''method void org.kde.KWallet.reconfigure()'''
    return _proxy.reconfigure()
    
def removeEntry( handle, folder, key, appid ):
    '''method int org.kde.KWallet.removeEntry(int handle, QString folder, QString key, QString appid)'''
    return _proxy.removeEntry(handle, folder, key, appid)
    
def removeFolder( handle, folder, appid ):
    '''method bool org.kde.KWallet.removeFolder(int handle, QString folder, QString appid)'''
    return _proxy.removeFolder(handle, folder, appid)
    
def renameEntry( handle, folder, oldName, newName, appid ):
    '''method int org.kde.KWallet.renameEntry(int handle, QString folder, QString oldName, QString newName, QString appid)'''
    return _proxy.renameEntry(handle, folder, oldName, newName, appid)
    
    
def users( wallet ):
    '''method QStringList org.kde.KWallet.users(QString wallet)'''
    return _proxy.users(wallet)
    
def signal_walletAsyncOpened( callback , tId, handle ):
    '''signal void org.kde.KWallet.walletAsyncOpened(int tId, int handle)'''
    return _proxy.connect_to_signal("walletAsyncOpened", callback, None)    
    
def signal_walletClosed( callback , wallet ):
    '''signal void org.kde.KWallet.walletClosed(QString wallet)'''
    return _proxy.connect_to_signal("walletClosed", callback, None)    
    
def signal_walletClosed( callback , handle ):
    '''signal void org.kde.KWallet.walletClosed(int handle)'''
    return _proxy.connect_to_signal("walletClosed", callback, None)    
    
def signal_walletCreated( callback , wallet ):
    '''signal void org.kde.KWallet.walletCreated(QString wallet)'''
    return _proxy.connect_to_signal("walletCreated", callback, None)    
    
def signal_walletDeleted( callback , wallet ):
    '''signal void org.kde.KWallet.walletDeleted(QString wallet)'''
    return _proxy.connect_to_signal("walletDeleted", callback, None)    
    
def signal_walletListDirty( callback ,  ):
    '''signal void org.kde.KWallet.walletListDirty()'''
    return _proxy.connect_to_signal("walletListDirty", callback, None)    
    
def signal_walletOpened( callback , wallet ):
    '''signal void org.kde.KWallet.walletOpened(QString wallet)'''
    return _proxy.connect_to_signal("walletOpened", callback, None)    
    
def wallets(  ):
    '''method QStringList org.kde.KWallet.wallets()'''
    return _proxy.wallets()
    
def writeEntry( handle, folder, key, value, appid ):
    '''method int org.kde.KWallet.writeEntry(int handle, QString folder, QString key, QByteArray value, QString appid)'''
    return _proxy.writeEntry(handle, folder, key, value, appid)
    
def writeEntryT( handle, folder, key, value, entryType, appid ):
    '''method int org.kde.KWallet.writeEntry(int handle, QString folder, QString key, QByteArray value, int entryType, QString appid)'''
    return _proxy.writeEntry(handle, folder, key, value, entryType, appid)
    
def writeMap( handle, folder, key, value, appid ):
    '''method int org.kde.KWallet.writeMap(int handle, QString folder, QString key, QByteArray value, QString appid)'''
    return _proxy.writeMap(handle, folder, key, value, appid)
    
def writePassword( handle, folder, key, value, appid ):
    '''method int org.kde.KWallet.writePassword(int handle, QString folder, QString key, QString value, QString appid)'''
    return _proxy.writePassword(handle, folder, key, value, appid)
    
#def Get(interface_name, property_name):
#    '''method QDBusVariant org.freedesktop.DBus.Properties.Get(QString interface_name, QString property_name)'''
#    return _proxy.Get(interface_name, property_name)
    
#def GetAll(interface_name):
#    '''method QVariantMap org.freedesktop.DBus.Properties.GetAll(QString interface_name)'''
#    return _proxy.GetAll(interface_name)
    
#def Set(interface_name, property_name, value):
#    '''method void org.freedesktop.DBus.Properties.Set(QString interface_name, QString property_name, QDBusVariant value)'''
#    return _proxy.Set(interface_name, property_name, value)
    
#def Introspect():
#    '''method QString org.freedesktop.DBus.Introspectable.Introspect()'''
#    return _proxy.Introspect()
