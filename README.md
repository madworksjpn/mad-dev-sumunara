# Sumunara
## Theme
* マクロサービスから入り、ミクロなコミュニティが複数存在するSNSの構築
* 福岡にいかにして、住民の力を借りて福岡市への移住者を増やすかをテーマにした、プラットフォームの提供
* トークンエコノミーで貨幣流通の掌握

## 事前準備
このプロジェクトに参加する方は、以下の事前準備を行ってください。

* 概要説明を受ける
* 各種アカウントを発行する
* 環境を構築する
    * 手順1
    * 手順2

## 環境
* AWS SAM

![Sumunara 概念図](https://image-iwata.s3-ap-northeast-1.amazonaws.com/image/sumunara_%E3%82%A2%E3%83%BC%E3%82%AD.png)

| Function| Function outline | Other |
| ------------- | ------------- | ------------- |
| CloudFront | Stack Management |  |
| Cognito | User Management | With Amplify |
| Lambda | Execute Function |  |
| API Gateway | API |  |

## git rules
### git flow(successful branch model)
* ブランチ
    * develop・・・開発用メインブランチ
        * feature・・・新しい機能を開発するのに使用
    * release・・・次期リリースの内容を反映（ステージング環境と同期）
    * master・・・リリース版（商用環境と同期）
        * hotfix・・・バグフィックス時に使用

* リリース手順
    * developブランチ⇒releaseブランチ⇒developブランチ
        * releaseブランチをstaging環境反映
        * QA実施
    * releaseブランチ⇒masterブランチ※リリース毎にタグ付け（バージョン）
        * 本番環境反映
        * 本番リリース
        * releaseブランチ削除

* 次期開発
    * 開発中
        * developブランチ⇒featureブランチ
            * developブランチ: 2.0の最新取り込み済状態
            * featureブランチ: 機能追加対応中
        * feature⇒develop マージ完了
            * feature削除
* バグフィックス
    * masterブランチ⇒hotfixブランチ
        * hotfixブランチでバグフィックス
    * hotfixブランチ⇒developブランチ
        * hotfixブランチをdevelop環境に差分反映
    * hotfixブランチ⇒releaseブランチ
        * QA実施
        * hotfixブランチをstaging環境に反映
    * releaseブランチ⇒masterブランチ※リリース毎にタグ付け
        * 本番環境反映
        * 本番リリース
        * releaseブランチ削除

### git command
* git clone
    * master branch
    ```
    git clone https://github.com/madworksjpn/mad-dev-sumunara.git
    ```

    * develop branch
    ```
    git clone -b develop https://github.com/madworksjpn/mad-dev-sumunara.git
    ```

    * feature branch
    ```
    git clone -b feature/XXXXXX https://github.com/madworksjpn/mad-dev-sumunara.git
    ```

* branch作成
    * feature branch
    ```
    git branch  # develop branch から切ることを確認
    git branch feature/XXXXXX
    git checkout feature/XXXXXX
    ```

    * hotfix branch
    ```
    git branch  # masterから切ることを確認
    git branch hotfix
    git checkout hotfix
    ```

* git push & merge
    * feature push
    ```
    git add . 
    git commit -m "message"
    git push origin feature/XXXXXX
    ```

    * feature => develop merge
    ```
    git checkout develop 
    git merge feature/XXXXXX
    git push origin develop
    git branch -d feature/XXXXXX
    ```

    * develop => releace
    ```
    git checkout release 
    git merge develop
    git push origin release
    ```

    * release => master
    ```
    git checkout master 
    git merge release
    git push origin master
    git branch -d release
    ```


    * hotfix => develop
    ```
    git checkout develop 
    git merge hotfix
    git push origin develop
    ```

    * hotfix => release
    ```
    git checkout release 
    git merge hotfix
    git push origin release
    git branch -d hotfix
    ```
