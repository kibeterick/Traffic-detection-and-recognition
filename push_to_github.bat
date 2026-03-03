@echo off
echo Updating .gitignore and adding sample images...

git add .gitignore
git add sample_images_fixed/class_00_Speed_limit_20km-h_sample1.jpg
git add sample_images_fixed/class_01_Speed_limit_30km-h_sample1.jpg
git add sample_images_fixed/class_13_Yield_sample1.jpg
git add sample_images_fixed/class_14_Stop_sample1.jpg
git add sample_images_fixed/class_17_No_entry_sample1.jpg

git commit -m "Add sample images and update gitignore"
git push

echo Done!
pause
