# loop over 25 50 and 100 fps

for fps in 25 50 100
do
    # loop over (stack size, step size) tuples (16 ,16), (16,8), (16,1), (32,32), (32,16), (32,1)
    pairs=(
    "16 16"
    "16 8"
    "16 1"
    "32 32"
    "32 16"
    "32 1"
    )

    for pair in "${pairs[@]}"; do
        set -- $pair
        stack_size=$1
        step_size=$2

        video_path="/home/joao/workspace/EquinePainFaceDataset/dataset_balanced/clips/${fps}FPS"

        ls -1 "$video_path" | shuf | sed "s|^|$video_path/|" > list_files.txt

        # create output path
        mkdir -p /home/joao/workspace/EquinePainFaceDataset/dataset_balanced/augmented_features/${fps}FPS/$stack_size/$step_size/

        python main.py \
            feature_type=i3d \
            device="cuda:0" \
            stack_size=$stack_size \
            step_size=$step_size \
            on_extraction=save_numpy \
            output_path=/home/joao/workspace/EquinePainFaceDataset/dataset_balanced/augmented_features/${fps}FPS/$stack_size/$step_size/ \
            file_with_video_paths=list_files.txt
        
        rm -rf list_files.txt
    done
done