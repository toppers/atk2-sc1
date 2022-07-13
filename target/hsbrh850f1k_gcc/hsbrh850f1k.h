/*
 *  TOPPERS ATK2
 *      Toyohashi Open Platform for Embedded Real-Time Systems
 *      Automotive Kernel Version 2
 *
 *  Copyright (C) 2015-2019 by Center for Embedded Computing Systems
 *              Graduate School of Information Science, Nagoya Univ., JAPAN
 *  Copyright (C) 2018-2019 by CRESCO LTD., JAPAN
 *  Copyright (C) 2018-2019 by ICOMSYSTECH Co.,Ltd., JAPAN
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
 *  $Id: hsbrh850f1k.h 886 2019-04-04 08:53:11Z nces-mtakada $
 */
/*
 *		HSBRH850F1Kボードの定義
 */

#ifndef TOPPERS_HSBRH850F1K_H
#define TOPPERS_HSBRH850F1K_H

#include "v850_gcc/rh850_f1k.h"

/*
 *  クロック速度
 */

/*
 *  PLL関連の定義
 */
#define MAINOSC_CLOCK_MHZ	16     /* Main OSC is 16MHz */
#define SUBOSC_CLOCK_KHZ	32768   /* Sub OSC is 32.768kHz */
#define INTOSCH_CLK_MHZ		8       /* High Speed Internal OSC Clock is 8MHz */
#define INTOSCL_CLK_KHZ		240     /* Low Speed Internal OSC Clock is 240kHz */

#define PLL_CLK_MHZ			120 /* PLL is 120MHz */
#define PLLC_DEFAULT_VALUE	0x00010300U
#define PLLC_M				0x01U
#define PLLC_N				0x3BU

/*
 * Port 8 Configuration for LED
 *   P8_4: LED4(OUT)
 *   P8_5: LED3(OUT)
 *   P8_6: LED2(OUT)
 *   P8_7: LED1(OUT)
 */
#define LED_P8_MASK				((uint16) 0x00F0)
#define LED_PM8_INIT			((uint16) 0xFF0F)
#define LED_P8_INIT				((uint16) 0x00F0)

/*
 *  Port 10 Configration for RLIN31
 *   P10_12 : RLIN31TX (第2兼用)
 *   P10_11 : RLIN31RX (第2兼用)
 */
#define RLIN31_P10_MASK			((uint16) 0x1800)
#define RLIN31_PMC10_INIT		((uint16) 0x1800)
#define RLIN31_PFC10_INIT		((uint16) 0x1800)
#define RLIN31_PM10_INIT		((uint16) 0x0800)
#define RLIN31_PIBC10_INIT		((uint16) 0x0800)

/*
 * Macro for hsbrh850f1k_led_output
 */
#define POS_LED1				((uint16) 0x01)
#define POS_LED2				((uint16) 0x02)
#define POS_LED3				((uint16) 0x04)
#define POS_LED4				((uint16) 0x08)
#define POS_LED_ALL				((uint16) 0x0F)

#endif /* TOPPERS_HSBRH850F1K_H */
