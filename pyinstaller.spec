
# -*- mode: python -*-
 
# if you use pyqt5, this patch must be adjusted
# https://github.com/bjones1/pyinstaller/tree/pyqt5_fix

block_cipher = None
app_name='shutdown_test'
 
a = Analysis(['shutdownPy.py'],
             pathex=[
			 r'C:\Users\AI\AppData\Local\Programs\Python\Python35',
			 r'C:\Users\AI\AppData\Local\Programs\Python\Python35\Lib',
			 r'C:\Users\AI\AppData\Local\Programs\Python\Python35\Lib\site-packages',
			 r'C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64',
			 r'C:\Users\AI\source\repos\shutdownPy',
			 ],
             binaries=[],
             datas=[('./conf.txt', './')],
             hiddenimports=[
							"time",
							"sys",
							"os",
							"socket",
							"base64",
							"json",
							"re",
							"threading",
							"codecs",
							"__future__",
							"cython",
							"pypiwin32",
							"pywin32-ctypes",
							"pywin32",
                            ],
             hookspath=[
						],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=app_name,
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=app_name)
