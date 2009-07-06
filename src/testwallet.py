#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Alexander Weigl <alexweigl@gmail.com>"
__date__ ="$06.07.2009 04:29:36$"

from kwallet import Wallet, Folder, Entry
import kwallet


if __name__ == "__main__":
    print kwallet.get_walletsName()

    w = Wallet("kdewallet")
  

    for folder in w:
        print str(folder)
        for    entry in folder:
            print "\t%s" %str(entry)
            d = entry.get_value()
            print d