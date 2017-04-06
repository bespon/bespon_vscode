'''
Install BespON extension for VS Code
'''

import os
import shutil

extension_path = os.path.expanduser('~/.vscode/extensions/')
if not os.path.isdir(os.path.join(extension_path, 'bespon')):
    os.mkdir(os.path.join(extension_path, 'bespon'))
if not os.path.isdir(os.path.join(extension_path, 'bespon', 'syntaxes')):
    os.mkdir(os.path.join(extension_path, 'bespon', 'syntaxes'))

source_files = [os.path.join(*x.split('/')) for x in ('bespon/package.json', 'bespon/language-configuration.json', 'bespon/syntaxes/bespon.tmLanguage.json')]
for f in source_files:
    shutil.copy(f, os.path.join(extension_path, f))
