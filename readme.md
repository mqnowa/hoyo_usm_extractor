Thanks for [@BUnipendix](https://github.com/BUnipendix/PyCriUsm)

# Usage

Clone **this repository** and [**PyCriUsm**](https://github.com/BUnipendix/PyCriUsm) on your PC

```
git clone https://github.com/mqnowa/hoyo_usm_extractor
git clone https://github.com/BUnipendix/PyCriUsm
```

### Preparing PyCriUsm

Build the decorder.

```
cd [...]/PyCriUsm

python setup.py build_ext --inplace
```

Rename `decrypt.xxxxxxxxxxxxx.pyd` to `decrypt.pyd`.

Move it to `cri_usm_demuxer` dir.

### Preparing Hoyo USM Extractor (this repository)

```
cd [...]/hoyo_usm_extractor
```

**Install ffmpeg and add path.** (i.e. Enable to use ffmpeg command.)

**Create `your_pycriusm_path.txt`** and write PyCriUsm path.

Run `main.py`

```
main.py -i USM_PATH -o OUTPUT_DIR -ch 2
```

```
-i: usm file to input
-o: output dir
-ch: channel 0: cn, 1: en, 2: jp, 3: kr
-vc: ffmpeg video codec. (h264, hevc, ...) default, "copy"
-ac: ffmpeg audio codec. (aac, ...) default, "aac"
```