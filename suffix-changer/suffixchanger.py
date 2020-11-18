#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-

import sys
import pathlib
import shutil
import argparse

verbose = True

def rename_suffix(ext_before, ext_after,path):
	files = list(pathlib.Path(path).rglob('*.{0}'.format(ext_before)))
	total = len(files)
	for count, before in enumerate(files, 1):
		after = before.with_name('{0}.{1}'.format(before.stem,ext_after))
		if verbose:
			print('{0}/{1}: {2} -> {3}'.format(count,total,before,after))
			shutil.move(before, after)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This is a suffix changer. If you need help, you should run this with option -h')
	parser.add_argument('-a', '--after',help='suffix after change')
	parser.add_argument('-b','--before',help='suffix before change')
	parser.add_argument('-p','--path',help='running directory',default='./')

	args = parser.parse_args()
	rename_suffix(args.before,args.after,args.path)
