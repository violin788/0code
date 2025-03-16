exec(open('util.py').read())
#video_path = "path_to_your_video_file.mp4"
video_path = "C:\\Users\\--\\Downloads\\nevada.mp4"

import os
from scenedetect import VideoManager
from scenedetect import SceneManager
from scenedetect.detectors import ContentDetector

def find_scenes(video_path, threshold=30.0):
    # Create a video manager to handle video loading and scene detection.
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))
    
    # Start video processing and scene detection.
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    
    # Obtain list of detected scenes.
    scene_list = scene_manager.get_scene_list(video_manager.get_base_timecode())
    
    return scene_list

def split_video_into_scenes(video_path, scene_list):
    # Create a directory to save the scene clips
    output_dir = os.path.splitext(video_path)[0] + "_scenes"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize the video manager to process each scene
    video_manager = VideoManager([video_path])
    
    for i, scene in enumerate(scene_list):
        start_frame = scene[0].get_frames()
        end_frame = scene[1].get_frames() if scene[1] else video_manager.get_num_frames()
        
        # Set the duration of the scene to be processed
        video_manager.set_duration(start_frame=start_frame, end_frame=end_frame)
        
        # Construct the output filename
        output_file = os.path.join(output_dir, f"scene_{i+1}.mp4")
        
        # Start the scene detection process
        video_manager.start()
        
        # Split the video and save the segment
        video_manager.split_video(output_file, start_frame=start_frame, end_frame=end_frame)
        print(f"Scene {i+1} saved as {output_file}")

if __name__ == "__main__":
    #video_path = "path_to_your_video_file.mp4"
    threshold = 30.0  # Adjust this threshold as needed (lower for more sensitivity)
    
    # Step 1: Find scenes in the video
    scene_list = find_scenes(video_path, threshold)
    
    # Step 2: Split the video into scenes and save them as separate clips
    split_video_into_scenes(video_path, scene_list)
