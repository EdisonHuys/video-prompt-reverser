#!/usr/bin/env python3
"""逐秒/按间隔抽帧并打印视频元数据，供视频反推提示词时逐帧观察。

用法:
    python3 extract_frames.py <video.mp4> [--out frames] [--fps 1] [--count N]

环境需有 ffmpeg / ffprobe。--count N 时改为均匀抽取 N 帧（忽略 --fps）。
输出: 元数据打印到 stdout；帧写入 --out 目录，命名 f_01.jpg ...
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def have(tool: str) -> bool:
    return shutil.which(tool) is not None


def probe(video: Path) -> dict:
    cmd = [
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", str(video),
    ]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"[ffprobe] 无法读取视频: {out.stderr.strip()}")
    data = json.loads(out.stdout)
    v = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
    a = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), None)
    duration = float(data.get("format", {}).get("duration", 0) or 0)
    w, h = v.get("width"), v.get("height")
    nb = v.get("nb_frames")
    try:
        nb_frames = int(nb) if nb else None
    except (TypeError, ValueError):
        nb_frames = None
    return {
        "duration_s": round(duration, 3),
        "width": w,
        "height": h,
        "ratio": f"{w}:{h}" if w and h else None,
        "fps": v.get("r_frame_rate"),
        "nb_frames": nb_frames,
        "has_audio": a is not None,
        "audio_codec": a.get("codec_name") if a else None,
    }


def extract(video: Path, out: Path, fps: float, count: int | None) -> list[Path]:
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("f_*.jpg"):
        old.unlink()
    if count:
        nb = probe(video)["nb_frames"]
        if nb and nb > count:
            # 按总帧数均匀取索引，构造 select 表达式
            idxs = [round(i * (nb - 1) / (count - 1)) for i in range(count)] if count > 1 else [nb // 2]
            cond = "+".join(f"eq(n\\,{i})" for i in sorted(set(idxs)))
            vf = f"select='{cond}'"
        else:
            vf = f"fps={count / probe(video)['duration_s']:.6f}"
    else:
        vf = f"fps={fps}"
    cmd = [
        "ffmpeg", "-y", "-v", "error", "-i", str(video),
        "-vf", vf, "-vsync", "0", str(out / "f_%02d.jpg"),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"[ffmpeg] 抽帧失败: {r.stderr.strip()}")
    return sorted(out.glob("f_*.jpg"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--out", default="frames")
    ap.add_argument("--fps", type=float, default=1.0, help="每秒抽帧数，默认1")
    ap.add_argument("--count", type=int, default=None, help="均匀抽取N帧，优先于--fps")
    args = ap.parse_args()

    if not have("ffmpeg") or not have("ffprobe"):
        sys.exit("缺少 ffmpeg/ffprobe，请先安装")
    video = Path(args.video)
    if not video.exists():
        sys.exit(f"找不到视频: {video}")

    meta = probe(video)
    print("=== 元数据 ===")
    for k, v in meta.items():
        print(f"{k}: {v}")

    frames = extract(video, Path(args.out), args.fps, args.count)
    print(f"\n=== 已抽取 {len(frames)} 帧 -> {Path(args.out).resolve()} ===")
    for f in frames:
        print(f.name)


if __name__ == "__main__":
    main()
