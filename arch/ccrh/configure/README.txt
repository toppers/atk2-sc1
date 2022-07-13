
		TOPPERS/ATK2-SC1
        ＜CS+用プロジェクト生成スクリプトマニュアル＞

このドキュメントはCS+用プロジェクト生成スクリプトの情報を記述したもの
である．

----------------------------------------------------------------------
TOPPERS ATK2
    Toyohashi Open Platform for Embedded Real-Time Systems
    Automotive Kernel Version 2

Copyright (C) 2013-2021 by Center for Embedded Computing Systems
            Graduate School of Information Science, Nagoya Univ., JAPAN
Copyright (C) 2013-2014 by FUJI SOFT INCORPORATED, JAPAN
Copyright (C) 2013-2014 by Panasonic Advanced Technology Development Co., Ltd., JAPAN
Copyright (C) 2013-2014 by Renesas Electronics Corporation, JAPAN
Copyright (C) 2013-2014 by Sunny Giken Inc., JAPAN
Copyright (C) 2013-2014 by TOSHIBA CORPORATION, JAPAN
Copyright (C) 2013-2014 by Witz Corporation, JAPAN

上記著作権者は，以下の (1)～(3)の条件を満たす場合に限り，本ドキュメ
ント（本ドキュメントを改変したものを含む．以下同じ）を使用・複製・改
変・再配布（以下，利用と呼ぶ）することを無償で許諾する．
(1) 本ドキュメントを利用する場合には，上記の著作権表示，この利用条件
    および下記の無保証規定が，そのままの形でドキュメント中に含まれて
    いること．
(2) 本ドキュメントを改変する場合には，ドキュメントを改変した旨の記述
    を，改変後のドキュメント中に含めること．ただし，改変後のドキュメ
    ントが，TOPPERSプロジェクト指定の開発成果物である場合には，この限
    りではない．
(3) 本ドキュメントの利用により直接的または間接的に生じるいかなる損害
    からも，上記著作権者およびTOPPERSプロジェクトを免責すること．また，
    本ドキュメントのユーザまたはエンドユーザからのいかなる理由に基づ
    く請求からも，上記著作権者およびTOPPERSプロジェクトを免責すること．

本ドキュメントは，AUTOSAR（AUTomotive Open System ARchitecture）仕様
に基づいている．上記の許諾は，AUTOSARの知的財産権を許諾するものではな
い．AUTOSARは，AUTOSAR仕様に基づいたソフトウェアを商用目的で利用する
者に対して，AUTOSARパートナーになることを求めている．

本ドキュメントは，無保証で提供されているものである．上記著作権者およ
びTOPPERSプロジェクトは，本ドキュメントに関して，特定の使用目的に対す
る適合性も含めて，いかなる保証も行わない．また，本ドキュメントの利用
により直接的または間接的に生じたいかなる損害に関しても，その責任を負
わない．

$Id: README.txt 929 2021-01-06 08:51:23Z nces-mtakada $
----------------------------------------------------------------------

○概要

CS+用プロジェクト生成スクリプトは，RH850用のATK2のプロジェクトを作成す
るスクリプトである．
                
動作確認を行ったCS+のバージョンは次の通りである．

  CS+ V6.03.00, V7.00.00, V8.04.00
  
○使用方法

以下の手順でターゲット用のプロジェクトファイルを生成する．

1.本フォルダ(configure)を適当な場所にコピーする．以下のファイルが含ま
  れている．
  ./configure.mtpj
  ./configure.py
  ./def.py
  ./README.txt

2.def.pyの編集
  以下のdef.pyの設定値を参考に設定する．
  
3.configure.mtpjをダブルクリック
  configure.py が実行され，atk2-sc1.mtpjが作成され開かれる．
  
4.アクティブプロジェクトを変更
  アクティブプロジェクトをatk2-sc1に変更する．  

  
プロジェクトファイル生成後は，atk2-sc1.mtpj を使用する．なお，プロジェ
クトファイル生成後はconfigure.mtpjとconfigure.pyは削除可能である．


○def.pyの設定値

・SRCDIR
 ・ATK2のソースコードのトップとの相対位置
   ./atk2-sc1/yyy/xxx/ にコピーした場合は，，
   
    SRCDIR = "../../"
   となる．
   
・CFGNAME
 ・コンフィギュレーションファイル名の指定．
   入力として必要なXMLファイル名を全て指定．

・TARGET 
 ・ターゲットの指定．./target 以下のいずれかのフォルダ名．
 
・TARGET_MCU
 ・ターゲットMCU名の指定．
 
・app_app_files
 ・アプリケーションファイルの指定．
 
・USER_INCLUDE
 ・インクルードパスの指定
  
・COPY_SAMPLE1  
 ・sample1のファイルを./sampleからコピーするか指定．

○プロジェクト構成

atk2-sc1 : トッププロジェクト
 cfg : サブプロジェクト コンフィギュレータ実行
 kernel : サブプロジェクト カーネルビルド用

○変更履歴

2021/01/06
・CS+ V8.04.00 対応

2017/09/23
・CS+ V6.00.00 対応

2014/10/14
・CS+ V3.00.00 対応

2014/05/01
・ターゲットフォルダ名をv850e2_gccからv850_gccに変更．
・sample1をコピーする際に，Rte_Type.h も対象に追加．
・カーネルビルド時の Rte_Type.h のインクルードのため，Rte_Type.h を置
  いているフォルダをカーネルビルド時のインクルード対象とする．

以上．
