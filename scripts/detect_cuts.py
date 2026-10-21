#!/usr/bin/env python3
"""辅助检测视频硬切（场景切换）时间点，供多镜头反推定位切点。

用法:
    python3 detect_cuts.py <video.mp4> [--threshold 0.3] [--min-gap 0.5]

- threshold: ffmpeg scene 分数阈值，0~1，越大越迟钝（默认 0.3）；
  漏检就调低（0.2），误检多就调高（0.4~0.5）。
- min-gap: 相邻切点最小间隔秒，过滤同一切点的重复上报（默认 0.5s）。

依赖 ffmpeg。只输出候选切点时间，需与肉眼抽帧互证，不直接当作最终切点。
"""
import argparse
import re
import subprocess
import sys


def detect(video: str, threshold: float, min_gap: float) -> list[float]:
    vf = f"select='gt(scene,{threshold})',showinfo"
    cmd = [
        "ffmpeg", "-hide_banner", "-i", video,
        "-vf", vf, "-f", "null", "-",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    # showinfo 把时间戳写进 stderr
    stamps = [float(m) for m in re.findall(r"pts_time:([0-9.]+)", r.stderr)]
    cuts: list[float] = []
    for t in stamps:
        if not cuts or t - cuts[-1] >= min_gap:
            cuts.append(round(t, 2))
    return cuts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--threshold", type=float, default=0.3)
    ap.add_argument("--min-gap", type=float, default=0.5)
    args = ap.parse_args()

    cuts = detect(args.video, args.threshold, args.min_gap)
    print(f"=== 候选硬切 {len(cuts)} 处（阈值 {args.threshold}，最小间隔 {args.min_gap}s）===")
    for i, t in enumerate(cuts, 1):
        print(f"cut {i:02d}: {t:.2f}s")
    print("\n提示：候选切点需用 extract_frames.py 在该时间前后密抽复核，"
          "叠化/淡入淡出等软转场不会被硬切阈值捕获。")


if __name__ == "__main__":
    sys.exit(main())
