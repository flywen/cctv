ffmpeg -re -rtsp_transport tcp -i rtsp://admin:12345@192.168.1.231/h264/1/main -codec copy -map 0 -use_localtime 1 -use_localtime_mkdir 1 -hls_segment_filename '%Y%m%d/%H%M%S.ts' playlist.m3u8
