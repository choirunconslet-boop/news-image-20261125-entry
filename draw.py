#!/usr/bin/env python3
"""Draw the 1024x1024 front page for Wednesday 25 November 2026.

Every story below happened, or was first reported, on Wednesday
25 November 2026 (checked against Reuters, Xinhua/AP, the Guardian and
Al Jazeera on the morning of 25 Nov WIB). Figures are the ones reported
that day. Pure PIL vector drawing, no photos, no network.

Stories deliberately left OUT although they lead 25 Nov front pages:
the Huawei guilty verdict, the Houthi strike on Riyadh's tower, the
Zelenskiy/Sparta II confirmation, the Giuliani Medal of Freedom and the
CIA/ODNI breach were all Tuesday 24 Nov events; the DR Congo plane went
missing on Sunday 22 Nov; the NATO "Sputnik-S" reports are 23-24 Nov.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 234)
INK = (26, 26, 26)
RED = (164, 30, 34)
GREY = (90, 86, 76)
PANEL = (255, 253, 245)
RULE = (200, 192, 172)
YELLOW = (255, 200, 60)
BLUE = (30, 80, 140)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning lines that fit `width` px."""
    lines = []
    for para in text.split("\n"):
        words, line = para.split(), ""
        for w in words:
            trial = (line + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = w
        if line:
            lines.append(line)
    return lines


def text_block(draw, x, y, text, fnt, width, fill=INK, leading=1.25):
    for ln in wrap(draw, text, fnt, width):
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


# ---- simple vector icons, each drawn in a s x s box at (x, y) ----

def icon_rocket(d, x, y, s, c):
    # upright rocket: nose cone, body, window, fins, flame
    d.polygon([(x + 0.5 * s, y + 0.02 * s), (x + 0.72 * s, y + 0.28 * s),
               (x + 0.28 * s, y + 0.28 * s)], fill=RED)
    d.rectangle([x + 0.28 * s, y + 0.28 * s, x + 0.72 * s, y + 0.70 * s], fill=c)
    d.ellipse([x + 0.40 * s, y + 0.38 * s, x + 0.60 * s, y + 0.58 * s],
              fill=PAPER, outline=INK, width=2)
    d.polygon([(x + 0.28 * s, y + 0.60 * s), (x + 0.08 * s, y + 0.88 * s),
               (x + 0.28 * s, y + 0.78 * s)], fill=RED)
    d.polygon([(x + 0.72 * s, y + 0.60 * s), (x + 0.92 * s, y + 0.88 * s),
               (x + 0.72 * s, y + 0.78 * s)], fill=RED)
    d.polygon([(x + 0.42 * s, y + 0.72 * s), (x + 0.58 * s, y + 0.72 * s),
               (x + 0.50 * s, y + 0.98 * s)], fill=YELLOW)


def icon_chart_down(d, x, y, s, c):
    # axes + falling line with arrowhead = markets down
    w = max(3, int(0.06 * s))
    d.line([x + 0.08 * s, y + 0.12 * s, x + 0.08 * s, y + 0.92 * s], fill=c, width=w)
    d.line([x + 0.08 * s, y + 0.92 * s, x + 0.95 * s, y + 0.92 * s], fill=c, width=w)
    pts = [(x + 0.14 * s, y + 0.22 * s), (x + 0.36 * s, y + 0.40 * s),
           (x + 0.55 * s, y + 0.34 * s), (x + 0.80 * s, y + 0.72 * s)]
    d.line(pts, fill=RED, width=max(4, int(0.07 * s)), joint="curve")
    d.polygon([(x + 0.80 * s, y + 0.72 * s), (x + 0.66 * s, y + 0.66 * s),
               (x + 0.80 * s, y + 0.52 * s)], fill=RED)


def icon_coins(d, x, y, s, c):
    # stack of three coins with an upward arrow = prices rising
    for i in range(3):
        yy = y + (0.55 - i * 0.16) * s
        d.ellipse([x + 0.12 * s, yy, x + 0.62 * s, yy + 0.22 * s],
                  fill=YELLOW, outline=c, width=3)
    d.line([x + 0.78 * s, y + 0.85 * s, x + 0.78 * s, y + 0.18 * s],
           fill=RED, width=5)
    d.polygon([(x + 0.78 * s, y + 0.06 * s), (x + 0.64 * s, y + 0.26 * s),
               (x + 0.92 * s, y + 0.26 * s)], fill=RED)


def icon_flags(d, x, y, s, c):
    # two crossed flags = treaty / pact
    d.line([x + 0.22 * s, y + 0.10 * s, x + 0.22 * s, y + 0.95 * s], fill=c, width=4)
    d.polygon([(x + 0.22 * s, y + 0.10 * s), (x + 0.58 * s, y + 0.22 * s),
               (x + 0.22 * s, y + 0.34 * s)], fill=RED)
    d.line([x + 0.78 * s, y + 0.10 * s, x + 0.78 * s, y + 0.95 * s], fill=c, width=4)
    d.polygon([(x + 0.78 * s, y + 0.10 * s), (x + 0.42 * s, y + 0.22 * s),
               (x + 0.78 * s, y + 0.34 * s)], fill=BLUE)


def icon_magnifier(d, x, y, s, c):
    # magnifying glass over a star = investigation of a top official
    w = max(4, int(0.08 * s))
    d.ellipse([x + 0.05 * s, y + 0.05 * s, x + 0.62 * s, y + 0.62 * s],
              outline=c, width=w)
    d.line([x + 0.48 * s, y + 0.48 * s, x + 0.88 * s, y + 0.88 * s],
           fill=c, width=w)
    cx, cy, r = x + 0.335 * s, y + 0.335 * s, 0.10 * s
    d.polygon([(cx, cy - r), (cx + 0.32 * r, cy - 0.32 * r),
               (cx + r, cy), (cx + 0.32 * r, cy + 0.32 * r),
               (cx, cy + r), (cx - 0.32 * r, cy + 0.32 * r),
               (cx - r, cy), (cx - 0.32 * r, cy - 0.32 * r)], fill=RED)


def icon_blast(d, x, y, s, c):
    # starburst = controlled detonation
    cx, cy = x + 0.5 * s, y + 0.5 * s
    outer, inner = 0.48 * s, 0.20 * s
    pts = []
    for i in range(16):
        r = outer if i % 2 == 0 else inner
        ang = 3.14159 * i / 8 - 3.14159 / 2
        pts.append((cx + r * __import__("math").cos(ang),
                    cy + r * __import__("math").sin(ang)))
    d.polygon(pts, fill=YELLOW, outline=RED)
    d.ellipse([cx - 0.14 * s, cy - 0.14 * s, cx + 0.14 * s, cy + 0.14 * s],
              fill=RED)


def icon_calendar(d, x, y, s, c):
    # calendar page with three data rows = data due today
    d.rectangle([x + 0.08 * s, y + 0.18 * s, x + 0.92 * s, y + 0.92 * s],
                fill=PANEL, outline=c, width=4)
    d.rectangle([x + 0.08 * s, y + 0.18 * s, x + 0.92 * s, y + 0.38 * s], fill=RED)
    d.line([x + 0.28 * s, y + 0.08 * s, x + 0.28 * s, y + 0.28 * s], fill=c, width=4)
    d.line([x + 0.72 * s, y + 0.08 * s, x + 0.72 * s, y + 0.28 * s], fill=c, width=4)
    for i in range(3):
        yy = y + (0.52 + i * 0.14) * s
        d.line([x + 0.22 * s, yy, x + 0.78 * s, yy], fill=c, width=3)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer frame
    d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=4)
    d.rectangle([18, 18, W - 19, H - 19], outline=RULE, width=1)

    # ---- masthead ----
    d.text((W // 2, 34), "THE WORLD", font=font(SERIF, 96), fill=INK, anchor="ma")
    d.line([40, 138, W - 40, 138], fill=INK, width=3)
    d.text((W // 2, 148), "Wednesday, 25 November 2026",
           font=font(SERIF, 30), fill=RED, anchor="ma")
    d.text((W // 2, 190),
           "THE DAY'S NEWS IN ONE PAGE  —  ALL STORIES FIRST REPORTED TODAY",
           font=font(SANS, 19), fill=GREY, anchor="ma")
    d.line([40, 224, W - 40, 224], fill=INK, width=2)

    # ---- lead story: Shenzhou-24 ----
    lx, ly, lw = 40, 240, W - 80
    d.rectangle([lx, ly, lx + lw, ly + 176], fill=PANEL, outline=RULE, width=1)
    d.text((lx + 20, ly + 12), "SPACE  •  LEAD STORY",
           font=font(SANS_B, 17), fill=RED)
    d.text((lx + 20, ly + 38), "First Pakistani reaches orbit",
           font=font(SERIF, 46), fill=INK)
    d.text((lx + 20, ly + 92),
           "Shenzhou-24 lifts off for Tiangong; Zeeshan Ali is the first",
           font=font(SANS, 21), fill=INK)
    text_block(d, lx + 20, ly + 124,
               "Pakistani in space and the first foreign astronaut aboard China's station.",
               font(SANS, 19), lw - 40, fill=GREY)
    icon_rocket(d, lx + lw - 96, ly + 36, 64, INK)

    # ---- six panels, 2 cols x 3 rows ----
    panels = [
        ("MARKETS", "Asian shares slide on tariff threats",
         "Seoul -5.3%, Taiwan -5.1%, Nikkei -2.9% as the US readies new tariffs.",
         icon_chart_down),
        ("AUSTRALIA", "Inflation jumps to 4.9%",
         "Australia's inflation rate jumps, deepening the cost-of-living squeeze.",
         icon_coins),
        ("PACIFIC", "Australia signs Solomons pact",
         "PMs Albanese and Wale sign a security treaty, a blow to China's sway.",
         icon_flags),
        ("CHINA", "Top Shanghai leader probed",
         "Beijing investigates Politburo member Chen Jining, the Shanghai party chief.",
         icon_magnifier),
        ("IOWA, USA", "Army blasts unstable explosives",
         "The Army detonates 5 tons of lead azide in Iowa at 9 a.m. today.",
         icon_blast),
        ("US ECONOMY", "Inflation data due today",
         "US inflation, GDP and jobs data land today; the Fed is seen hiking in Dec.",
         icon_calendar),
    ]
    pw, ph, gap = 462, 148, 20
    x0, y0 = 40, 432
    for i, (kick, head, body, icon) in enumerate(panels):
        x = x0 + (i % 2) * (pw + gap)
        y = y0 + (i // 2) * (ph + 14)
        d.rectangle([x, y, x + pw, y + ph], fill=PANEL, outline=RULE, width=1)
        d.text((x + 14, y + 10), kick, font=font(SANS_B, 15), fill=RED)
        ty = text_block(d, x + 14, y + 34, head, font(SANS_B, 24),
                        pw - 110, leading=1.12)
        # body uses the same narrow width as the headline so its lines can
        # never run into the icon at the panel's right edge
        text_block(d, x + 14, ty + 4, body, font(SANS, 18), pw - 110,
                   fill=GREY, leading=1.18)
        icon(d, x + pw - 78, y + 30, 58, INK)

    # ---- in brief strip ----
    by = y0 + 3 * ph + 2 * 14 + 12
    d.line([40, by, W - 40, by], fill=INK, width=2)
    d.text((40, by + 10), "IN BRIEF", font=font(SANS_B, 17), fill=RED)
    text_block(d, 40, by + 36,
               "• Sydney jury convicts ex-officer Beau Lamarre-Condon of double murder.  "
               "• Trump is reported open to pardoning Nvidia chief Jensen Huang.  "
               "• WHO chief urges an end to the US fuel blockade on Cuba.",
               font(SANS, 17), W - 80, leading=1.25)

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
