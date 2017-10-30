import glob


def convert_youtube_subtitle_to_srt(youtube_subtitles_filename):
    base_filename = youtube_subtitles_filename.split('.')[0]
    srt_out_filename = '%s.srt' % base_filename
    subtitles = list()
    with open(youtube_subtitles_filename, 'r') as infile:
        lines = infile.readlines()
        previous = None
        for index, line in enumerate(lines):
            text = ' '.join(line.split())
            if index % 2 == 0:
                entry = {'start_time': text}
                if previous is not None:
                    previous['end_time'] = text
            else:
                entry['subtitle'] = text
                subtitles.append(entry)
                previous = entry
        if previous is not None:
            previous['end_time'] = previous['start_time']

    with open(srt_out_filename, 'w') as outfile:
        for index, entry in enumerate(subtitles):
            outfile.write('{0}\n'.format(index + 1))
            outfile.write('00:{0},000 --> 00:{1},000\n'.format(entry['start_time'], entry['end_time']))
            outfile.write('{0}\n'.format(entry['subtitle']))
            outfile.write('\n')


def main():
    files = glob.glob('*.txt')
    for filename in files:
        convert_youtube_subtitle_to_srt(filename)


if __name__ == '__main__':
    main()
