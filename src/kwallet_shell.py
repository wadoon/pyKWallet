#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="alex"
__date__ ="$06.07.2009 10:54:24$"


import cmd
from kwallet import Wallet, Folder, Entry
import kwallet


import readline

def input_default(prompt, default):
    def startup_hook():
        readline.insert_text(default)
    readline.set_startup_hook(startup_hook)
    try:
        return raw_input(prompt)
    finally:
        readline.set_startup_hook(None)


class KWalletShell(cmd.Cmd):
    def __init__(self):
        #super(cmd.Cmd,  self ).__init__("")
        cmd.Cmd.__init__(self)
        self.wallet = None
        self.folder = None

    def prettypath(self, wallet=None, folder=None, entry=None ):
        p=""
        if self.wallet:
            p= wallet.name
            if folder:
                p+="::"+folder.name
                if entry:
                    p+=":"+entry.name
        return p



    def _updatePrompt(self):
        self.prompt=self.prettypath(self.wallet , self.folder) + "> "


    def do_lsf(self, cmd):
        for f in self.wallet:
            print self.prettypath(self.wallet, f)

    def help_lsf(self):
        return "list all folders in the wallet"

    def do_ch_folder(self, cmd):
        self.folder = self.wallet.openFolder(cmd)
        self._updatePrompt()

    def help_ch_folder(self):
        return "change folder to first parameter"

    def do_open(self, cmd):
        self.wallet = Wallet(cmd)
        self._updatePrompt()

    def help_open(self):
        return "opens the specified wallet, if wallet does not exists, you ask to create it"

    def do_lsw(self,cmd):
        print "dfsadf", cmd
        for wallet in kwallet.get_walletsName():
            print wallet

    def help_lsw(self):
        return "list all avaiables wallets"

    def do_exit(self,cmd):
        import sys

        del self.folder, self.wallet
        sys.exit(0)
        
    def help_exit(self):
        return "close this shell"


    def do_lse(self, cmd):
        l = self.folder
        for e in l:
            print self.prettypath(self.wallet, self.folder, e)
        else:
            print "No Entries in folder"

    def help_lse(self):
        return "list all entries in the current folder"

    def do_get(self, entry):
        if entry in self.folder:
            entry = self.folder.openEntry(entry)
            print '%s=%s' %(
                self.prettypath(self.wallet, self.folder, e),
                entry.value)

    def help_get(self):
        return "get the value behind the given entry in the current folder and wallet"

    def do_ch_pwd(self,cmd):
        self.wallet.changePassword()

    def help_ch_pwd(self):
        return "change the password for the current wallet"

    def do_set(self, entry):
        if entry in self.folder:
            print "overriding existing value!"

        entry = self.folder.openEntry(entry)
        entry.value = input_default(
            self.prettypath(self.wallet,self.folder, entry)+"="
            , entry.value)


    def help_set(self):
        return "set or override the value for the entry in teh current folder and wallet"


if __name__ == "__main__":
    cmd = KWalletShell()
    cmd.cmdloop("kwallet started..., enjoy")

