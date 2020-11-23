# WaGyUアプリ

## 開発者
- WaGyU/config
  
  このアプリ全体の設定アプリ。

- WaGyU/home
  
  ホーム画面兼牛のパーツ画面の処理とhtmlが入っている。
  
- WaGyU/templates 

  parts_list.htmlにはホーム画面兼牛のパーツの説明ページへのアクセスリンクが貼ってある。
  cssファイルはmanage.pyと同じ階層のstaticに入っている。parts_list.cssを参考に作成すること。
 
- WaGyUtemplates/parts 

  parts_list.htmlからリンクで飛ばされた先のファイルたち。
  牛のパーツ別のhtmlファイルが入っているので、ここから編集すること。


- 牛のパーツの追加
  ```
  python3 manage.py runserver 
  ```
  として、サーバを立ち上げたら、URLにadmin/を追加してログインする。
  牛のパーツを追加したい場合は、Parts modelsというデータベースに追加していく。
