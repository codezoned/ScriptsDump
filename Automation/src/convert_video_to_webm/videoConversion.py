import os
import logging
import subprocess
import jobDistribution as jd

log = logging.getLogger()
handlers = [
    logging.StreamHandler(),
    logging.FileHandler( "VideoConversion.log", mode="a" )
]
formatter = logging.Formatter('%(asctime)s %(message)s')
for handler in handlers:
    log.setLevel( logging.INFO )
    handler.setFormatter( formatter )
    log.addHandler( handler )

OUTPUT_FILETYPE = '.webm'

ACCEPTED_FILETYPES = [
    "mp4",
    "mov"
]

FFMPEG_BIN = os.path.join( './FFMPEG/bin/ffmpeg.exe' )


def get_filepaths(fp):
    file_paths = []
    if os.path.isdir( fp ):
        for root, directories, files in os.walk( fp ):
            for filename in files:
                ext = os.path.splitext( filename )[1][1:]
                if ext in ACCEPTED_FILETYPES:
                    filepath = os.path.join( root, filename )
                    file_paths.append( filepath )
    else:
        file_paths = [ fp ]

    return file_paths


def convert_file(videoFilePath):
    newFileName = os.path.splitext( videoFilePath )[0] + OUTPUT_FILETYPE
    with open( videoFilePath, "rb" ):
        command = [
            FFMPEG_BIN,
            '-i', videoFilePath,
            "-c:v", "libvpx", # codec
            "-vf", "yadif", #Deinterlacing
            "-crf", "4", # The range of the quantizer scale is 4-51: where 4 is near lossless, 23 is default, and 51 is worst possible. A lower value is a higher quality
            "-af", "volume=2dB",
            "-b:v", "10M", # bitrate
            "-c:a", "libvorbis", # stream specifier
            "-q:a", "2",
            newFileName
        ]
        print 'command: {}'.format( command )
        p = subprocess.Popen( command, stdout=subprocess.PIPE )
        while True:
            data = p.stdout.read( 1024 )
            if len( data ) == 0:
                break
            print( data )
        print p.wait()
    return newFileName

if __name__ == "__main__":

    log.info( "Starting Video Conversion" )
    videoPathLocation = ""
    convertedVideos = []

    while not os.path.exists( videoPathLocation ):
        videoPathLocation = raw_input( "Source video location: " )
        originalVids = get_filepaths( videoPathLocation )

    log.info( "File Path Entered: {}".format( videoPathLocation ) )

    for file in originalVids:
        log.info( "Converting the following video file {}".format( file ) )
        convertedFileName = convert_file( file )
        convertedVideos.append( convertedFileName )

    log.info( '::::::::Conversion Complete::::::::' )
    log.info( "New Videos Location: ".format( videoPathLocation ) )
    log.info('-----------------------------------')
    for finVid in convertedVideos:
        log.info( "New Video Converted: {}".format( finVid ) )

    raw_input( "Script Complete. Hit Enter to continue" )
