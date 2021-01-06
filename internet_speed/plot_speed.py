#!/usr/bin/env python3

"""A script to plot the donwload/upload/ping chart data from speedtest-cli output json file"""

import json
import matplotlib.pyplot as plt

FILE_NAME = 'speedtest_dump.json'
REPORT_FILE_NAME = './report/speedtest_report.txt'
MEGA = 1000000

def load_json_to_list():
    read_list = []
    for line in open(FILE_NAME, 'r'):
        read_list.append(json.loads(line))
    return read_list

def get_parsed_timestamp(raw):
    raw = raw.split('T')
    day = raw[0]
    hour = GMT_to_BRT(raw[1])
    return hour + " / " + day

def GMT_to_BRT(time_raw):
    minutes = time_raw[3:5]
    hour = int(time_raw[:2]) - 3
    return str(hour) + ":" + minutes

def parse_data(raw_data):
    downloads = []
    uploads = []
    pings = []
    timestamps = []
    for i in raw_data:
        timestamp = get_parsed_timestamp(i['timestamp'])
        timestamps.append(timestamp)
        downloads.append(i['download']/MEGA)
        uploads.append(i['upload']/MEGA)
        pings.append(i['ping'])
    return downloads, uploads, pings, timestamps

def plot_download_upload(x1_plot, x2_plot, y_plot):
    plt.plot(y_plot, x1_plot, label='Download')
    plt.plot(y_plot, x2_plot, label='Upload')
    plt.legend(loc='best')
    plt.title('Download and Upload speeds per time measure')
    plt.xlabel('Hour/Date measures')
    plt.ylabel('Speed (Mbps)')
    plt.savefig('./report/download_upload.png')
    plt.clf()

def plot_ping(x_plot, y_plot):
    plt.plot(y_plot, x_plot, label='Ping')
    plt.legend(loc='best')
    plt.title('Ping per time measure')
    plt.xlabel('Hour/Date measures')
    plt.ylabel('Ping (ms)')
    plt.savefig('./report/ping.png')
    plt.clf()

def dump_logs(downloads, uploads, pings, timestamps):
    with open(REPORT_FILE_NAME, 'w') as report:
        report.write('Intenet speed report\n\n')
        for i in range(len(timestamps)):
            report.write('Timestamp: ' + timestamps[i] + '\n')
            report.write('Download: %.2f Mbps\n' % downloads[i])
            report.write('Upload: %.2f Mbps\n' % uploads[i])
            report.write('Ping: %.0fms \n\n' % round(pings[i]))

def main():
    json_loaded = load_json_to_list()
    downloads, uploads, pings, timestamps = parse_data(json_loaded)
    plot_download_upload(downloads, uploads, timestamps)
    plot_ping(pings, timestamps)
    dump_logs(downloads, uploads, pings, timestamps)

if __name__ == '__main__':
    main()
