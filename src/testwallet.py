#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="alex"
__date__ ="$06.07.2009 04:29:36$"

import cmd
from kwallet import Wallet, Folder, Entry
import kwallet


class KWalletShell(cmd.Cmd):
    def __init__(self):
        #super(cmd.Cmd,  self ).__init__("")
        cmd.Cmd.__init__(self)
        self.wallet = None
        self.folder = None

    def _updatePrompt(self):
        if self.wallet:
            self.prompt = self.wallet.name
            if self.folder:
                self.prompt+=":"+self.folder.name
        self.prompt+="> "


    def do_lsf(self, cmd):
        for f in self.wallet:
            print f

    def do_ch_folder(self, cmd):
        self.folder = self.wallet.openFolder(cmd)
        self._updatePrompt()

    def do_open(self, cmd):
        self.wallet = Wallet(cmd)
        self._updatePrompt()

    def do_lsw(self,cmd):
        print "dfsadf", cmd
        for wallet in kwallet.get_walletsName():
            print wallet

    def do_exit(self,cmd):return


    def do_lse(self, cmd):
        print "Folder: %s" % self.folder.name
        for e in self.folder:
            print e.name

    def do_get(self, entry):
        if entry in self.folder:
            entry = self.folder.openEntry(entry)
            print entry.name
            print entry.value

    def do_ch_pwd(self,cmd):
        self.wallet.changePassword()

    def do_set(self, entry):
        if entry in self.folder:
            print "overriding existing value!"

        entry = self.folder.openEntry(entry)
        entry.value = input ()



if __name__ == "__main__":
    print kwallet.get_walletsName()

    w = Wallet("kdewallet")
  

    for folder in w:
        print str(folder)
        for    entry in folder:
            print "\t%s" %str(entry)
            d = entry.get_value()
            print d

    cmd = KWalletShell()
    cmd.cmdloop("kwallet started...")
