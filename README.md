# Word2Vec

Tutorial for Word2Vec.

Dockerfile contains Python3.6, Mecab, Neologd.

## Getting Started

1. build image  
`$ docker build -t word2vec:1.0 .`
2. run container  
`$ docker run -it -p 8888:8888 -v ~/Desktop/word2vec-gensim-sample:/home word2vec:1.0`

## Stop and Delete
1. stop container
`$ docker stop`
2. delete container
`$ docker rm containerID`
3. delete image
`$ docker rmi imageID`

## Check
1. check docker container
`$ docker ps -a`
2. check docker images
`$ docker images -a`

You can use `$python3` .

Based on https://qiita.com/oreyutarover/items/909d614ca3b48d2c9e16
