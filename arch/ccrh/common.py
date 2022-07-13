#!python
# -*- coding: utf-8 -*-
#
#  TOPPERS ATK2
#      Toyohashi Open Platform for Embedded Real-Time Systems
#      Automotive Kernel Version 2
#
#  Copyright (C) 2013-2021 by Center for Embedded Computing Systems
#              Graduate School of Information Science, Nagoya Univ., JAPAN
#  Copyright (C) 2013-2021 by FUJI SOFT INCORPORATED, JAPAN
#  Copyright (C) 2013-2014 by Panasonic Advanced Technology Development Co., Ltd., JAPAN
#  Copyright (C) 2013-2014 by Renesas Electronics Corporation, JAPAN
#  Copyright (C) 2013-2014 by Sunny Giken Inc., JAPAN
#  Copyright (C) 2013-2014 by TOSHIBA CORPORATION, JAPAN
#  Copyright (C) 2013-2014 by Witz Corporation, JAPAN
#
#  上記著作権者は，以下の(1)～(4)の条件を満たす場合に限り，本ソフトウェ
#  ア（本ソフトウェアを改変したものを含む．以下同じ）を使用・複製・改
#  変・再配布（以下，利用と呼ぶ）することを無償で許諾する．
#  (1) 本ソフトウェアをソースコードの形で利用する場合には，上記の著作
#      権表示，この利用条件および下記の無保証規定が，そのままの形でソー
#      スコード中に含まれていること．
#  (2) 本ソフトウェアを，ライブラリ形式など，他のソフトウェア開発に使
#      用できる形で再配布する場合には，再配布に伴うドキュメント（利用
#      者マニュアルなど）に，上記の著作権表示，この利用条件および下記
#      の無保証規定を掲載すること．
#  (3) 本ソフトウェアを，機器に組み込むなど，他のソフトウェア開発に使
#      用できない形で再配布する場合には，次のいずれかの条件を満たすこ
#      と．
#    (a) 再配布に伴うドキュメント（利用者マニュアルなど）に，上記の著
#        作権表示，この利用条件および下記の無保証規定を掲載すること．
#    (b) 再配布の形態を，別に定める方法によって，TOPPERSプロジェクトに
#        報告すること．
#  (4) 本ソフトウェアの利用により直接的または間接的に生じるいかなる損
#      害からも，上記著作権者およびTOPPERSプロジェクトを免責すること．
#      また，本ソフトウェアのユーザまたはエンドユーザからのいかなる理
#      由に基づく請求からも，上記著作権者およびTOPPERSプロジェクトを
#      免責すること．
#
#  本ソフトウェアは，AUTOSAR（AUTomotive Open System ARchitecture）仕
#  様に基づいている．上記の許諾は，AUTOSARの知的財産権を許諾するもので
#  はない．AUTOSARは，AUTOSAR仕様に基づいたソフトウェアを商用目的で利
#  用する者に対して，AUTOSARパートナーになることを求めている．
#
#  本ソフトウェアは，無保証で提供されているものである．上記著作権者お
#  よびTOPPERSプロジェクトは，本ソフトウェアに関して，特定の使用目的
#  に対する適合性も含めて，いかなる保証も行わない．また，本ソフトウェ
#  アの利用により直接的または間接的に生じたいかなる損害に関しても，そ
#  の責任を負わない．
#
# $Id: common.py 929 2021-01-06 08:51:23Z nces-mtakada $
#

#
# variable definition
#
INCLUDES = []
CFG1_DEF_TABLES = []

#
# set cfg and cfg kernel param
#
CFG = SRCDIR + "cfg/cfg/cfg.exe"
CFG_KERNEL = "atk2"


#
# files for each project 
#
app_files = []
app_configuration_files = ['Os_Lcfg_asm.asm', 'Os_Lcfg.c']
app_sysmod_files = ['sysmod/banner.c', 'sysmod/serial.c', 'sysmod/syslog.c']
app_library_files = ['library/log_output.c', 'library/strerror.c', 'library/t_perror.c', 'library/vasyslog.c']

kernel_kernel_files = ['kernel/alarm.c','kernel/counter.c','kernel/counter_manage.c','kernel/event.c','kernel/interrupt.c','kernel/interrupt_manage.c','kernel/osctl.c','kernel/osctl_manage.c','kernel/resource.c','kernel/scheduletable.c','kernel/task.c','kernel/task_manage.c']

cfg_files = []
cfg_configuration_files = ['cfg1_out.c']

#
# pre/postbuiled file
#
cfg_pre_python_files = ['arch/ccrh/pre_cfg.py']
cfg_post_python_files = ['arch/ccrh/post_cfg.py']
atk2_sc1_post_python_files = ['arch/ccrh/post_atk2.py']

#
# cubesuite+ depend files
#
atk2_sc1_rel_includes = [".","cfg"]
cfg_rel_includes = [".."]
kernel_rel_includes = ["..","..\cfg"]

#
# library
#
#atk2_sc1_lib_includes = []
atk2_sc1_lib_files = [r'kernel\%BuildModeName%\kernel']

#
# cx define
#
kernel_define = ['ALLFUNC', 'TOPPERS_LABEL_ASM']


#
# cx additional option
#  -Xno_warning=20177 : Suppress warnings no refer label(exit_no_errorhooh, d_exit_no_errorhook) 
kernel_c_addopt = ['-Xno_warning=20177']
#  -Xno_warning=50013 : Use r1 register as source register
kernel_asm_addopt = ['-Xno_warning=50013']

#
# Set cfg path and srdir path
#
cfg = proj_rel_dir + CFG
srcdir = proj_rel_dir + SRCDIR

#
# soucre target file
#
execfile(srcdir + "target/" + TARGET + "/target.py")

#
# merge files
#
app_files.append(statup_file)
app_files = app_files + app_sysmod_files + app_library_files
kernel_files = kernel_kernel_files + kernel_target_files + kernel_arch_files

#
# Set include path and cfg1_def_table
#
INCLUDES = USER_INCLUDE + ["", "arch", "include", "kernel", "arch", "sysmod", "library"] + INCLUDES
CFG1_DEF_TABLES = ["kernel/kernel_def.csv"] + CFG1_DEF_TABLES

API_TABLE = "kernel/kernel.csv"
INI_FILE  = "kernel/kernel.ini"

CFG_TF = "target/" + TARGET + "/target.tf"
CFG_OFFSET_TF = "target/" + TARGET + "/target_offset.tf"
CFG_CHECK_TF = "target/" + TARGET + "/target_check.tf"

#
# cfg input files
#
cfg_rel_files = []
cfg_input_str = ""
for cfg_filename in CFGNAME:
	cfg_rel_file = cfg_filename + '.arxml'

 	cfg_list = [proj_rel_dir + cfg_rel_file]
 	for inc_path in INCLUDES:
 		cfg_list = cfg_list + [src_abs_path + '/' + inc_path  + '/' + cfg_rel_file]

 	flg = 0
 	for cfg_rel_file in cfg_list:
 		if os.path.exists(cfg_rel_file):
			cfg_rel_files.append(cfg_rel_file)
 			flg = 1
 			break

	if flg == 0:
		print "WARNING!! : Not Exist %s" % cfg_filename

cfg_input_str = " ".join(cfg_rel_files)

#
# make cfg include path
#
cfg_includes = ""
for include in INCLUDES:
	cfg_includes = cfg_includes + " -I" + srcdir + include

#
# make cfg1_def_table
#
cfg_cfg1_def_tables = ""
for cfg1_def_table in CFG1_DEF_TABLES:
	cfg_cfg1_def_tables = cfg_cfg1_def_tables + " --cfg1-def-table " + srcdir + cfg1_def_table

#
# Set api_table
#
cfg_api_table = srcdir + API_TABLE

#
# Set ini_file
#
cfg_ini_file = srcdir + INI_FILE

#
# Set tf 
#
cfg_tf =  srcdir + CFG_TF

#
# Set offset tf 
#
cfg_offset_tf =  srcdir + CFG_OFFSET_TF

#
# Set check tf 
#
cfg_check_tf =  srcdir + CFG_CHECK_TF

#
#
# Functions
#
#
import re

#
# Set Cx Includes
# 
def SetCxIncludes(inputstr, include_list, rel_include_list, relpath):
	cx_includes = ""
	for include in rel_include_list:
		include_list.append(relpath + include)
	for include in include_list:
		cx_includes = cx_includes + include + "\n"
	cx_includes = cx_includes.replace('/', r'\\')
	pattern_pre = r'(\s\<AdditionalIncludePaths-0\>)[\s\S]+?(\</AdditionalIncludePaths-0\>)'
	pattern_post = r'\1' + cx_includes + r'\2'
	inputstr = re.sub (pattern_pre, pattern_post, inputstr)
	return inputstr

#
# ChangeSetItemXml
#
def ChangeItemXml(inputstr, xml_pattern, newitemstr):
	pattern_pre = r'<' + xml_pattern + r'>[\s\S]+?</' + xml_pattern + '>'
	pattern_post = '<' + xml_pattern + '>' + newitemstr + '</' + xml_pattern + '>'
	inputstr = re.sub (pattern_pre, pattern_post, inputstr)
	return inputstr

#
# NewSetItemXml
#
def NewSetItemXml(inputstr, xml_pattern, newitemstr):
	pattern_pre = r'\<' + xml_pattern + r' /\>'
	pattern_post = r'<' + xml_pattern + r'>' + newitemstr + '</' + xml_pattern + r'>'
	inputstr = re.sub (pattern_pre, pattern_post, inputstr)
	return inputstr

#
# NewSetItemXmlOnce
#
def NewSetItemXmlOnce(inputstr, xml_pattern, newitemstr):
	pattern_pre = r'\<' + xml_pattern + r' /\>'
	pattern_post = r'<' + xml_pattern + r'>' + newitemstr + '</' + xml_pattern + r'>'
	inputstr = re.sub (pattern_pre, pattern_post, inputstr, 1)
	return inputstr

#
# New set Cx Include
#
def NewSetCxIncludes(inputstr, include_list, rel_include_list, relpath):
	cx_includes = ""
	for include in rel_include_list:
		include_list.append(relpath + include)
	for include in include_list:
		cx_includes = cx_includes + include + "\n"
	cx_includes = cx_includes.replace('/', r'\\')
	return NewSetItemXml(inputstr, 'AdditionalIncludePaths-0', cx_includes)

def NewSetCCRHIncludes(inputstr, include_list, rel_include_list, relpath):
	ccrh_includes = ""
	for include in rel_include_list:
		include_list.append(relpath + include)
	for include in include_list:
		ccrh_includes = ccrh_includes + include + "\n"
	ccrh_includes = ccrh_includes.replace('/', r'\\')
	return NewSetItemXml(inputstr, 'COptionI-0', ccrh_includes)

#
# New set library Include
#
def NewSetLibIncludes(inputstr, include_list, rel_include_list, relpath):
	lib_includes = ""
	for include in rel_include_list:
		include_list.append(relpath + include)
	for include in include_list:
		lib_includes = lib_includes + include + "\n"
	lib_includes = lib_includes.replace('/', r'\\')
	return NewSetItemXml(inputstr, 'AdditionalLibraryPaths-0', lib_includes)

#
# New set library files
#
def NewSetLibFiles(inputstr, file_list):
	lib_files = ""
	for file in file_list:
		lib_files = lib_files + file + "\n"
	lib_files = lib_files.replace('/', r'\\')
	return NewSetItemXml(inputstr, 'LinkOptionLibrary-0', lib_files)

#
# New set prebuild
#
def NewSetPrebuild(inputstr, rel_command_list, relpath):
	command_str = ''
	for command in rel_command_list:
		command_str = command_str + relpath + command
	command_str = r'#!python\ncommon.Source("' + command_str + r'")\n'
	return NewSetItemXml(inputstr, 'PreBuildCommands-0', command_str)


#
# New set postbuild
#
def NewSetPostbuild(inputstr, rel_command_list, relpath):
	command_str = ''
	for command in rel_command_list:
		command_str = command_str + relpath + command
	command_str = r'#!python\ncommon.Source("' + command_str + r'")\n'
	return NewSetItemXml(inputstr, 'PostBuildCommands-0', command_str)


#
# New set Define
#
def NewSetDefine(inputstr, define_list):
	define_str = ''
	for define in define_list:
		define_str = define_str + define + '\n'
	return NewSetItemXml(inputstr, 'COptionD-0', define_str)

#
# New set additional options
#
def NewSetCAddOpt(inputstr, option_list):
	option_str = ''
	for option in option_list:
		option_str = option_str + option + ' '
	return NewSetItemXmlOnce(inputstr, 'COptionOtherAdditionalOptions-0', option_str)

def NewSetAsmAddOpt(inputstr, option_list):
	option_str = ''
	for option in option_list:
		option_str = option_str + option + ' '
	return NewSetItemXmlOnce(inputstr, 'AsmOptionOtherAdditionalOptions-0', option_str)

#
# Set target file relative path
#
def SetTargetFileRelativePath(inputstr, file_list, relpath):
	relpath_win = re.sub(r'/',r'\\\\', relpath)
	for file_path in file_list:
		file_path = re.sub(r'/',r'\\\\',file_path)
		pattern_pre = r'(\s\<RelativePath\>).+?' + file_path + r'(\</RelativePath\>)'
		pattern_post = r'\1' + relpath_win + file_path + r'\2'
		inputstr = re.sub (pattern_pre, pattern_post, inputstr)
	return inputstr


#
# Set python file relative path
#
def SetPythonFileRelativePath(inputstr, file_list, relpath):
	for file_path in file_list:
		pattern_pre = r'".+?' + file_path + r'"'
		pattern_post = r'"' + relpath + file_path + r'"'
		inputstr = re.sub (pattern_pre, pattern_post, inputstr)
	return inputstr

def ReadFile(filename):
	f = open(filename, "r")
	str = f.read()
	f.close()
	return str

def WriteFile(filename, str):
	f = open(filename, "w")
	str = re.sub (u'\uFEFF', '', str)  ## Delete BOM
	f.write(str)
	f.close()

def WriteFile_B(filename, str):
	f = open(filename, "wb")
	f.write(str)
	f.close()

