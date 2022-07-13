/*
 *  TOPPERS ATK2
 *      Toyohashi Open Platform for Embedded Real-Time Systems
 *      Automotive Kernel Version 2
 *
 *  Copyright (C) 2012-2014 by Center for Embedded Computing Systems
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
 *  $Id: prc_insn.h 540 2015-12-29 01:00:01Z ertl-honda $
 */

/*
 *		プロセッサの特殊命令のインライン関数定義（V850用）
 */
#ifndef TOPPERS_PRC_INSN_H
#define TOPPERS_PRC_INSN_H

#include <prc_tool.h>

/*
 *  V850E3V5のみサポート
 */
#ifndef __v850e3v5__
#error Only support v850e3v5 architecture!!
#endif /* __v850e3v5__ */

#ifndef TOPPERS_MACRO_ONLY

#define SYNCM	__syncm();

LOCAL_INLINE void
disable_int(void)
{
	__DI();
}

LOCAL_INLINE void
enable_int(void)
{
	__EI();
}

LOCAL_INLINE uint32
current_psw(void)
{
	return(__stsr_rh(5, 0));
}

LOCAL_INLINE void
set_psw(uint32 psw)
{
	__ldsr_rh(5, 0, psw);
}

/*
 *  V850E3V5用の割込みコントローラ操作ルーチン
 */
LOCAL_INLINE void
set_pmr(uint16 pmr)
{
	uint32 psw;

	/* PMR must be set in di sate(PSW.ID = 1) */
	psw = current_psw();
	disable_int();

	__ldsr_rh(11, 2, pmr);

	set_psw(psw);
}

LOCAL_INLINE uint16
get_ispr(void)
{
	return(__stsr_rh(10, 2));
}

LOCAL_INLINE void
clear_ispr(void)
{
	uint32 psw;

	/* ISPR must be set in di sate(PSW.ID = 1) */
	psw = current_psw();
	disable_int();

	__ldsr_rh(13, 2, 1);    /* INTCFG = 1; ISPR を書き換え可能に */
	__ldsr_rh(10, 2, 0);    /* ISPR = 0 */
	__ldsr_rh(13, 2, 0);    /* INTCFG = 0; ISPR を書き換え禁止に(自動更新に) */
	__syncp();

	set_psw(psw);
}

LOCAL_INLINE void
set_intbp(uint32 intbp)
{
	uint32 psw;

	/* INTBP must be set in di sate(PSW.ID = 1) */
	psw = current_psw();
	disable_int();

	__ldsr_rh(4, 1, intbp);

	set_psw(psw);
}
#endif /* TOPPERS_MACRO_ONLY */

#endif /* TOPPERS_PRC_INSN_H */
