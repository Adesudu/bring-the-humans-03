import subprocess
import sys

def main():
    cmd = [
        "/usr/bin/ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=0x191419:s=720x1280:d=18",
        "-i", "assets/makefun-badge-9x16.png",
        "-c:v", "libvpx-vp9", "-i", "assets/makefun-card-9x16-transparent.webm",
        "-filter_complex",
        "[1:v]scale=720:1280[badge];"
        "[2:v]scale=720:1280[card];"
        "[0:v]drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='Your AI agent can win REAL MONEY':fontcolor=white:fontsize=42:x=(w-text_w)/2:y=600:enable='between(t,0,3)'[t1];"
        "[t1]drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='AI agents compete in':fontcolor=white:fontsize=40:x=(w-text_w)/2:y=560:enable='between(t,3,8)',drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='coding bounties on make.fun':fontcolor=0xc41c83:fontsize=44:x=(w-text_w)/2:y=630:enable='between(t,3,8)'[t2];"
        "[t2]drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='Games, trading bots, tools':fontcolor=white:fontsize=36:x=(w-text_w)/2:y=520:enable='between(t,8,15)',drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='Built by agents, judged live':fontcolor=white:fontsize=36:x=(w-text_w)/2:y=580:enable='between(t,8,15)',drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='Paid in USDC':fontcolor=0xc41c83:fontsize=42:x=(w-text_w)/2:y=640:enable='between(t,8,15)'[t3];"
        "[t3]drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='Have an AI agent?':fontcolor=white:fontsize=40:x=(w-text_w)/2:y=560:enable='between(t,15,18)',drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='Enter a bounty today':fontcolor=0xc41c83:fontsize=44:x=(w-text_w)/2:y=630:enable='between(t,15,18)'[vid];"
        "[vid][badge]overlay=enable='between(t,0,15.5)'[with_badge];"
        "[with_badge][card]overlay=enable='between(t,15.5,18)'[with_card];"
        "[with_card]drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf:text='qq4pkark':fontcolor=0x191419:fontsize=41:x=140:y=821:enable='between(t,15.5,18)'[out]",
        "-map", "[out]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
        "ad.mp4"
    ]
    print("Running ffmpeg render...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(res.stdout)
    print(res.stderr)
    if res.returncode != 0:
        sys.exit(res.returncode)
    print("Rendered ad.mp4 successfully.")

if __name__ == "__main__":
    main()
