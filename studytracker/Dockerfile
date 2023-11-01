#Python3イメージ

FROM python:3.9
ENV PHTHONUNBUFFERED 1

#ビルド時にディレクトリ作成
RUN mkdir /studytracker

#ワークディレクトリの設定
WORKDIR /studytracker

#requirements.txtを/code下にコピー
ADD requirements.txt /studytracker/

#requirements.txtを基にpip installする
RUN pip3 install -r requirements.txt
ADD . /studytracker/
