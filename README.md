# YOLO v4 on Google Colaboratory
  
当リポジトリではLinux環境(Google Colab)でのビルドを想定して、簡単にセットアップができるようにDarknetビルドのYOLOv4ソースコードを配置しています。  
ブラウザさえあれば誰でも動かせますので、以下の手順でやってみましょう。  

## つかいかた  
1. [YOLOv4-Training.ipynb](/YOLOv4-Training.ipynb)をDriveに置き、Google Colaboratoryで開きます。
2. ランタイムのタイプを"GPU"に変更し、一番上のコードブロックで自分のDriveをマウントします。次行、そこにこのリポジトリをクローンしましょう。
3. [workspace](/workspace)内にフォルダを作り、[pumpkin_640_480](/workspace/pumpkin_640_480)を参考に画像とラベルのフォルダを作ります。対応する画像とラベルの名前は必ず同じにしてください。
4. [.names](/workspace/pumpkin_640_480/.names)を編集して、作成したフォルダに置きます。検出したいクラス数だけ改行しながらラベル名を書いてください。
5. ノートブックのconfigと書いてあるエリアでクラス数や画像サイズなどを適切に指定してください。
6. 上からポチポチしていきます。学習開始して、ザーッと画面が流れ始めたら成功です。もし途中でColabの接続が切れた場合でも、100回ごとにモデルは保存されているので再開可能です。自分の作ったフォルダ/backupにあるモデルで続きから学習しましょう。
7. 終わったら、モデルを使って評価実行してみましょう。"_final.weights"が最終成果物です。また、学習の結果はchart.pngみたいなファイルに出力されているはずです。  

darknetだけで学習から推論までできますが、darknetは最適コードでない(らしい)ため少し遅い & Colabでしか動かせないのは悲しいので、OpenCVから呼び出しましょう。[Husty-public](https://github.com/husty530/Husty-public)に行くと、C++,C#,PythonからYOLOを呼び出すコードが置いてあります。C#のみサンプルも置いてあるのですぐに使えます。YOLOv4もYOLOv4-tinyも同じコードで使えるので、学習および実行環境の都合に合わせて使い分けてみてください。    

### ラベリング
正解ラベル付けはColabでなくローカル環境で行います。  
データフォーマットは物体一つにつきスペース区切りで(index) (x) (y) (width) (height)\nです。ただし、すべて画像の幅高さで割って0~1に丸めたものとなります。
ただのテキストファイルなので自作もできますが、[labelImg](https://github.com/tzutalin/labelImg)というフリーソフトが便利なのでそれを使いましょう。  
Python環境があるなら、pipコマンドが使える環境で
```
pip install labelImg
labelImg
```
だけで起動OK。一応ラベル名としてclasses.txtというファイルを置いとかないと動いてくれない仕様になっています。  
なんか怒られた場合は_.namesと同じ内容をdatasetフォルダにコピーしてclasses.txtという名前にしてください。  
