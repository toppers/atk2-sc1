/*
 *  TOPPERS ATK2
 *      Toyohashi Open Platform for Embedded Real-Time Systems
 *      Automotive Kernel Version 2
 *
 *  Copyright (C) 2013-2017 by Center for Embedded Computing Systems
 *              Graduate School of Information Science, Nagoya Univ., JAPAN
 *
 *  上記著作権者は，以下の(1)～(4)の条件を満たす場合に限り，本ソフトウェ
 *  ア（本ソフトウェアを改変したものを含む．以下同じ）を使用・複製・改
 *  変・再配布（以下，利用と呼ぶ）することを無償で許諾する．
 *  (1) 本ソフトウェアをソースコードの形で利用する場合には，上記の著作
 *      権表示，この利用条件および下記の無保証規定が，そのままの形でソー
 *      スコード中に含まれていること．
 *  (2) 本ソフトウェアを，ライブラリ形式など，他のソフトウェア開発に使
 *      用できる形で再配布する場合には，再配布に伴うドキュメント（利用
 *      者マニュアルなど）に，上記の著作権表示，この利用条件および下記
 *      の無保証規定を掲載すること．
 *  (3) 本ソフトウェアを，機器に組み込むなど，他のソフトウェア開発に使
 *      用できない形で再配布する場合には，次のいずれかの条件を満たすこ
 *      と．
 *    (a) 再配布に伴うドキュメント（利用者マニュアルなど）に，上記の著
 *        作権表示，この利用条件および下記の無保証規定を掲載すること．
 *    (b) 再配布の形態を，別に定める方法によって，TOPPERSプロジェクトに
 *        報告すること．
 *  (4) 本ソフトウェアの利用により直接的または間接的に生じるいかなる損
 *      害からも，上記著作権者およびTOPPERSプロジェクトを免責すること．
 *      また，本ソフトウェアのユーザまたはエンドユーザからのいかなる理
 *      由に基づく請求からも，上記著作権者およびTOPPERSプロジェクトを
 *      免責すること．
 *
 *  本ソフトウェアは，AUTOSAR（AUTomotive Open System ARchitecture）仕
 *  様に基づいている．上記の許諾は，AUTOSARの知的財産権を許諾するもので
 *  はない．AUTOSARは，AUTOSAR仕様に基づいたソフトウェアを商用目的で利
 *  用する者に対して，AUTOSARパートナーになることを求めている．
 *
 *  本ソフトウェアは，無保証で提供されているものである．上記著作権者お
 *  よびTOPPERSプロジェクトは，本ソフトウェアに関して，特定の使用目的
 *  に対する適合性も含めて，いかなる保証も行わない．また，本ソフトウェ
 *  アの利用により直接的または間接的に生じたいかなる損害に関しても，そ
 *  の責任を負わない．
 *
 *  $Id: prc_inline_symbols.h 829 2017-09-23 02:08:24Z ertl-honda $
 */

/*
 *		コンパイラ依存定義
 */

#ifndef PRC_INLINE_SYMBOL_H
#define PRC_INLINE_SYMBOL_H

#include "kernel_inline_symbols.h"

/* v850.h */
#pragma inline set_pmr
#pragma inline get_ispr
#pragma inline clear_ispr

/* prc_config.h */
#pragma inline x_lock_all_int
#pragma inline x_unlock_all_int
#pragma inline x_nested_lock_os_int
#pragma inline x_nested_unlock_os_int
#pragma inline x_set_ipm
#pragma inline x_get_ipm
#pragma inline x_disable_int
#pragma inline x_enable_int
#pragma inline x_clear_int
#pragma inline x_probe_int
#pragma inline i_begin_int
#pragma inline i_end_int

/* prc_insn.h */
#pragma inline disable_int
#pragma inline enable_int
#pragma inline current_psw
#pragma inline set_psw

/* prc_sil.h */
#pragma inline sil_reb_mem
#pragma inline sil_wrb_mem
#pragma inline sil_reh_mem
#pragma inline sil_wrh_mem
#pragma inline sil_rew_mem
#pragma inline sil_wrw_mem
#pragma inline TOPPERS_disint
#pragma inline TOPPERS_enaint

/* taua_timer.h */
#pragma inline target_timer_get_current
#pragma inline target_timer_probe_int

/* uart.h */
#pragma inline uart_putc

/* uart.c */
#pragma inline uart_getready
#pragma inline uart_getchar


#endif /* PRC_INLINE_SYMBOL_H */
