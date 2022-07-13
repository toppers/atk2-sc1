/*
 *  TOPPERS ATK2
 *      Toyohashi Open Platform for Embedded Real-Time Systems
 *      Automotive Kernel Version 2
 *
 *  Copyright (C) 2015 by Center for Embedded Computing Systems
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
 *  $Id: target_config.c 716 2017-01-19 01:02:05Z ertl-honda $
 */

/*
 *		ターゲット依存モジュール（HSBRH850F1K用）
 */

#include "kernel_impl.h"
#include "v850_gcc/uart_rlin.h"
#include "v850_gcc/prc_sil.h"
#include "target_sysmod.h"
#ifdef ENABLE_RETURN_MAIN
#include "interrupt.h"
#endif /* ENABLE_RETURN_MAIN */
#ifdef TOPPERS_ENABLE_TRACE
#include "logtrace/trace_config.h"
#endif /* TOPPERS_ENABLE_TRACE */

/*
 *  文字列の出力
 */
void
target_fput_str(const char8 *c)
{
	while (*c != '\0') {
		uart_putc(*c);
		c++;
	}
	uart_putc('\n');
}

void
hsbrh850f1k_led_output(uint8 pattern)
{
	uint16 wk;

	pattern = ~pattern;
	wk = sil_reh_mem((void *) P(8));
	wk &= ~LED_P8_MASK;
	wk |= (pattern & LED_P8_MASK);
	sil_wrh_mem((void *) P(8), wk);
}

/*
 *  ポートの初期設定
 */
void
target_port_initialize(void)
{
	uint16 wk;

	/*
	 * PORT8(LED)
	 */
	/* PM8 設定 */
	wk = sil_reh_mem((void *) PM(8));
	wk &= ~LED_P8_MASK;
	wk |= (LED_PM8_INIT & LED_P8_MASK);
	sil_wrh_mem((void *) PM(8), wk);

	/* P8 設定 */
	wk = sil_reh_mem((void *) P(8));
	wk &= ~LED_P8_MASK;
	wk |= (LED_P8_INIT & LED_P8_MASK);
	sil_wrh_mem((void *) P(8), wk);

	/*
	 * PORT10(RLIN31)
	 */
	/* PFC10 設定 */
	wk = sil_reh_mem((void *) PFC(10));
	wk &= ~RLIN31_P10_MASK;
	wk |= (RLIN31_PFC10_INIT & RLIN31_P10_MASK);
	sil_wrh_mem((void *) PFC(10), wk);

	/* PMC10 設定 */
	wk = sil_reh_mem((void *) PMC(10));
	wk &= ~RLIN31_P10_MASK;
	wk |= (RLIN31_PMC10_INIT & RLIN31_P10_MASK);
	sil_wrh_mem((void *) PMC(10), wk);

	/* PM10 設定 */
	wk = sil_reh_mem((void *) PM(10));
	wk &= ~RLIN31_P10_MASK;
	wk |= (RLIN31_PM10_INIT & RLIN31_P10_MASK);
	sil_wrh_mem((void *) PM(10), wk);

	/* PIBC10 設定 */
	wk = sil_reh_mem((void *) PIBC(10));
	wk &= ~RLIN31_P10_MASK;
	wk |= (RLIN31_PIBC10_INIT & RLIN31_P10_MASK);
	sil_wrh_mem((void *) PIBC(10), wk);
}

/*
 *  クロック関係の初期化
 */
void
target_clock_initialize(void)
{
	uint32 errcnt = 0;

	/* Init Main Clock */
	if (EnableMainOSC(MHz(MAINOSC_CLOCK_MHZ)) != UC_SUCCESS) {
		errcnt++;
	}

	/* Init PLL */
	if (EnablePLL() != UC_SUCCESS) {
		errcnt++;
	}

	/* Set PPLLCLK Clock */
	if (SetClockSelection(CKSC_PPLLCLKS_CTL, CKSC_PPLLCLKS_ACT,
						  PNO_CtrlProt1, 0x03, /* PPLLOUT */
						  0, 0, 0) != UC_SUCCESS) {
		errcnt++;
	}

	/* Set CPU Clock */
	if (SetClockSelection(CKSC_CPUCLKS_CTL, CKSC_CPUCLKS_ACT,
						  PNO_CtrlProt1, 0x03, /* CPLLOUT */
						  CKSC_CPUCLKD_CTL, CKSC_CPUCLKD_ACT,
						  0x11 /* 120Mhz */) != UC_SUCCESS) {
		errcnt++;
	}

	/* Set TAUJ Clock */
	if (SetClockSelection(CKSC_ATAUJS_CTL, CKSC_ATAUJS_ACT,
					  PNO_CtrlProt0, 0x02, /* MainOSC */
					  CKSC_ATAUJD_CTL, CKSC_ATAUJD_ACT,
					  0x01) != UC_SUCCESS) {
		errcnt++;
	}

	/* Set RLIN Clock */
	if (SetClockSelection(CKSC_ILINS_CTL, CKSC_ILINS_ACT,
					  PNO_CtrlProt1, 0x02, /* MainOSC */
					  CKSC_ILIND_CTL, CKSC_ILIND_ACT,
					  0x01) != UC_SUCCESS) {
		errcnt++;
	}

	if (errcnt > 0) {
		infinite_loop();
	}
}

/*
 *  ターゲット依存のハードウェアの初期化
 *  スターアップルーチンから呼び出される．
 */
void
target_hardware_initialize(void)
{
	/* クロックの初期設定 */
	target_clock_initialize();

	/* ポートの初期設定 */
	target_port_initialize();
}

/*
 *  ターゲット依存の初期化
 */
void
target_initialize(void)
{
	/*
	 *  V850依存の初期化
	 */
	prc_initialize();

#ifdef TOPPERS_ENABLE_TRACE
	/*
	 *  トレースログ機能の初期化
	 */
	trace_initialize((uintptr) (TRACE_AUTOSTOP));
#endif /* TOPPERS_ENABLE_TRACE */
}

/*
 *  ターゲット依存の終了処理
 */
void
target_exit(void)
{
#ifdef TOPPERS_ENABLE_TRACE
	/*
	 *  トレースログのダンプ
	 */
	trace_dump(target_fput_log);
#endif /* TOPPERS_ENABLE_TRACE */

#ifndef ENABLE_RETURN_MAIN
	/*
	 *  シャットダウン処理の出力
	 */
	target_fput_str("Kernel Exit...");
#else
	target_fput_str("Kernel Shutdown...");
#endif /* ENABLE_RETURN_MAIN */

	/*
	 *  FL-850/F1K依存の終了処理
	 */
	prc_terminate();

#ifdef ENABLE_RETURN_MAIN
	kerflg = FALSE;
	except_nest_cnt = 0U;
	nested_lock_os_int_cnt = 0U;
	sus_all_cnt = 0U;
	sus_all_cnt_ctx = 0U;
	sus_os_cnt = 0U;
	sus_os_cnt_ctx = 0U;

	/* スタックポインタの初期化とmain()の呼び出し */
	return_main();
#endif /* ENABLE_RETURN_MAIN */

	infinite_loop();
}

/*
 *  ターゲット依存の文字出力
 */
void
target_fput_log(char8 c)
{
	if (c == '\n') {
		uart_putc('\r');
	}
	uart_putc(c);
}
