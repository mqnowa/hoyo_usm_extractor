from argparse import ArgumentParser
import sys
import os
from pathlib import PurePath
import subprocess

with open("your_pycriusm_path.txt") as f:
    line = f.readline()
    sys.path.append(line.strip())
from cri_usm_demuxer.demux import UsmDemuxer


def main(usm_path: str | None = None, out_dir: str | None = None,
         audio_ch: list[int] | int | None = None,
         video_codec="copy", audio_codec="aac"):
    # Use PyCriUSM
    usm_path = input("usm_path > ") if usm_path is None else usm_path
    out_dir = input("out_dir > ") if out_dir is None else out_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    dmx = UsmDemuxer(usm_path)
    video, audios = dmx.export(out_dir)

    # Marge Video and Audio
    export_path = os.path.join(out_dir, PurePath(usm_path).stem + ".mp4")
    audio_ch = ([audio_ch] if isinstance(audio_ch, int)
                else [int(input("audio_ch > "))] if audio_ch is None or len(audio_ch) == 0
                else audio_ch)

    args = ["ffmpeg"]
    args2 = []
    args.extend(["-i", str(video)])
    args2.extend(["-map", "0:v:0"])
    for i, c in enumerate(audio_ch):
        args.extend(["-i", str(audios[c])])
        args2.extend(["-map", f"{i + 1}:a:{i}"])
    args2.extend(("-c:v", video_codec, "-c:a", audio_codec))
    args2.append(export_path)

    subprocess.run(args + args2)

    for path in [video] + list(audios.values()):
        os.remove(str(path))

    return export_path


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--input", "-i")
    parser.add_argument("--diroutput", "-o")
    parser.add_argument("--audiochannels", "-ch", nargs='*', type=int)
    parser.add_argument("--videocodec", "-vc")
    parser.add_argument("--audiocodec", "-ac")

    args = parser.parse_args()
    a = main(
        usm_path=args.input,
        out_dir=args.diroutput,
        audio_ch=args.audiochannels,
        video_codec="copy" if args.videocodec is None else args.videocodec,
        audio_codec="aac" if args.audiocodec is None else args.audiocodec
    )