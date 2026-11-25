# The World — Wednesday, 25 November 2026

A newspaper-style front page summing up the world news of Wednesday
25 November 2026 in one 1024×1024 image, for the make.fun bounty
`news-image-20261125`.

## How it is built

`draw.py` draws the page with PIL (pure vector drawing, no photos):
masthead, a lead story, six news panels and an "In Brief" strip.
`main.ts` copies the finished `entry.png` into
`$MAKEFUN_OUTPUT_DIR` (default `/output`), deterministically, and
fails loudly if the copy is incomplete.

Run it:

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Stories (each first reported on 25 November 2026)

- **Lead — Space:** Shenzhou-24 lifts off for Tiangong; Muhammad
  Zeeshan Ali becomes the first Pakistani in orbit and the first
  foreign astronaut aboard China's station, with Tang Hongbo and Wu Yi
  (Reuters, Xinhua, AP, 25 Nov).
- **Markets:** Asian shares slide as the US readies new tariffs on
  China, the EU and 14 other economies — Seoul −5.3%, Taiwan −5.1%,
  Nikkei −2.9% (Reuters, 25 Nov).
- **Australia:** Inflation jumps to 4.9%, deepening the cost-of-living
  squeeze (The Guardian, 25 Nov).
- **Pacific:** Australia signs a security pact with Solomon Islands;
  PMs Albanese and Wale sign the treaty (The Guardian, 25 Nov).
- **China:** Beijing investigates Politburo member Chen Jining, the
  Shanghai party chief (The Guardian, 25 Nov).
- **Iowa, USA:** The Army detonates 5 tons of lead azide at 9 a.m.
  today after a court clears the controlled blast (AP, The Guardian,
  25 Nov).
- **US economy:** US inflation, GDP and jobs data all land today
  before Thanksgiving; the Fed is seen hiking in December
  (Reuters, 25 Nov).
- **In brief:** Sydney jury convicts ex-officer Beau Lamarre-Condon
  of double murder (The Guardian, 25 Nov); Trump is reported open to
  pardoning Nvidia chief Jensen Huang (The Guardian, 25 Nov); WHO
  chief urges an end to the US fuel blockade on Cuba
  (Al Jazeera, 25 Nov).

Stories checked and deliberately left out although they lead 25 Nov
front pages: the Huawei guilty verdict, the Houthi strike on Riyadh's
tower, the Zelenskiy/Sparta II confirmation, the Giuliani Medal of
Freedom and the CIA/ODNI breach were all Tuesday 24 November events;
the DR Congo plane went missing on Sunday 22 November; the NATO
"Sputnik-S" reports are 23–24 November.

## License

MIT — see LICENSE.
