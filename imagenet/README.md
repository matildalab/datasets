## Labeling validation datasets
repository를 받게 되면 train 데이터는 tfrecord와 구조가 일치 하지만 validation 데이터의 구조는 일치하지 않습니다.
validation 데이터를 TF-Record format과 일치하는 디렉터리 구조로 변경하는 스크립트입니다.
이미지 데이터는 저작권의 문제로 직접 다운을 받아야합니다. 이미지 데이터가 위치하는 디렉터리 명을 val로 설정합니다.

## Quick Start

image_metadata.txt 과 group_truth.txt 의 정보를 기반으로 이미지를 분류합니다.
```
#image_metadata.txt
#https://gist.github.com/aaronpolhamus/964a4411c0906315deb9f4a3723aac57

#group_truth.txt
#https://github.com/ryujaehun/alexnet/blob/master/etc/data/ILSVRC2012_validation_ground_truth.txt

cd ~/graphcore/tensorflow1/efficientnet
python3 labeling_validation_datasets.py
```
실행전 디렉터리 구조

```
/val
  +-- ILSVRC2012_val_000xxxx1.JPEG
  +-- ILSVRC2012_val_000xxxx2.JPEG
  +-- ILSVRC2012_val_000xxxx3.JPEG
  +-- ILSVRC2012_val_000xxxx4.JPEG
  +-- ..
```

실행 된 후의 디렉터리 구조는 다음과 같습니다.
```
/val
  +-- n01xxx1
  |     +-- ILSVRC2012_val_0001xxx1.JPEG
  |     +-- ILSVRC2012_val_0001xxx2.JPEG
  |     +-- ...
  +-- n01xxx2
  |     +-- ILSVRC2012_val_0002xxx1.JPEG
  |     +-- ILSVRC2012_val_0002xxx1.JPEG
  |     +-- ...
  +-- n01xxx3
  +-- ..
```
이후 다음 코드를 통해 tfrecord 형식으로 변경 합니다.
```
cd ~/examples/applications/tensorflow/cnns/training/Datasets/imagenet-data/ImageNet-to-TFrecord
nohup python3 build_imagenet_data.py -validation_directory ../val -output_directory ../tfrecord &
```
