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
# $Id: configure_body.py 929 2021-01-06 08:51:23Z nces-mtakada $
#

import os.path
import os
import shutil

# call common file
common.Source(src_abs_path + "/arch/ccrh/common.py")

src_abs_path = os.path.abspath(SRCDIR)
wd_abs_path = os.path.abspath('.')
cfg_mtsp = wd_abs_path + r"\cfg\cfg.mtsp"
kernel_mtsp = wd_abs_path + r"\kernel\kernel.mtsp"
atk2_sc1_mtpj = wd_abs_path + r"\atk2-sc1.mtpj"


if COPY_SAMPLE1:
	shutil.copy(src_abs_path + r'/sample/sample1.c', '.')
	shutil.copy(src_abs_path + r'/sample/sample1.h', '.')
	shutil.copy(src_abs_path + r'/sample/sample1.arxml', '.')
	shutil.copy(src_abs_path + r'/sample/Rte_Type.h', '.')

#
# close project
#
#project.Close() 
print wd_abs_path + "\\atk2-sc1"
project.Create(wd_abs_path + "\\atk2-sc1",
				MicomType.RH850, 
				TARGET_MCU, 
				ProjectKind.Empty,
				Compiler.CC_RH,
				False)

project.Create(wd_abs_path + "\\cfg\\cfg",
				MicomType.RH850, 
				TARGET_MCU, 
				ProjectKind.Empty,
				Compiler.CC_RH,
				True)

project.Create(wd_abs_path + "\\kernel\\kernel",
				MicomType.RH850, 
				TARGET_MCU, 
				ProjectKind.Library,
				Compiler.CC_RH,
				True)

#
# Change debug tool
#
debugger.DebugTool.Change(DebugTool.E1Lpd)

#
# Add files for atk2-sc1 project
#
for file in app_app_files:
	project.File.Add(wd_abs_path + "\\" + file, u"app")

for file in app_sysmod_files:
	project.File.Add(src_abs_path + "\\" + file, u"sysmod")

for file in app_library_files:
	project.File.Add(src_abs_path + "\\" + file, u"library")

for file in app_configuration_files:
	project.File.Add(wd_abs_path + "\\cfg\\" + file, u"configuration")

str = src_abs_path + '\\' + statup_file
project.File.Add(str, u"startup")

#
# Add files fot cfg project
#
project.Change(cfg_mtsp)

file_list = project.File.Information()
for file in file_list:
	project.File.Remove(file)

str = src_abs_path + '\\' + statup_file
project.File.Add(str, u"startup")

for file in cfg_configuration_files:
	project.File.Add(wd_abs_path + "\\cfg\\" + file, u"configuration")

#
# Add files fot kernel project
#
project.Change(kernel_mtsp)

file_list = project.File.Information()
for file in file_list:
	project.File.Remove(file)

for file in kernel_kernel_files:
	project.File.Add(src_abs_path + "\\" + file, u"kernel")

for file in kernel_arch_files:
	project.File.Add(src_abs_path + "\\" + file, u"arch")

for file in kernel_target_files:
	project.File.Add(src_abs_path + "\\" + file, u"target")

project.Close(True)


#
# Modify atk2-sc1.mtpfj
#
inputstr = ReadFile('atk2-sc1.mtpj')

# Set cx include path
inputstr = NewSetCCRHIncludes(inputstr, atk2_sc1_rel_includes, INCLUDES, SRCDIR)
# Set libary path and file
#inputstr = NewSetLibIncludes(inputstr, atk2_sc1_lib_includes, [], SRCDIR)
inputstr = NewSetLibFiles(inputstr, atk2_sc1_lib_files)
# change Option
inputstr = ChangeItemXml(inputstr, 'OutputMessageFormat-0', '%Program% %Options%')
#inputstr = ChangeItemXml(inputstr, 'UseProEpiRuntimeLibrary-0', 'False')
#inputstr = ChangeItemXml(inputstr, 'HexadecimalFileFormat-0','MotrolaSType32Bit')
inputstr = ChangeItemXml(inputstr, 'HexOptionOutputFileName-0', r'%ProjectName%.srec')
#inputstr = ChangeItemXml(inputstr, 'OutputLinkMapFile-0', 'True')
inputstr = ChangeItemXml(inputstr, 'LinkOptionShowSymbol-0', 'True')
#inputstr = ChangeItemXml(inputstr, 'OutputSymbolInformationToLinkMapFile-0', 'True')
inputstr = ChangeItemXml(inputstr, 'DebuggerProperty-EssentialProperty-Clock-MainClockGeneration', MAIN_CLK)
inputstr = ChangeItemXml(inputstr, 'GeneralOptionXreserveR2-0', 'True')
inputstr = ChangeItemXml(inputstr, 'COptionOsize-0', 'AdvancedSpeed')
# Change linkoption if link_option is exist.
try:
	link_option = link_option
	inputstr = ChangeItemXml(inputstr, 'LinkOptionStart-0', link_option)
except NameError:
	link_option = ''


                                    
# Set user macro definitions
inputstr = NewSetDefine(inputstr, USER_MACRO)

# Set Prebuild/Postbuile
inputstr = NewSetPostbuild(inputstr, atk2_sc1_post_python_files, SRCDIR)

WriteFile('atk2-sc1.mtpj', inputstr)

#
# Modify ./cfg/cfg.mtsp
#
inputstr = ReadFile('./cfg/cfg.mtsp')

# Set cx include path
inputstr = NewSetCCRHIncludes(inputstr, cfg_rel_includes, INCLUDES, "../" + SRCDIR)

# change Option
inputstr = ChangeItemXml(inputstr, 'OutputMessageFormat-0', '%Program% %Options%')
#inputstr = ChangeItemXml(inputstr, 'UseProEpiRuntimeLibrary-0', 'False')
#inputstr = ChangeItemXml(inputstr, 'HexadecimalFileFormat-0','MotrolaSType32Bit')
inputstr = ChangeItemXml(inputstr, 'HexOptionOutputFileName-0', 'cfg1_out.srec')
#inputstr = ChangeItemXml(inputstr, 'OutputLinkMapFile-0', 'True')
inputstr = ChangeItemXml(inputstr, 'LinkOptionShowSymbol-0', 'True')
inputstr = ChangeItemXml(inputstr, 'HexOptionOutputFolder-0', '.')

# Set Prebuild/Postbuile
inputstr = NewSetPrebuild(inputstr, cfg_pre_python_files, "../" + SRCDIR)
inputstr = NewSetPostbuild(inputstr, cfg_post_python_files, "../" + SRCDIR)

# Set user macro definitions
inputstr = NewSetDefine(inputstr, USER_MACRO)

WriteFile('./cfg/cfg.mtsp', inputstr)

#
# Mofity ./kernel/kernel.mtsp
#
inputstr = ReadFile('./kernel/kernel.mtsp')

# Add user macro definitions
kernel_define = kernel_define + USER_MACRO

# Set cx include path
inputstr = NewSetCCRHIncludes(inputstr, kernel_rel_includes, INCLUDES, "../" + SRCDIR)
# Set cx define
inputstr = NewSetDefine(inputstr, kernel_define)
# Set cx addition option
inputstr = NewSetCAddOpt(inputstr, kernel_c_addopt)
inputstr = NewSetAsmAddOpt(inputstr, kernel_asm_addopt)

# change Option
inputstr = ChangeItemXml(inputstr, 'OutputMessageFormat-0', '%Program% %Options%')
#inputstr = ChangeItemXml(inputstr, 'UseProEpiRuntimeLibrary-0', 'False')
inputstr = ChangeItemXml(inputstr, 'GeneralOptionXreserveR2-0', 'True')
inputstr = ChangeItemXml(inputstr, 'COptionOsize-0', 'AdvancedSpeed')

WriteFile('./kernel/kernel.mtsp', inputstr)

project.Open(wd_abs_path + r'\atk2-sc1.mtpj')
project.Change(atk2_sc1_mtpj)
