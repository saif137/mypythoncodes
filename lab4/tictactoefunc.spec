# -*- mode: python -*-

block_cipher = None


a = Analysis(['tictactoefunc.py'],
             pathex=['C:\\Python27:C:\\Python27\\Lib\\site-packages\\pyglet', 'C:\\habibdata\\PycharmProjects\\habib_ctii_fall16\\lab4'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('greebg.gif','C:\\habibdata\\PycharmProjects\\habib_ctii_fall16\\lab4\\greebg.gif','DATA')]
a.datas += [('ttticon.png','C:\\habibdata\\PycharmProjects\\habib_ctii_fall16\\lab4\\ttticon.png','DATA')]
a.datas += [('cross.gif','C:\\habibdata\\PycharmProjects\\habib_ctii_fall16\\lab4\\cross.gif','DATA')]
a.datas += [('o.gif','C:\\habibdata\\PycharmProjects\\habib_ctii_fall16\\lab4\\o.gif','DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='tictactoefunc',
          debug=False,
          strip=False,
          upx=True,
          console=True )
