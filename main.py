from moviepy.editor import AudioFileClip, ImageClip
import argparse
import colorama
import sys

# initialize colorama
colorama.init()

def add_audio(img, audio_file, dest_file):
    '''Quickly and easily add audio effects to your images
    img: Image to use in the video
    audio_file: the audio to use in the video clip
    dest_file: the filename to write the ouput to, should be a .mp4 file
    '''

    print(colorama.Fore.GREEN + "[+] STaRtInG......ThIs MaY tAkE A WhIl3......")

    try:
        # create the audio clip and img clip objects
        audio_clip_file = AudioFileClip(audio_file)
        image_clip_file = ImageClip(img)

        # add an audio file to the img to make it a video
        generated_video_clip = image_clip_file.set_audio(audio_clip_file)

        # set how long you want the video to be, you can use the audio's full length
        generated_video_clip.duration = audio_clip_file.duration

        # don't forget that vids have a frame rate i.e FPS
        generated_video_clip.fps = 2

        # output the result to a file and disable progress output
        generated_video_clip.write_videofile(dest_file, verbose=False, logger=None)

    except OSError as err_1:
        print(colorama.Fore.RED+ "[-] An error occured, Please check that the filepaths specified are correct ")

    except:
        print(colorama.Fore.RED + "[-] Something went Wr0ng.....QUITTING.....")
  

    print(colorama.Fore.GREEN + "[+] Done ")
    sys.exit()


def process_input_params():

    banner = r"""

				██╗██████╗  ██████╗██╗   ██╗
				██║╚════██╗██╔════╝╚██╗ ██╔╝
				██║ █████╔╝██║  ███╗╚████╔╝ 
				██║ ╚═══██╗██║   ██║ ╚██╔╝  
				██║██████╔╝╚██████╔╝  ██║   
				╚═╝╚═════╝  ╚═════╝   ╚═╝   
			[+] https://github.com/monty-iggy-xtius

	"""

    print(colorama.Fore.GREEN + banner)
    # initialize
    input_parser = argparse.ArgumentParser(
        description='Quickly and easily add audio effects to your images')

    # add additional arguments
    input_parser.add_argument(
        'Image_filename', help='Full path to Image file to use in the video')
    input_parser.add_argument(
        'Audio_filename', help='Full path to Audio\\Mp4 file to use in the video clip')
    input_parser.add_argument(
        'Output_filename', help='Full path of the output filename, should be a .mp4 file')

    # parse arguments
    current_args = input_parser.parse_args()

    # access values from command line
    image_file = current_args.Image_filename
    music_file = current_args.Audio_filename
    destination_file = current_args.Output_filename

    # check values
    destination_file_extension = current_args.Output_filename.split(".")
    if destination_file_extension[-1] == "mp4":
        print(colorama.Fore.GREEN + "[+] DeStIn4tI0n fIl3 Ok......pRocEeDiNg")
        add_audio(image_file, music_file, destination_file)
    else:
        print(colorama.Fore.YELLOW + "[-] The destination output file should be an mp4 file e.g video.mp4, type --help for more information")
        sys.exit()


if __name__ == '__main__':
    process_input_params()