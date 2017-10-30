# YouTube Transcript --> .srt

Convert YouTube transcriptions to `.srt` files

1. Copy the transcripts from YouTube and save in a `.txt` file in the same directory as the `yt2srt.py` script.

Sample input file:

**transcript.txt**

```
00:00
"Who Shouldn't Consume Curcumin or Turmeric"
00:07
Following flax and wheatgrass,
00:09
turmeric is the third best-selling
00:11
botanical dietary supplement,
```

2. Execute the `yt2srt.py` script. It will collect all `.txt` files in the same directory and try to convert to `.srt`:

```
python3 yt2srt.py
```

3. An output file with the same name and `.srt` is created.

Sample output file:

**transcript.srt**

```
1
00:00:00,000 --> 00:00:07,000
"Who Shouldn't Consume Curcumin or Turmeric"

2
00:00:07,000 --> 00:00:09,000
Following flax and wheatgrass,

3
00:00:09,000 --> 00:00:11,000
turmeric is the third best-selling

4
00:00:11,000 --> 00:00:12,000
botanical dietary supplement,
```

4. Manually adjust the the end time of the last entry in the `.srt` file for a better result.
