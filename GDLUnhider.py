import sys
import shutil
import os

SCRIPTMASTERPOS = 0x0CE
SCRIPT2DPOS = 0x0BE
SCRIPT3DPOS = 0x0AE
SCRIPTPROPPOS = 0x0DE
SCRIPTUIPOS = 0x0EE
SCRIPTPARAMPOS = 0x0FE
SCRIPTFWDMIGRATIONPOS = 0x10E
SCRIPTBWDMIGRATIONPOS = 0x11E

def unlockGDL(sPath, sMacro):
    shutil.move(os.path.join(sPath, sMacro), os.path.join(sPath, "_" + sMacro))

    with open(os.path.join(sPath, "_" + sMacro), "rb") as _file:
        _s = bytearray(_file.read(-1))

        _s[SCRIPTMASTERPOS] = 0
        _s[SCRIPT2DPOS] = 0
        _s[SCRIPT3DPOS] = 0
        _s[SCRIPTPROPPOS] = 0
        _s[SCRIPTUIPOS] = 0
        _s[SCRIPTPARAMPOS] = 0
        _s[SCRIPTFWDMIGRATIONPOS] = 0
        _s[SCRIPTBWDMIGRATIONPOS] = 0

        with open(os.path.join(sPath, sMacro), "wb") as _fileToWrite:
            _fileToWrite.write(_s)


if __name__ == "__main__":
    # for gdlMacro in sys.argv[1:]:
    #     unlockGDL(gdlMacro)

    for dp, dn, names in os.walk(sys.argv[1]):
        for n in names:
            if n.endswith(".gsm"):
                unlockGDL(dp, n)